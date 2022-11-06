# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from igor import binarywave
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from colorbar import mud_cmap

import roughness_calcs as rough
#%%
def get_data(path):
    # raw data ###################################################################
    load = binarywave.load(path) # load the .ibw file
    wave = load['wave'] # isolate wave data 
    data = wave['wData']
    
    # data into height and amplitude #############################################
    Height = np.rot90(data[:,:,0]) * 10**9 #in nm
    Amplitude = np.rot90(data[:,:,1]) * 10**9  #in nm
    
    return Height, Amplitude, wave
#%%
def limits(Height, Amplitude): # colorbar limits
    # height stats ########################################################
    ra_ht = rough.ra_calc(Height)
    rq_ht = rough.rq_calc(Height) 
    sigma_ht,Range_ht = rough.stats(Height)
    
    prod_ht = sigma_ht*Range_ht
    map_lim_ht = 0.0189*prod_ht + 3.43
    
    # amp stats ########################################################

    ra_am = rough.ra_calc(Amplitude)
    rq_am = rough.rq_calc(Amplitude) 
    sigma_am,Range_am = rough.stats(Amplitude)
    
    prod_am = sigma_am*Range_am
    map_lim_am = 0.124*prod_am + 0.3489
     
    limits = {"height":map_lim_ht, "amplitude":map_lim_am}
    return limits
#%%
def heatmap(Height,Amplitude, wave, path,custom_lim = None):
    # Get Measurement Name #######################################################
    Measurement = path.split('\\')[-1]
    
    # get colorbar limits #########################################################
    if custom_lim == None:
        lims = limits(Height, Amplitude)
    elif type(custom_lim) == list:
        lims = {"height":custom_lim[0], "amplitude":custom_lim[1]}
    else:
        raise Exception("enter limits as list: {height_lim, amplitude_lim]")        
        
    # determine scan scale #######################################################
    num_points = wave['wave_header']['nDim'][0]
    spacing_dim = wave['wave_header']['sfA'][0]*10**6 # each points spacing in um
    xy_lim = (num_points-1)*spacing_dim # the total xy_lim in um
    
    #tick labels #################################################################
    ticks = np.linspace(0,num_points-1,5)
    ticks_strx = [str('{:,.2f}'.format(x*spacing_dim)) for x in ticks]
    ticks_stry = ticks_strx.copy()
    
    # create subplot ##############################################################
    fig, axes = plt.subplots(1, 2,figsize=(14,6))
    fig.tight_layout(pad=5.0)
    fig.suptitle(Measurement.split('.')[0] + ", Height Roughness: " + "{:.3f}".format(rough.rq_calc(Height)) + " nm"
                 ,fontsize = '20')
    
    # plot height heatmap #########################################################
    sns.heatmap(data = Height, 
                cmap= mud_cmap(),
                cbar_kws={'label': 'Z height (nm)'},
                ax=axes[0], vmin = -lims["height"], vmax = lims["height"])
    
    cax = plt.gcf().axes[-1]
    cax.tick_params(labelsize=16)
    cax.set_ylabel(cax.get_ylabel(), fontsize = 18)

    axes[0].set_xticks(ticks)
    axes[0].set_yticks(np.flip(ticks))
    axes[0].set_xticklabels(ticks_strx, fontsize = 16)
    axes[0].set_yticklabels(ticks_stry, fontsize = 16)
    axes[0].set_xlabel('um',fontsize='18')
    axes[0].set_ylabel('um',fontsize='18')
    axes[0].set_title('Height',fontsize='18')
    
    # plot amplitude heatmap #########################################################
    sns.heatmap(Amplitude, 
                cmap=mud_cmap(),
                cbar_kws={'label': 'Z height (nm)'},
                ax=axes[1], vmin = -lims["amplitude"], vmax = lims["amplitude"])
    
    cax = plt.gcf().axes[-1]
    cax.tick_params(labelsize=16)
    cax.set_ylabel(cax.get_ylabel(), fontsize = 18)
    
    axes[1].set_xticks(ticks)
    axes[1].set_yticks(np.flip(ticks))
    axes[1].set_xticklabels(ticks_strx, fontsize = 16)
    axes[1].set_yticklabels(ticks_stry, fontsize = 16)
    axes[1].set_xlabel('um',fontsize='18')
    axes[1].set_ylabel('um',fontsize='18')
    axes[1].set_title('Amplitude',fontsize='18')
    
    
    # save figure ########################################################################     
    plt.tight_layout()
    fig.savefig(path.split('.')[0])


    # show figure ########################################################################
    plt.figure()

#%% plot path

def plot(path, custom_lim = None): #*args is optional custom colorbar ranges
        
            Height, Amplitude, wave = get_data(path)
            heatmap(Height,Amplitude, wave, path, custom_lim)
        

    
#%%
def folder_parser(folder):
    folder_contents = os.listdir(folder)
    folder_contents = [x for x in folder_contents if  '.ibw' in x]

    for file_name in folder_contents:
        path = folder + '\\' + file_name # the path of the measurement
        plot(path)
    

    
    