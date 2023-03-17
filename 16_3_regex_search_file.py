import re

# X-DSPAM-Confidence: 0.84575
# Task: Find the lines beginning with 'X-DSPAM-Confidence:' to extract number and finally compute the maximum of the number

fhandle = open('16_3_mbox-short.txt')
numlist = list()

for line in fhandle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)

'''
Breakdown of the RegEx 
^X-DSPAM-Confidence: ([0-9.]+)

^X-DSPAM-Confidence:    -   Starting with '^X-DSPAM-Confidence:' and followed a space
(  -   start extracting
a digit or period
+   -   at least one or more
)  -   stop extracting
'''

print('Maximum', max(numlist))