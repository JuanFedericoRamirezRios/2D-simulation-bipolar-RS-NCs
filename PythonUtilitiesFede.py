"""
 * Python 3.11

 * GPL-3.0 license
"""
import sys
import os
import typing

def LoadParams(filePath) -> typing.List[str]:
    """
    The format is "...:(space)value(line break)"
    Exms: 
    "Experimental data: K-63-RT_exp_corrct.dat" -> "K-63-RT_exp_corrct.dat"
    "N_LRS: 0.2" -> "0.2"
    "t_0 gener-recomb: 5e-06 s" -> "5e-06 s"
    """
    if not os.path.exists(filePath):
        print("Warning:", filePath, "not exist.")
        return None
    params = []
    with open(filePath, 'r') as file:
        for lineText in file:
            posInLine = lineText.find(": ") # When not find ": ", return -1
            if(posInLine > -1):
                if lineText[-1] == '\n':
                    params.append(lineText[posInLine+2:-1]) # -1 to eliminate '\n'
                else: # The lineText is the last line of file.
                    params.append(lineText[posInLine+2:])
    return params

def FindInText(text, string) -> typing.Tuple[int, int, str]:
    lines = text.splitlines()
    for row, lineText in enumerate(lines, start=0):
        if string in lineText:
            col = lineText.find(string)
            return (row, col, lineText)

    return (None, None, None)

def FindInPlainText(filePath, string) -> typing.Tuple[int, int, str]:
    if not os.path.exists(filePath):
        print("Warning:", filePath, "not exist.")
        return (None, None, None)
    with open(filePath, 'r') as file:
        for row, lineText in enumerate(file, start=0):
            if string in lineText:
                col = lineText.find(string)
                return (row, col, lineText)
    return (None, None, None)


b = "\b \b" # Erase a char
def PrintValStatic(backCounts, text) -> int:
    sys.stdout.write(b*backCounts)
    c = sys.stdout.write(text); sys.stdout.flush()
    return c # number of written chars
