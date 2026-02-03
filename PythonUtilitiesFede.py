"""
 * Python 3.11

 * GPL-3.0 license
"""
import sys
def FindText(filePath, text):
    with open(filePath, 'r') as file:
        for row, lineText in enumerate(file, start=0):
            if text in lineText:
                col = lineText.find(text)
                return (row, col)
    return (None, None)


b = "\b \b" # Erase a char
def PrintValStatic(backCounts, text):
    sys.stdout.write(b*backCounts)
    c = sys.stdout.write(text); sys.stdout.flush()
    return c # number of written chars
