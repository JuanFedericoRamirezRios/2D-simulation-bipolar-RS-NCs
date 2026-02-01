"""
 * Python 3.11

 * GPL-3.0 license
"""
def FindText(filePath, text):
    with open(filePath, 'r') as file:
        for row, lineText in enumerate(file, start=0):
            if text in lineText:
                col = lineText.find(text)
                return (row, col)
    return (None, None)
