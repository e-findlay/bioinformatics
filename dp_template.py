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
scoringMatrix = []
backtrackingMatrix = []
counter=0
for i in range(len(seq1)):
    scoringMatrix.append([])
    backtrackingMatrix.append([])
    for j in range(len(seq2)):
        scoringMatrix[counter].append(0)
        backtrackingMatrix[counter].append('')
    counter+=1
scoreValues = {'A': 4, 'C': 3, 'G': 2, 'T': 1}
for i in range(0, len(seq1)):
    for j in range(0, len(seq2)):
        if j == 0:
            scoringMatrix[i][0], backtrackingMatrix[i][0] = -2*i, 'L'
        elif i == 0:
            scoringMatrix[0][j], backtrackingMatrix[0][j] = -2*j, 'U'
        else:
            if seq1[i] == seq2[j]:
                score = scoreValues[seq1[i]] + scoringMatrix[i-1][j-1]
            else:
                score = -3 + scoringMatrix[i-1][j-1]
            direction = 'D'
            next_score = scoringMatrix[i][j-1] -2
            if next_score > score:
                score = next_score
                direction = 'U'
            next_score =  scoringMatrix[i-1][j] -2
            if next_score > score:
                score = next_score
                direction = 'L'
            scoringMatrix[i][j] = score
            backtrackingMatrix[i][j] = direction    
backtrackingMatrix[0][0] = 'END'
seq1 = list(seq1[1:])
seq2 = list(seq2[1:])
alignment1, alignment2 = '', ''
y,x = -1, -1
best_score = scoringMatrix[-1][-1]
best_alignment = []
while backtrackingMatrix[x][y] != 'END':
    coords=backtrackingMatrix[x][y]
    if coords == 'D':
        y, x = y-1, x-1
        alignment1 += seq1.pop()
        alignment2 += seq2.pop()
    elif coords == 'U':
        y -= 1
        alignment1 += '-'
        alignment2 += seq2.pop()
    else:
        x -= 1
        alignment1 += seq1.pop()
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

