<img src="AttachmentsREADME/k61.gif" alt="k61-GIF" width="500"/>
<img src="AttachmentsREADME/k63.gif" alt="k61-GIF" width="700"/>

##### Compile: pyinstaller --onefile --add-binary "CalcsCpp.dll;." 2D_RRAM_NCs_DCmode.py
By GenerateGIF.exe you can create a .gif after "DRAW LAST SIMULATION" button. Usage of GenerateGIF.exe in my repository: https://github.com/JuanFedericoRamirezRios/Generator-GIF

# 2D-simulation-bipolar-RS-NCs
2D simulation of Resistive switching memory of oxides with conductive-nanocrystals embedded. The simulation emulates the DC voltage stimulus (voltage sweep). If you use this software, cite: https://doi.org/10.3390/nano13142124

## GUI
The graphical user interface to change the values of simulation is:

<img src="AttachmentsREADME/GUI.png" alt="GUI" width="800"/>

### Where:
#### 1st row of GUI:
- $N_{LRS}$: Resistive state ($N_S$) at Low Resistive State (LRS).
- $N_{HRS}$: $N_S$ at High Resistive State (HRS).
- $N_{FS}$: $N_S$ at Fresh State (FS).
- $V_{FORMING}$: voltage needed for the FORMING.
- $V_{RESET}$: voltage that achieve the RESET.
- $V_{SET}$: voltage where the SET occurs.
- $K_{HRS}$: Enhancement factor for HRS.
- $K_{LRS}$: Enhancement factor for LRS.
#### 2nd row of GUI:
- ${\gamma}_{SET}$: Enhancement coefficient of generation probability during SET and FORMING.
- ${\gamma}_{RESET}$: Enhancement coefficient of generation probability during RESET.
- $\varphi_{drift}$: Enhancement coefficient for the drift of $\mathrm{O_{ion}}$.









