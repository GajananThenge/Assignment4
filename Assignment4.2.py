'''Problem Statement 1:
Find the variance for the following set of data representing trees in California (heights in
feet):
3, 21, 98, 203, 17, 9'''

try:
    #here in order to calculate Variance we can calculate in two ways 
    
    from math import sqrt
    import numpy as np
    
    #Approach 1: Manually finding the Variance
    input_data= [3, 21, 98, 203, 17, 9]
    mean = sum(input_data)/len(input_data)
    variance = sum([(i-mean)**2 for i in input_data])/len(input_data)
    print("Manually Calculating Variance: {}".format(variance))
    
    #Approach 2: Using library function
    varen= np.var(input_data)
    print("Variance using Library Function : {}".format(varen))
except Exception as e:
    print('Error Occured')