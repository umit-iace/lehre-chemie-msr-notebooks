import numpy as np
from scipy.integrate import solve_ivp
from models import nonLinSys, linSys


def simu_nlin_noFF(regler, timeDom, z0, setPoint):
    zNLin = np.zeros((2, len(timeDom)))
    zNLin[:,0] = z0

    uNLin = np.zeros((len(timeDom),))
    
    for idx, _ in enumerate(timeDom[1:]):
        z0NLin = zNLin[:, idx]
        uNLin[idx] = regler.run(setPoint=setPoint, curValue=z0NLin) + 9 # maybe here buA

        resNLin = solve_ivp(nonLinSys,
                                [timeDom[idx], timeDom[idx + 1]],
                                z0NLin,
                                args=(uNLin[idx], ))
        zNLin[:, idx + 1] = resNLin.y.T[-1, :]
    
    return zNLin, uNLin


def simu_lin_noFF(regler, timeDom, z0, setPoint, A, B):
    zLin = np.zeros((2, len(timeDom)))
    zLin[:, 0] = z0
    
    uLin = np.zeros((len(timeDom),))
                    
    for idx, _ in enumerate(timeDom[1:]):
        z0PhyLin = zLin[:, idx]
        uLin[idx] = regler.run(setPoint=setPoint, 
                                curValue=z0PhyLin) + 9

        resLin = solve_ivp(linSys,
                            [timeDom[idx], timeDom[idx + 1]],
                            z0PhyLin,
                            args=(uLin[idx], A, B, 9))
        zLin[:, idx + 1] = resLin.y.T[-1, :]
    
    return zLin, uLin


def simu_nlin_withFF(regler, FF, timeDom, z0, bz2):
    zNLin = np.zeros((2, len(timeDom)))
    zNLin[:,0] = z0
    
    uNLin = np.zeros((len(timeDom),))

    uFFNLin = np.zeros(len(timeDom))
    z2FFNLin = np.zeros(len(timeDom))
    
    for idx, t in enumerate(timeDom[1:]):
        z0NLin = zNLin[:, idx]

        z2FFNLin[idx], dz2FFNLin, uFFNLin[idx] = FF.run(t)

        # der Regler arbeitet in linearen Koordinaten, weshalb man hier die Ruhelage abziehen muss
        uRegler = regler.run(setPoint=np.array([z2FFNLin[idx], dz2FFNLin]), 
                                curValue=np.array([z0NLin[0] - bz2, z0NLin[1]]))
        
        uNLin[idx] = uRegler + uFFNLin[idx] + 9 # maybe here buA

        resNLin = solve_ivp(nonLinSys,
                            [timeDom[idx], timeDom[idx + 1]],
                            z0NLin,
                            args=(uNLin[idx], ))
        zNLin[:, idx + 1] = resNLin.y.T[-1, :]
    
    return zNLin, z2FFNLin, uNLin


def simu_lin_withFF(regler, FF, timeDom, z0, A, B):
    zLin = np.zeros((2, len(timeDom)))
    zLin[:,0] = z0
    
    uLin = np.zeros((len(timeDom),))

    uFFLin = np.zeros(len(timeDom))
    z2FFLin = np.zeros(len(timeDom))
    
    for idx, t in enumerate(timeDom[1:]):
        z0Lin = zLin[:, idx]

        z2FFLin[idx], dz2FFLin, uFFLin[idx] = FF.run(t)

        uRegler = regler.run(setPoint=np.array([z2FFLin[idx], dz2FFLin]), 
                                curValue=z0Lin)
        
        uLin[idx] = uRegler + uFFLin[idx] + 9 # maybe here buA

        resLin = solve_ivp(linSys,
                            [timeDom[idx], timeDom[idx + 1]],
                            z0Lin,
                            args=(uLin[idx], A, B, 9))
        zLin[:, idx + 1] = resLin.y.T[-1, :]
    
    return zLin, z2FFLin, uLin