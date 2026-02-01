"""
 * Python 3.11

 * GPL-3.0 license
"""

import tkinter
import math

class CONTROLS_VALUE(tkinter.Frame):    
    
    def __init__(s, master, name, units, value):
        super().__init__(master)
        s.config(bg = "black", padx = 5, pady = 5)
        
        s.value = value
        s.min = s.MinDoubleValue(value[0])
        s.max = s.MaxDoubleValue(value[0])
        s.name = name
        s.units = units
        
        s.valueLabel = tkinter.Label(s)
        text = name + "="
        # text = text + str(sigfig.round(value[0], sigfigs = 3)) + units
        text = text + "{:.2e}".format(value[0]) + units
        s.textLabel = tkinter.StringVar()
        s.textLabel.set(text)
        s.valueLabel.config(textvariable = s.textLabel) # textLabel pass as reference. 
        s.valueLabel.pack()

        tghf2 = tkinter.Frame(s)
        tghf2.pack(fill = "both", expand = True)

        tgvfValue = tkinter.Frame(tghf2)
        tgvfValue.pack(side = "left", fill = "both", expand = True)

        s.maxNumberEntry = tkinter.Entry(tgvfValue)
        s.maxNumberEntry.pack(anchor = "ne", expand = True) # n: north
        s.textMax = tkinter.StringVar()
        s.textMax.set(s.max)
        s.maxNumberEntry.config(textvariable = s.textMax, width = 5)
        s.maxNumberEntry.bind("<KeyRelease>", s.DoMax)

        s.valueNumberEntry = tkinter.Entry(tgvfValue)
        s.valueNumberEntry.pack(anchor = "e", expand = True) # e: east
        s.textValue = tkinter.StringVar()
        s.textValue.set(s.value[0])
        s.valueNumberEntry.config(textvariable = s.textValue, width = 5)
        s.valueNumberEntry.bind("<KeyRelease>", s.DoValue)

        s.minNumberEntry = tkinter.Entry(tgvfValue)
        s.minNumberEntry.pack(anchor="se", expand = True) # s: south
        s.textMin = tkinter.StringVar()
        s.textMin.set(s.min)
        s.minNumberEntry.config(textvariable = s.textMin, width = 5)
        s.minNumberEntry.bind("<KeyRelease>", s.DoMin)

        s.valueSlider = tkinter.Scale(tghf2, from_= -100, to = 0, orient = "vertical", showvalue = False,  command=s.MoveSlider)
        s.valueSlider.pack(side = "left", fill = "both", expand = True)
        s.fromDoValue = True
        s.valueSlider.set(-((s.value[0] - s.min)*100.00/(s.max-s.min)))

    def MinDoubleValue(s, doubleValue):
        if(doubleValue == 0.0):
            return -1.0
        if(doubleValue > 0.0):
            return 0.0
            
        # if(doubleValue < 0.0):
        doubleValue = doubleValue * (-1.0) # absolute value of doubleValue
        log10 = math.log10(doubleValue*1.1) # 1.1 times, is necessary when doubleValue is 0.1, 0.01, ... 10^(-n)
        exp10 = 0 # exp10 must be integer
        if(log10 < 0.0):
            exp10 = int(log10)
        else:
            exp10 = int(log10 + 1.0)
        minVal = -math.pow(10.0, exp10)
        if(doubleValue < minVal):
            return -doubleValue*10.0
        return minVal

    def MaxDoubleValue(s, doubleValue):
        if(doubleValue == 0.0):
            return 1.0
        if(doubleValue < 0.0):
            return 0.0
        
        # if(doubleValue > 0.0):
        log10 = math.log10(doubleValue*1.1) # 1.1 times, is necessary when doubleValue is 0.1, 0.01, ... 10^(-n)
        exp10 = 0 # exp10 must be integer
        if(log10 < 0.0):
            exp10 = int(log10)
        else:
            exp10 = int(log10 + 1.0)
        maxVal = math.pow(10.0, exp10)
        if(doubleValue > maxVal):
            return doubleValue*10.0
        return maxVal

    def DoMax(s, *args): # is necessary *args
        try:
            newValue = float(s.textMax.get())
        except ValueError:
            s.textMax.set(str(s.max))
            return
        
        if(newValue <= s.min):
            s.textMax.set(str(s.max))
            return

        if(newValue >= s.value[0]):
            s.max = newValue
        else:
            s.max = s.value[0]
            s.textMax.set(str(s.value[0]))

        s.valueSlider.set(-((s.value[0] - s.min)*100.00/(s.max-s.min)))

    def DoValue(s, *args):
        try:
            newValue = float(s.textValue.get())
        except ValueError:
            s.textValue.set(str(s.value[0]))
            return

        if((s.min <= newValue) & (newValue <= s.max)):
            s.value[0] = newValue
        elif(s.min > newValue):
            s.value[0] = s.min
            s.textValue.set(str(s.min))
        elif(newValue > s.max):
            s.value[0] = s.max
            s.textValue.set(str(s.max))
        
        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

        s.fromDoValue = True
        s.valueSlider.set(-((s.value[0] - s.min)*100.00/(s.max-s.min)))
        

    def MoveSlider(s, event): # is necessary parameter event
        if s.fromDoValue:
            s.fromDoValue = False
            return
        s.value[0] = (-1.0*s.valueSlider.get()/100.00)*(s.max-s.min) + s.min
        s.textValue.set(s.value[0])

        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

    def DoMin(s, *args):
        try:
            newValue = float(s.textMin.get())
        except ValueError:
            s.textMin.set(str(s.min))
            return
        
        if(newValue >= s.max):
            s.textMin.set(str(s.min))
            return

        if(newValue <= s.value[0]):
            s.min = newValue
        else:
            s.min = s.value[0]
            s.textMin.set(str(s.value[0]))

        s.valueSlider.set(-((s.value[0] - s.min)*100.00/(s.max-s.min)))

class CONTROLS_SCIENTIFIC(tkinter.Frame):
    
    def __init__(s, master, name, units, value):
        super().__init__(master)
        s.config(bg = "black", padx = 5, pady = 5)
        s.value = value

        if(value[0] == 0.0):
            s.fac = 0.0
            s.minFac = 0.0
            s.maxFac = 10.0
            s.exp = 0 # exp must be an integer
            s.minExp = -5 # minExp must be an integer
            s.maxExp = 5 # maxExp must be an integer
        else:
            log10 = math.log10(abs(value[0])*1.1) # 1.1 times, is necessary when abs(value[0]) is 0.1, 0.01, ... 10^(-n)
            if(log10 < 0.0):
                s.exp = int(log10-1.0)
            else:
                s.exp = int(log10)

            if(value[0] < 0.0):
                s.minFac = -10.0
                s.maxFac = 0.0
            else:
                s.minFac = 0.0
                s.maxFac = 10.0
            s.fac = value[0]/math.pow(10.0, s.exp)
            s.maxExp = s.exp + 5
            s.minExp = s.exp - 5
        
        s.name = name
        s.units = units

        s.valueLabel = tkinter.Label(s)
        text = name + "="
        text = text + "{:.2e}".format(s.value[0]) + units
        s.textLabel = tkinter.StringVar()
        s.textLabel.set(text)
        s.valueLabel.config(textvariable = s.textLabel) # textLabel pass as reference. 
        s.valueLabel.pack()

        tghf2 = tkinter.Frame(s)
        tghf2.pack(fill = "both", expand = True)

        tgvfFac = tkinter.Frame(tghf2)
        tgvfFac.pack(side = "left", fill = "both", expand = True)

        s.maxFacNumberEntry = tkinter.Entry(tgvfFac)
        s.maxFacNumberEntry.pack(anchor = "ne", expand = True) # n: north
        s.textMaxFac = tkinter.StringVar()
        s.textMaxFac.set(str(s.maxFac))
        s.maxFacNumberEntry.config(textvariable = s.textMaxFac, width = 5) # textMaxFac pass as reference
        s.maxFacNumberEntry.bind("<KeyRelease>", s.DoMaxFac)

        s.facNumberEntry = tkinter.Entry(tgvfFac)
        s.facNumberEntry.pack(anchor = "e", expand = True) # e: east
        s.textFac = tkinter.StringVar()
        s.textFac.set(str(s.fac))
        s.facNumberEntry.config(textvariable = s.textFac, width = 5) # textFac pass as reference
        s.facNumberEntry.bind("<KeyRelease>", s.DoFac)

        s.minFacNumberEntry = tkinter.Entry(tgvfFac)
        s.minFacNumberEntry.pack(anchor = "se", expand = True) # n: north
        s.textMinFac = tkinter.StringVar()
        s.textMinFac.set(str(s.minFac))
        s.minFacNumberEntry.config(textvariable = s.textMinFac, width = 5) # textMinFac pass as reference
        s.minFacNumberEntry.bind("<KeyRelease>", s.DoMinFac)

        s.facSlider = tkinter.Scale(tghf2, from_= -100, to = 0, orient = "vertical", showvalue = False,  command=s.MoveFacSlider)
        s.facSlider.pack(side = "left", fill = "both", expand = True)
        s.fromDoFac = True
        s.facSlider.set(-((s.fac - s.minFac)*100/(s.maxFac-s.minFac)))

        tgvfExp = tkinter.Frame(tghf2)
        tgvfExp.pack(side = "left", fill = "both", expand = True)

        s.maxExpNumberEntry = tkinter.Entry(tgvfExp)
        s.maxExpNumberEntry.pack(anchor = "ne", expand = True) # n: north
        s.textMaxExp = tkinter.StringVar()
        s.textMaxExp.set(str(s.maxExp))
        s.maxExpNumberEntry.config(textvariable = s.textMaxExp, width = 5) # textMaxFac pass as reference
        s.maxExpNumberEntry.bind("<KeyRelease>", s.DoMaxExp)

        s.expNumberEntry = tkinter.Entry(tgvfExp)
        s.expNumberEntry.pack(anchor = "e", expand = True) # c: center
        s.textExp = tkinter.StringVar()
        s.textExp.set(str(s.exp))
        s.expNumberEntry.config(textvariable = s.textExp, width = 5) # textFac pass as reference
        s.expNumberEntry.bind("<KeyRelease>", s.DoExp)

        s.minExpNumberEntry = tkinter.Entry(tgvfExp)
        s.minExpNumberEntry.pack(anchor = "se", expand = True) # n: north
        s.textMinExp = tkinter.StringVar()
        s.textMinExp.set(str(s.minExp))
        s.minExpNumberEntry.config(textvariable = s.textMinExp, width = 5) # textMinFac pass as reference
        s.minExpNumberEntry.bind("<KeyRelease>", s.DoMinExp)

        s.expSlider = tkinter.Scale(tghf2, from_= -100, to = 0, orient = "vertical", showvalue = False,  command=s.MoveExpSlider)
        s.expSlider.pack(side = "left", fill = "both", expand = True)
        s.fromDoExp = True
        s.expSlider.set(-((s.exp - s.minExp)*100/(s.maxExp-s.minExp)))

    def DoMaxFac(s, *args):
        try:
            newValue = float(s.textMaxFac.get())
        except ValueError:
            s.textMaxFac.set(str(s.maxFac))
            return
        
        if(newValue <= s.minFac):
            s.textMaxFac.set(str(s.maxFac))
            return

        if newValue >= s.fac:
            s.maxFac = newValue
        else:
            s.maxFac = s.fac
            s.textMaxFac.set(str(s.fac))
        
        s.facSlider.set(-((s.fac - s.minFac)*100.0/(s.maxFac - s.minFac)))

    def DoFac(s, *args):
        try:
            newValue = float(s.textFac.get())
        except ValueError:
            s.textFac.set(str(s.fac))
            return
        
        if (s.minFac <= newValue) & (newValue <= s.maxFac):
            s.fac = newValue
        elif s.minFac > newValue:
            s.fac = s.minFac
            s.textFac.set(str(s.minFac))
        elif newValue > s.maxFac:
            s.fac = s.maxFac
            s.textFac.set(str(s.maxFac))
        
        s.value[0] = s.fac*math.pow(10.0, s.exp)
        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

        s.fromDoFac = True
        s.facSlider.set(-((s.fac - s.minFac)*100/(s.maxFac - s.minFac)))

    def MoveFacSlider(s, event):
        if s.fromDoFac:
            s.fromDoFac = False
            return

        s.fac = (-1.0*s.facSlider.get()/100.0)*(s.maxFac - s.minFac) + s.minFac
        s.textFac.set(str(s.fac))

        s.value[0] = s.fac*math.pow(10.0, s.exp)
        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

    def DoMinFac(s, *args):
        try:
            newValue = float(s.textMinFac.get())
        except ValueError:
            s.textMinFac.set(str(s.minFac))
            return
        
        if(newValue >= s.maxFac):
            s.textMinFac.set(str(s.minFac))
            return

        if newValue <= s.fac:
            s.minFac = newValue
        else:
            s.minFac = s.fac
            s.textMinFac.set(str(s.fac))
        
        s.facSlider.set(-((s.fac - s.minFac)*100.0/(s.maxFac - s.minFac)))

    def DoMaxExp(s, *args):
        try:
            newValue = int(s.textMaxExp.get())
        except ValueError:
            s.textMaxExp.set(str(s.maxExp))
            return
        
        if(newValue <= s.minExp):
            s.textMaxExp.set(str(s.maxExp))
            return

        if newValue >= s.exp:
            s.maxExp = newValue
        else:
            s.maxExp = s.exp
            s.textMaxExp.set(str(s.exp))
        
        s.expSlider.set(-((s.exp - s.minExp)*100/(s.maxExp - s.minExp)))

    def DoExp(s, *args):
        try:
            newValue = int(s.textExp.get())
        except ValueError:
            s.textExp.set(str(s.exp))
            return
        
        if (s.minExp <= newValue) & (newValue <= s.maxExp):
            s.exp = newValue
        elif s.minExp > newValue:
            s.exp = s.minExp
            s.textExp.set(str(s.minExp))
        elif newValue > s.maxExp:
            s.exp = s.maxExp
            s.textExp.set(str(s.maxExp))
        
        s.value[0] = s.fac*math.pow(10.0, s.exp)
        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

        s.fromDoExp = True
        s.expSlider.set(-((s.exp - s.minExp)*100.0/(s.maxExp - s.minExp)))

    def MoveExpSlider(s, event):
        if s.fromDoExp:
            s.fromDoExp = False
            return

        s.exp = int((-1.0*s.expSlider.get()/100.0)*(s.maxExp - s.minExp) + s.minExp)
        s.textExp.set(str(s.exp))

        s.value[0] = s.fac*math.pow(10.0, s.exp)
        text = s.name + "="
        text = text + "{:.2e}".format(s.value[0]) + s.units
        s.textLabel.set(text)

    def DoMinExp(s, *args):
        try:
            newValue = int(s.textMinExp.get())
        except ValueError:
            s.textMinExp.set(str(s.minExp))
            return
        
        if(newValue >= s.maxExp):
            s.textMinExp.set(str(s.minExp))
            return

        if newValue <= s.exp:
            s.minExp = newValue
        else:
            s.minExp = s.exp
            s.textMinExp.set(str(s.exp))
        
        s.expSlider.set(-((s.exp - s.minExp)*100.0/(s.maxExp - s.minExp)))
