# NOTE: 
- Need at least 2 filters, 1 being quantization from 8.5
- Use atleast 2 diff data structures

# TODO:
- Write-up for O(n) for data structures
- Video, screenshare
    - Logic flow diagram
    - Demo

# Filters included in this program

## Quantization filter
- I'm gonna be using an Octree datatype which is like a binary tree but with 8 children on each node
- Show comparisons 

## Blur [Reference](https://medium.com/@rohit-krishna/coding-gaussian-blur-operation-from-scratch-in-python-f5a9af0a0c0f)
- Gaussian blur using matrix operations/convolution networks

## Edge Detection
- Talk about police catching perpetrators by using CCTV footage and analysing the tattoos to detect the distinct gang related tattoos and solving a case of a hit and run.
- This segways fro the Blur filter, basically a difference in Gaussian Blurs
- Subtracting each pixel of the image with a stronger Gaussian Blur to a smaller one