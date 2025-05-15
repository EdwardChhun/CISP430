from PIL import Image
import sys
import os

class Octree:
    
    class OTNode:
        
        def __init__(self, parent=None, level=0, outer=None):
            self.red = 0
            self.green = 0
            self.blue = 0
            self.count = 0
            self.parent = parent
            self.level = level
            self.oTree = outer
            self.children = [None] * 8
            
        def insert(self, r, g, b, level, outer):
            if level < self.oTree.max_level:
                idx = self.compute_index(
                    r, g, b, level
                )
                if self.children[idx] == None:
                    self.children[idx] = outer.OTNode(
                        parent=self,
                        level=level + 1,
                        outer=outer,
                    )
                self.children[idx].insert(
                    r, g, b, level + 1, outer
                )
            else:
                if self.count == 0:
                    self.oTree.num_leaves = (
                        self.oTree.num_leaves + 1
                    )
                    self.oTree.all_leaves.append(self)
                self.red += r
                self.green += g
                self.blue += b
                self.count = self.count + 1

        def compute_index(self, r, g, b, l):
            shift = 8 - l
            rc = (r >> (shift - 2)) & 0x4
            gc = (g >> (shift - 1 ))& 0x2
            bc = (b >> shift) & 0x1
            return rc | gc | bc
        
        def find(self, r, g, b, level):
            if level < self.oTree.max_level:
                idx = self.compute_index(r, g, b, level)
                if self.children[idx]:
                    return self.children[idx].find(
                        r, g, b, level + 1
                    )
                elif self.count > 0:
                    return (
                        self.red // self.count,
                        self.green // self.count,
                        self.blue // self.count,
                    )
                else:
                    print("No leaf node to represent this color")
            else:
                return (
                    self.red // self.count,
                    self.green // self.count,
                    self.blue // self.count,
                )
        
        def merge(self):
            for child in [c for c in self.children if c]:
                if child.count > 0:
                    self.oTree.all_leaves.remove(child)
                    self.oTree.num_leaves -= 1
                else:
                    print("Recursively merging non-leaf...")
                    child.merge()
                self.count += child.count
                self.red += child.red
                self.green += child.green
                self.blue += child.blue
            for i in range(8):
                self.children[i] = None
                
    def __init__(self):
        self.root = None
        self.max_level = 5
        self.num_leaves = 0
        self.all_leaves = []

    def insert(self, r, g, b):
        if not self.root:
            self.root = self.OTNode(outer=self)
        self.root.insert(r, g, b, 0, self)

    def find(self, r, g, b):
        if self.root:
            return self.root.find(r, g, b, 0)

    def reduce(self, max_cubes):
        while len(self.all_leaves) > max_cubes:
            smallest = self.find_min_cube()
            smallest.parent.merge()
            self.all_leaves.append(smallest.parent)
            self.num_leaves = self.num_leaves + 1

    def find_min_cube(self):
        min_count = sys.maxsize
        max_level = 0
        min_cube = None
        for i in self.all_leaves:
            if (
                i.count <= min_count
                and i.level >= max_level
            ):
                min_cube = i
                min_count = i.count
                max_level = i.level
        return min_cube

def build_and_display(filename):
    img = Image.open(filename)
    w, h = img.size
    ot = Octree()
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            ot.insert(r, g, b)
    ot.reduce(256)

    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            nr, ng, nb = ot.find(r, g, b)
            img.putpixel((col, row), (nr, ng, nb))
    img.show()
    
    img.save("output/"+filename.strip("input")+"_quantized.bmp")