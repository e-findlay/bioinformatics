#!/usr/bin/python
import time
import sys
import numpy as np

# YOUR FUNCTIONS GO HERE -------------------------------------

    
    
    


# 1. Populate the scoring matrix and the backtracking matrix

# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
seq1 = '-{}'.format(seq1)
seq2 = '-{}'.format(seq2)
scoringMatrix = np.zeros((len(seq2), len(seq1)))
backtrackingMatrix = np.empty((len(seq2), len(seq1)), dtype=object)
scoreValues = {'A': 4, 'C': 3, 'G': 2, 'T': 1}
directionValues = {1: 'D', 2: 'L', 3: 'U'}
for i in range(0, len(seq1)):
    for j in range(0, len(seq2)):
        if j == 0:
            scoringMatrix[0,i], backtrackingMatrix[0,i] = -2*i, 'L'
        elif i == 0:
            scoringMatrix[j,0], backtrackingMatrix[j,0] = -2*j, 'U'
        else:
            if seq1[i] == seq2[j]:
                score = scoreValues[seq1[i]] + scoringMatrix[j-1, i-1]
            else:
                score = -3 + scoringMatrix[j-1, i-1]
            direction = 1
            next_score = scoringMatrix[j,i-1] -2
            if next_score > score:
                score = next_score
                direction = 2
            next_score =  scoringMatrix[j-1,i] -2
            if next_score > score:
                score = next_score
                direction = 3
            scoringMatrix[j,i] = score
            backtrackingMatrix[j,i] = directionValues[direction]    
backtrackingMatrix[0,0] = 'END'
seq1 = seq1[1:]
seq2 = seq2[1:]
alignment1, alignment2 = '', ''
y,x = backtrackingMatrix.shape
y,x = y-1, x-1
best_score = scoringMatrix[-1,-1]
best_alignment = []
while backtrackingMatrix[y,x] != 'END':
    coords=backtrackingMatrix[y,x]
    if coords == 'D':
        y, x = y-1, x-1
        alignment1 += seq1[-1]
        seq1 = seq1[:-1]
        alignment2 += seq2[-1]
        seq2 = seq2[:-1]
    elif coords == 'U':
        y -= 1
        alignment1 += '-'
        alignment2 += seq2[-1]
        seq2 = seq2[:-1]
    else:
        x -= 1
        alignment1 += seq1[-1]
        seq1 = seq1[:-1]
        alignment2 += '-'
best_alignment.append(alignment1[::-1])
best_alignment.append(alignment2[::-1])    




#-------------------------------------------------------------

    
                
    

# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

