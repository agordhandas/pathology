__author__ = 'AnkitAthos'

import variables

mirror = variables.exons
idx = []
counter = 1

for i in range(len(variables.gene)):
    letter = variables.gene[i]
    if letter.isupper():
        if mirror[0].isupper():
            idx.append(counter)
            counter = counter + 1
            mirror = mirror[1:]
        else:
            idx.append ('nan')
            mirror = mirror[1:]
    else:
        idx.append ('nan')

def whatsTheIdx (number):
    global idx
    codonIdx = [i for i in range(len (idx)) if idx[i] == number][0] + 117120017
    return codonIdx