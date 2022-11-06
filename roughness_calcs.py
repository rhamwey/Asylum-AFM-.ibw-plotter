# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:26:29 2022

@author: raham
"""

import numpy as np


# roughness calculation functions #############################################
def ra_calc(data): # absolute difference rougness
    average = data.mean()
    normalized = abs(data - average)
    ra = normalized.mean()
    
    return ra

def rq_calc(data): # RMS roughness !!!! THIS IS WHAT IS USED BY ASYLUM !!!!
    
    
    average = data.mean()
    normalized = data - average
    squared = normalized**2
    
    num_points = len(data)**2
    
    rq = ((np.sum([squared]))/num_points)**0.5
    
    return rq

# def bin(Height_Amp,bin_no,R_Max,R_Min,G_Max,G_Min,B_Max,B_Min):
def stats(data):

        # flatten into array
        data = data.flatten()
        
        #find std dev
        sigma = np.std(data)
        
        #range
        Range = (max(data)-min(data))
        
            
        return sigma, Range   