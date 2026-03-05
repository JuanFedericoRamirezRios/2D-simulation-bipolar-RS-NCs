<img src="AttachmentsREADME/k61.gif" alt="k61-GIF" width="600"/>
<img src="AttachmentsREADME/k63.gif" alt="k61-GIF" width="600"/>

##### Compile: pyinstaller --onefile --add-binary "CalcsCpp.dll;." 2D_RRAM_NCs_DCmode.py

# 2D-simulation-bipolar-RS-NCs
2D simulation of Resistive switching memory of oxides with conductive-nanocrystals embedded. The simulation emulates the DC voltage stimulus (voltage sweep). If you use this software, cite: https://doi.org/10.3390/nano13142124.

## The simulation model
The simulation model is explained in [2D-simulation-model](https://doi.org/10.3390/nano13142124) and the electrical current calculation, equations (8) and (9) was modified to best adjust to experiment results by:

$$
J_{HRS}=K_{HRS}f_{HRS}\left[\left|F^H\right|\exp{\left(\frac{\beta\sqrt{\left|F^H\right|}-q\phi_t}{kT_r}\right)}\right] \text{\quad\quad(8)}
$$

$$
J_{LRS}=K_{LRS}\frac{f_{LRS}}{N_S-N_{FS}}\left[\frac{\left(F^H\right)^2}{L}\exp{\left(\frac{0.891\beta\sqrt{\left|F^H\right|}-q\phi_t}{kT_J}\right)}\right] \text{\quad\quad(9)} 
$$

## GUI
The graphical user interface to change the values of simulation is:

<img src="AttachmentsREADME/GUI.png" alt="GUI" width="800"/>

### Where:
#### 1st row of GUI:
- $N_{LRS}$: Conductive state ($N_S$), *NOT CONDUCTIVITY*, at Low Resistive State (LRS).
- $N_{HRS}$: $N_S$ at High Resistive State (HRS).
- $N_{FS}$: $N_S$ at Fresh State (FS).
- $V_{FORMING}$: Voltage needed for the FORMING.
- $V_{RESET}$: Voltage that achieve the RESET.
- $V_{SET}$: Voltage where the SET occurs.
- $K_{HRS}$: Enhancement factor for HRS.
- $K_{LRS}$: Enhancement factor for LRS.
#### 2nd row of GUI:
- $\gamma_{SET}$: Enhancement coefficient of generation probability during SET and FORMING.
- $\gamma_{RESET}$: Enhancement coefficient of generation probability during RESET.
- $\varphi_{drift}$: Enhancement coefficient for the drift of $O_{ion}$.
- $I_{compliance}$ during the FORMING process.
- $I_{compliance}$ during the RESET process.
- $I_{compliance}$ during the SET process.
- $a$: Mesh size.
- $A$: Device area.
#### 3rd row of GUI:
- $V_{Oinit}$: Initial number of oxygen vacancies ($V_O$).
- $t_{init}$: Time to generate or recombine $V_O$.
- $E_{Oe}$: Migration barrier for oxygen ion ($O_{ion}$) from equilibrium.
- $E_{Om}$: Migration barrier for $O_{ion}$ during their migration.
- $L_O$: Decaying length of the $O_{ion}$ concentration.
- $\beta_R$: Coefficient for the recombination.
- $Rth$: Thermal resistance of (conductive filaments) CFs.
- $a_0$: Attenuation length of the electron wave function.
#### 4th row of GUI:
- Number of sweep cycles ($0 V \to (V_{FORMING}\text{ or }V_{SET}) \to 0 V \to V_{RESET} \to 0 V$).
- $\varepsilon$: Relative electrical permittivity.
- $\phi_t$: Potential of the trap levels for charge conductivity.

- Experiment: Name of OPTIONAL plain text file with the experimental $I-V$ results to compare with $I-V$ simulated. The format must be:

&emsp;1st line: V (V)`tab`I (A)

&emsp;2nd line: 1st voltage`tab`1st current

&emsp;3rd line: 2nd voltage`tab`2nd current

&emsp; &emsp; &emsp; &emsp; &emsp; ...

- Structure: Name of plain text file with nanocrystals configuration. With:

&emsp;0 → Not $V_O$.

&emsp;1 → $V_O$.

&emsp;2 → Fixed $V_O$, these are the nanocrystals.

Examples in the files: [K-61-RT.txt](K-61-RT.txt) and [K-63-RT-shift.txt](K-63-RT-shift.txt).
I recommend using the graphical editor of plain text online: https://asciiflow.com/
- Out file: Name of out data simulation results (**WARNING**: If it exists, this will be remplaced).
- Seed: Seed of the random number generator. It is ranlux24 engine.
- SIMULATE button: Simulate the cycles and show the simulation results of $N_S-V$ and $I-V$, if the *Experiment* file exists, it is include in the $I-V$ graph. It action creates the folder *configurations* (**WARNING**: If it exists, this will be remplaced) with the plain text files of each $V_O$ configuration during the simulation. Additional, it generates the *Out file* with the results of simulation.
- DRAW LAST SIMULATION button: By the $V_O$ configurations in *configurations* folder and *Out file* data, it generates .png images of simulation results in the folder *confsPng* (**WARNING**: If it exists, this will be remplaced).

By [GenerateGIF.exe](GenerateGIF.exe) you can create a .gif after "DRAW LAST SIMULATION" button. Usage of GenerateGIF.exe in my repository: https://github.com/JuanFedericoRamirezRios/Generator-GIF








