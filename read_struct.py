#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:05:36 2022

@author: jsears
"""
import numpy as np

# Helper function to read in an irrep from a saved text file
def read_struct(fname):  

    file = open(fname)
    
    # Make dictionaries for the r, u1 (cos), and u2 (sin) arrays for each mode/atom
    masterlist = []
    
    eof = 0
    found_dat=0
    r = []
    while not eof:
        line = file.readline()
        #print(len(line.split()))
    
        if not line:
            eof = 1
            r = np.asarray(r,dtype='float')
            masterlist.append([ [mode, atom], r ])
            break    
        
        
        # Check if this is a new mode
        if line[0:3]=='P4_':
            found_dat = 1
            if len(r)>0:
                r = np.asarray(r,dtype='float')
                masterlist.append([ [mode, atom], r ])
                r = []
    
            mode = line.replace(']',' ').split()[2]
    
    
        if found_dat:
            if len(line.split() )==7:
                r.append(line.split()[1:])
                atom = line.split()[0]

                
            if len(line.split() )==6:
                r.append(line.split()[:])
    
    
    file.close()
    return masterlist

