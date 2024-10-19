# Imports
import math
import string
import sys


# Dictionary + List Instance
fileCount = {}
fileOutput = []

# Input
testCases = int(sys.stdin.readline().strip())

# Getting Every File 
for x in range(testCases):
    fileNames = sys.stdin.readline().strip().split(".")
    # Determining if File Count exists + Increasing File Count
    if fileNames[1] not in fileCount:
        fileCount.update({fileNames[1]: 1})
    else:
        fileCount.update({fileNames[1]: fileCount.get(fileNames[1]) + 1})

   # Lists Stuff (Clear old Cache and Shows new one)
    fileOutput.clear()
    fileOutput += fileCount.keys()

# Output
for x in range(len(fileOutput)):
    print(fileOutput[x], fileCount.get(fileOutput[x]))