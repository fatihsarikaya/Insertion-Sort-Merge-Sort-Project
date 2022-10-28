
# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 


#########################################################
'''
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız !

  Dizinin root elemanı 5 olarak seçilir. 
    Her bir adımda kendisinden küçükler sola, büyükler sağa olacak şekilde ağacın yapısına yerleştirilir.
            
                         5 
                    /        \
                   3          7  
                  / \        / \ 
                 1   4      6   8        
                / \              \     
               0   2              9       
'''