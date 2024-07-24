import numpy as np

def calculate(list):
    if(len(list)<9 | len(list)>9):
       raise ValueError("List must contain nine numbers.")   
    
    list_to_numpy = np.array(list).reshape((3,3))

    calculations = {}
    calculations['mean'] = [np.mean(list_to_numpy, axis = 0), np.mean(list_to_numpy, axis =1), np.mean(list_to_numpy.flatten())]
    calculations['variance'] = [np.var(list_to_numpy, axis = 0), np.var(list_to_numpy, axis = 1), np.var(list_to_numpy.flatten())]
    calculations['standard deviation'] = [np.std(list_to_numpy, axis = 0), np.std(list_to_numpy, axis = 1), np.std(list_to_numpy.flatten())]
    calculations['max'] = [np.max(list_to_numpy, axis = 0), np.max(list_to_numpy, axis = 1), np.max(list_to_numpy.flatten())]
    calculations['min'] = [np.min(list_to_numpy, axis = 0), np.min(list_to_numpy, axis = 1), np.min(list_to_numpy.flatten())]
    calculations['sum'] = [np.sum(list_to_numpy, axis = 0), np.sum(list_to_numpy, axis = 1), np.sum(list_to_numpy.flatten())]

    return calculations

print(calculate([9,1,5,3,3,3,2,9,0]))