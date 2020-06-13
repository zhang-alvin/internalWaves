from proteus import *
from proteus.default_p import *
from dambreak import *
from proteus.mprans import RANS2P
from proteus import Context
ct = Context.get()

#parallelPeriodic=True

LevelModelType = RANS2P.LevelModel
if useOnlyVF:
    LS_model = None
else:
    LS_model = 2
if useRANS >= 1:
    Closure_0_model = 5; Closure_1_model=6
    if useOnlyVF:
        Closure_0_model=2; Closure_1_model=3
    if movingDomain:
        Closure_0_model += 1; Closure_1_model += 1
else:
    Closure_0_model = None
    Closure_1_model = None

coefficients = RANS2P.Coefficients(epsFact=epsFact_viscosity,
                                   sigma=0.0,
                                   rho_0 = rho_0,
                                   nu_0 = nu_0,
                                   rho_1 = rho_1,
                                   nu_1 = nu_1,
                                   g=g,
                                   nd=nd,
                                   VF_model=1,
                                   LS_model=LS_model,
                                   Closure_0_model=Closure_0_model,
                                   Closure_1_model=Closure_1_model,
                                   epsFact_density=epsFact_density,
                                   stokes=False,
                                   useVF=useVF,
                                   useRBLES=useRBLES,
                                   useMetrics=useMetrics,
                                   eb_adjoint_sigma=1.0,
                                   eb_penalty_constant=weak_bc_penalty_constant,
                                   forceStrongDirichlet=ns_forceStrongDirichlet,
                                   turbulenceClosureModel=ns_closure,
                                   movingDomain=movingDomain)


wind_Amp=0.1
wavelength = L[0]#*2.0
wave_num = 2.0*np.pi/wavelength
wave_freq = np.sqrt(-g[1]*wave_num*np.tanh(wave_num*L[1]))
#5.31655337432 
gravity = -g[1]
trueH = L[1]*2.0


def getDBC_p(x,flag):
    if flag == boundaryTags['top']:# or x[1] >= L[1] - 1.0e-12:
        #return lambda x,t: 0.0
        return lambda x,t: rho_1*gravity*(trueH-L[1])+ 2*rho_1*(gravity)*wind_Amp*np.cosh(wave_num*L[1])/np.cosh(wave_num*trueH)*np.sin(wave_num*x[0])*np.sin(wave_freq*t)
    
def getDBC_u(x,flag):
    #return None
    if flag == boundaryTags['top']:# or x[1] >= L[1] - 1.0e-12:
        return lambda x,t: wind_Amp*2*wave_freq*np.cosh(wave_num*L[1])/np.sinh(wave_num*trueH)*np.sin(wave_num*x[0])*np.sin(wave_freq*t)
        #return lambda x,t: wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.sin(2.0*np.pi*wind_omega/T*t)
    if flag in [boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:# or x[1] >= l[1] - 1.0e-12:
        return lambda x,t: 0.0 #reynold's number of 10


def v_profile(x,t):
    #k = np.pi*wind_N/L[0]
    #A = k*L[1]*wind_Amp
    return 2*wave_freq*wind_Amp*np.sinh(wave_num*L[1])/np.sinh(wave_num*trueH)*np.sin(wave_num*x[0])*np.cos(wave_freq*t)

def getDBC_v(x,flag):
    if flag == boundaryTags['top']:
        return lambda x,t: v_profile(x,t)#wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.cos(2.0*np.pi*wind_omega/T*t)
    #if flag == boundaryTags['bottom']:# or x[1] >= l[1] - 1.0e-12:
    if flag in [boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:# or x[1] >= l[1] - 1.0e-12:
        return lambda x,t: 0.0 #reynold's number of 10

dirichletConditions = {0:getDBC_p,
                       1:getDBC_u,
                       2:getDBC_v}

#periodicDirichletConditions = {0:ct.getPDBC,
#                               1:ct.getPDBC,
#                               2:ct.getPDBC}

def getAFBC_p(x,flag):
    if flag == boundaryTags['top']:# or x[1] < L[1] - 1.0e-12:
        return lambda x,t: v_profile(x,t)
    else:
        return lambda x,t: 0.0

def getAFBC_u(x,flag):
    if flag not in [boundaryTags['top'],boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:
        return lambda x,t: 0.0

def getAFBC_v(x,flag):
    if flag not in [boundaryTags['top'],boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:
        return lambda x,t: 0.0

def getDFBC_u(x,flag):
    if flag not in [boundaryTags['top'],boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:
        return lambda x,t: 0.0

def getDFBC_v(x,flag):
    if flag not in [boundaryTags['top'],boundaryTags['left'],boundaryTags['bottom'],boundaryTags['right']]:
        return lambda x,t: 0.0

advectiveFluxBoundaryConditions =  {0:getAFBC_p,
                                    1:getAFBC_u,
                                    2:getAFBC_v}

diffusiveFluxBoundaryConditions = {0:{},
                                   1:{1:getDFBC_u},
                                   2:{2:getDFBC_v}}

class PerturbedSurface_p:
    def __init__(self,waterLevel):
        self.waterLevel=waterLevel
    def uOfXT(self,x,t):
        if signedDistance(x) < 0:
            #return rho_1*gravity*(trueH-self.waterLevel)+rho_0*gravity*(self.waterLevel-x[1])+2*rho_0*(gravity)*wind_Amp*np.cosh(wave_num*x[1])/np.cosh(wave_num*self.waterLevel)*np.sin(wave_num*x[0])*np.sin(wave_num*t)
            return rho_1*gravity*(trueH-self.waterLevel)+rho_0*gravity*(self.waterLevel-x[1])+2*rho_0*(gravity)*wind_Amp*np.cosh(wave_num*x[1])/np.cosh(wave_num*trueH)*np.sin(wave_num*x[0])*np.sin(wave_freq*t)
        else:
            return rho_1*gravity*(trueH-x[1])+2*rho_1*(gravity)*wind_Amp*np.cosh(wave_num*x[1])/np.cosh(wave_num*trueH)*np.sin(wave_num*x[0])*np.sin(wave_freq*t)

class AtRest:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return 0.0

class InitialU:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return wind_Amp*2*wave_freq*np.cosh(wave_num*x[1])/np.sinh(wave_num*trueH)*np.sin(wave_num*x[0])*np.sin(wave_freq*t)

class InitialV:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return 2*wave_freq*wind_Amp*np.sinh(wave_num*x[1])/np.sinh(wave_num*trueH)*np.sin(wave_num*x[0])*np.cos(wave_freq*t)
        #return wind_Amp*np.sinh(wind_N*x[) np.sin(np.pi*wind_N*x[0]/L[0])*np.cos(2.0*np.pi*wind_omega/T*t)


initialConditions = {0:PerturbedSurface_p(waterLine_z),
                     1:InitialU(),
                     2:InitialV()}
