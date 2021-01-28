import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/djawed/Images/manutentionnaire.png',0)

## slicing en 3x3



## the vertical edges detection
matrice= [[-1,-2,-1],[0,0,0],[1,2,1]]
verticaleEdges=img


for x in range(0,verticaleEdges.shape[0]):
    for y in range(0,verticaleEdges.shape[1]):
       
       
        verticaleEdges[y:y+3,x:x+3]      
        verticaleEdges[y,x]=verticaleEdges[y,x]*matrice[0][0]
        verticaleEdges[y+1,x+1]=verticaleEdges[y+1,x+1]*matrice[0][1]
        verticaleEdges[y+2,x+2]=verticaleEdges[y+2,x+2]*matrice[0][2]
        
        verticaleEdges[y,x]=verticaleEdges[y,x]*matrice[1][0]
        verticaleEdges[y+1,x+1]=verticaleEdges[y+1,x+1]*matrice[1][1]
        verticaleEdges[y+2,x+2]=verticaleEdges[y+2,x+2]*matrice[1][2]
        
        verticaleEdges[y,x]=verticaleEdges[y,x]*matrice[2][0]
        verticaleEdges[y+1,x+1]=verticaleEdges[y+1,x+1]*matrice[2][1]
        verticaleEdges[y+2,x+2]=verticaleEdges[y+2,x+2]*matrice[2][2]
        
        
        
        
        
      


