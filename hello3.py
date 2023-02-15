#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import statistics

#PLOT SETUP FOR 1st PART OF LAB 03
V = np.array( [4.294, 6.83, 8.4, 9.38, 
               10.01, 10.43, 10.71, 10.89, 
               10.97, 11.05, 11.11, 11.16 ] ) # fill in the array

t = np.array( [10.29, 20.19, 30.31, 40.03,  
               49.93, 60.09, 70.21, 80.34, 
               90.41, 100, 110, 120 ] )

plt.title("Lab 03, Part 01: Capacitor Build-up")
plt.xlabel("Time: 10 second intervals")
plt.ylabel("Voltage: Coulombs per Meter")
plt.plot(t , V )

print("AVG: " + str(statistics.mean(V) ) + "\nSTD_DEV: " + str( statistics.stdev(V) ) )



# you can change the color and shape of the points
# don ’t forget to put a title and x and y axes labels on it as well .
# r e f e r e n c e our normal p l o t t i n g code for help , or the web


# In[9]:


#PLOT SETUP FOR 2nd PART OF LAB 03
V = np.array( [7.16, 4.523, 2.875, 1.834,
              1.174, 0.755, 0.488, 0.322,
              0.260, 0.222, 0.190, 0.177] ) # fill in the array

t = np.array( [10.19, 20.09, 30.14, 40.25,  
               50.13, 60.11, 70.21, 80.19,
               90.22, 100.14, 110.00, 120.07] )

plt.title("Lab 03, Part 02: Capacitor losing charge")
plt.xlabel("Time: 10 second intervals")
plt.ylabel("Voltage: Coulombs per Meter")
plt.plot(t , V )
print("AVG: " + str(statistics.mean(V) ) + "\nSTD_DEV: " + str( statistics.stdev(V) ) )

