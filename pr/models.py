import numpy as np


def nonLinSys(t, z, uA):
    z1 = z[0]
    z2 = z[1]

    if z1 < 0:
        z1 = 0

    if z2 < 0:
        z2 = 0
        
    hV1 = 0.055
    hV2 = 0.055
    
    dz = np.zeros(2)
    dz[0] = 0.00216625315586689 * (uA - 6.4) - 0.0127646468529449 * np.sqrt(2) * np.sqrt(hV1 + z1)
    dz[1] = 0.0127646468529449 * np.sqrt(2) * np.sqrt(hV1 + z1) - 0.00908683019582126 * np.sqrt(2) * np.sqrt(hV2 + z2)

    return dz

def linSys(t, x, uA, A, B, buA):
    x1 = x[0]
    x2 = x[1]
    
    if x1 < 0:
        x1 = 0

    if x2 < 0:
        x2 = 0
    
    return A.dot(x) + B.dot(np.array([uA - buA]))