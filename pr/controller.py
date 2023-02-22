import numpy as np

class ZustandsRegler:
    def __init__(self, k, T, outMin, outMax, sampleTime):
        self.k = k
        self.T = T
        self.T_inv = np.linalg.inv(T)
        self.outMin = outMin
        self.outMax = outMax

    def run(self, setPoint, curValue):
        # setPoint und curValue sind in linearisierten Koordinaten
        # setPoint = self.T_inv.dot(setPoint)
        e = setPoint - curValue

        out = self.k.dot(self.T).dot(e)

        if out < self.outMin:
            out = self.outMin
        elif out > self.outMax:
            out = self.outMax

        return out