'''
You survey households in your area to find the average rent they are paying. Find the
standard deviation from the following data:
$1550, $1700, $900, $850, $1000, $950.
'''

try:
    #here in order to calculate standrd deviation we can calculate in two ways 
    
    from math import sqrt
    import numpy as np
    
    #Approach 1: Manually finding the standard deviation
    input_data= [1150,1700,850,1000,950]
    mean = sum(input_data)/len(input_data)
    variance = sum([(i-mean)**2 for i in input_data])/len(input_data)
    standrd_devitaion = sqrt(variance)
    print("Manually Calculating Standard Deviation: {}".format(standrd_devitaion))
    
    #Approach 2: Using library function
    std= np.std(input_data)
    print("Standard Deviation using Library Function : {}".format(std))
except Exception as e:
    print('Error Occured')