import sympy as sp

class Steuerung:
    def __init__(self, x0, x1, t0, t1, a0, a1, b):
        self.x0 = x0
        self.x1 = x1
        self.t0 = t0
        self.t1 = t1
        self.dt = t1 - t0
        self.a0 = a0
        self.a1 = a1
        self.b = b

        tau = sp.symbols('\\tau')
        self.phi = 6 * tau ** 5 - 15 * tau ** 4 + 10 * tau ** 3
        self.dphi = self.phi.diff(tau)
        self.ddphi = self.phi.diff(tau, 2)
        
        self.xr = lambda t: self.x0 + (self.x1 - self.x0) * self.phi.subs({tau: t / self.dt}) if 0 <= t <= self.dt else x0 if t < 0 else self.x1 
        self.dxr = lambda t: (self.x1 - self.x0) * self.dphi.subs({tau: t / self.dt}) / self.dt if 0 < t < self.dt else 0
        self.ddxr = lambda t: (self.x1 - self.x0) * self.ddphi.subs({tau: t / self.dt}) / self.dt ** 2 if 0 < t < self.dt else 0
        self.ur = lambda t: 1/ self.b * (self.ddxr(t) + self.a1 * self.dxr(t) + self.a0 * self.xr(t))

    def run(self, t):
        return self.xr(t), self.dxr(t), self.ur(t)   