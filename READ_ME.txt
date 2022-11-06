USE AFM_plotter.py TO PLOT AFMs!!! All other files are function files that must 
be imported



#### define project path ###
First block must be run to import functions from the other files. Path of these
files must be specified in line 9, e.g. "C:\Users\raham\Google Drive\work\Lab\Scripts\AFM\AFM reader"

### plot AFMs in a folder ###
"folder" is the specified directory which includes all the .ibw AFM files to be plotted. 
Height and amplitude scans will be saved in this directory following .ibw file name
These scans use an auto z-bar scaling function similar to mud. RMS roughness is also
shown.

### plot an indivudal scan with custom colorbar limits ###
If unhappy with colorbar scaling (height or amplitude) for a specific .ibw file,
custom values can be inputted as ht_lim (height) or amp_lim (amplitude). 
.ibw in of interest must be specified as the measurement_path.
