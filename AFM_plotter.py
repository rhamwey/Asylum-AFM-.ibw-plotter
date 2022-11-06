# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:36:05 2022

@author: raham
"""
# define project path
import sys
sys.path.append(r"C:\Users\raham\Google Drive\work\Lab\Scripts\AFM\AFM reader")
# import parse_n_plot
import parse_n_plot as pnp

#%% plot AFMs in a folder
folder = r"C:\Users\raham\Google Drive\work\Lab\AFM\221031"

pnp.folder_parser(folder)

#%% plot an indivudal scan with custom colorbar limits
measurement_path = r"C:\Users\raham\Google Drive\work\Lab\AFM\220527\RH220526IA_45_20000.ibw"

ht_lim = 20
amp_lim = -20
custom_lim = [ht_lim,amp_lim]

pnp.plot(measurement_path,custom_lim)

