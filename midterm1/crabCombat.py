from linkedList import DoublyLinkedList

# Recursion <3
def foo(deck1, deck2): # Both decks are DoublyLinkedLists
    
    # Base Case:
    if deck1.is_empty() or deck2.is_empty():
        return deck1 if not deck1.is_empty() else deck2
    
    # Recursive Case:
    # Step 1: Take the first card of both decks and compare
    # Step 2: Remove the lower number from said deck, and append both cards to the winning player's deck
    #         Append as such x, x, x, biggerCard, smallerCard 
    # NOTE  : All of these operations are made to mutate the doubly linked list
    # Step 3: Recursively call the function such that it ends with a person winning with all the cards
    
    else:
        
        card1 = deck1._head._data
        card2 = deck2._head._data
        
        if card1 > card2:
            
            deck1.remove(card1)         # Take both cards and append it to 
            deck2.remove(card2)         # the bottom of winning deck
            
            deck1.append(card1)
            deck1.append(card2)
        
        else:                           # If card1 < card2 
            
            deck1.remove(card1)         
            deck2.remove(card2)
            
            deck2.append(card2)
            deck2.append(card1)
        
        # We can safely assume that the players will not get the same cards
    
    return foo(deck1, deck2)
    
    
def calculate_score(deck):
    """Calculate the score of the winning deck"""
    
    total = 0
    
    for index in range(len(deck)):
    
        total += deck.removeLast() * (index + 1)    # to get position 
                                                    # NOTE: This mutates the original dll 
    return total


if __name__ == "__main__":
    
    
    
    # ---- TEST CASE ---- 
    p1 = DoublyLinkedList()
    p2 = DoublyLinkedList()
        
    for p1Card in [9, 2, 6, 3, 1]:
        p1.append(p1Card)
        
    for p2Card in [5,8, 4, 7, 10]:
        p2.append(p2Card)
        
    winningDeckTest = foo(p1, p2)
    print(calculate_score(winningDeckTest))
    # -------------------
    
    

    # ---- PART TWO ----
    deck1 = DoublyLinkedList()
    deck2 = DoublyLinkedList()
    
    with open("8_p1.txt") as f:
        for i in f:
            deck1.append(int(i))
            
    with open("8_p2.txt") as f:
        for i in f:
            deck2.append(int(i))
        
    winningDeck = foo(deck1, deck2)
    print(calculate_score(winningDeck))
    # ------------------