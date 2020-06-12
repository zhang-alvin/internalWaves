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


wind_Amp=5.0
wind_N=2.0
wind_omega = 2.0
T_length = 2
#tank.BC['y+'].u_dirichlet.uOfXT = lambda x,t, n=np.zeros(3,):  wind_Amp*np.sin(np.pi*wind_N*x[0]/tank_length)*np.sin(2.0*np.pi*wind_omega/t_length*t)


def getDBC_p(x,flag):
    if flag == boundaryTags['top']:# or x[1] >= L[1] - 1.0e-12:
        return lambda x,t: 0.0
    
def getDBC_u(x,flag):
    #return None
    if flag == boundaryTags['top']:# or x[1] >= L[1] - 1.0e-12:
        return lambda x,t: wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.sin(2.0*np.pi*wind_omega/T_length*t)
        #return lambda x,t: wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.sin(2.0*np.pi*wind_omega/T*t)
    if flag in [boundaryTags['bottom'],boundaryTags['left'],boundaryTags['right']]:# or x[1] >= l[1] - 1.0e-12:
        return lambda x,t: 0.0 #reynold's number of 10


def v_profile(x,t):
    k = np.pi*wind_N/L[0]
    A = k*L[1]*wind_Amp
    return A*np.sin(np.pi*wind_N*x[0]/L[0])*np.cos(2.0*np.pi*wind_omega/T_length*t)

def getDBC_v(x,flag):
    if flag == boundaryTags['top']:
        return lambda x,t: v_profile(x,t)#wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.cos(2.0*np.pi*wind_omega/T*t)
    #if flag == boundaryTags['bottom']:# or x[1] >= l[1] - 1.0e-12:
    if flag in [boundaryTags['bottom'],boundaryTags['left'],boundaryTags['right']]:# or x[1] >= l[1] - 1.0e-12:
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
    return None
    #if flag != boundaryTags['top'] or flag != boundaryTags['bottom'] :# or x[1] < L[1] - 1.0e-12:
    #    return lambda x,t: 0.0

def getAFBC_v(x,flag):
    return None
    #if flag != boundaryTags['top'] or flag != boundaryTags['bottom']:# or x[1] < L[1] - 1.0e-12:
    #    return lambda x,t: 0.0

def getDFBC_u(x,flag):
    return None
    #if flag == boundaryTags['top'] or flag == boundaryTags['bottom']:# or x[1] < L[1] - 1.0e-12:
    #    return None
    #else:
    #    return lambda x,t: 0.0
    
def getDFBC_v(x,flag):
    return None
    #if flag == boundaryTags['top'] or flag == boundaryTags['bottom']:# or x[1] < L[1] - 1.0e-12:
    #    return None
    #else:
    #    return lambda x,t: 0.0

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
            return -(L[1] - self.waterLevel)*rho_1*g[1] - (self.waterLevel - x[1])*rho_0*g[1]
        else:
            return -(L[1] - self.waterLevel)*rho_1*g[1]

class AtRest:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return 0.0

class InitialU:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return wind_Amp*np.sin(np.pi*wind_N*x[0]/L[0])*np.sin(2.0*np.pi*wind_omega/T_length*t)

class InitialV:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return 0.0
        #return wind_Amp*np.sinh(wind_N*x[) np.sin(np.pi*wind_N*x[0]/L[0])*np.cos(2.0*np.pi*wind_omega/T*t)


initialConditions = {0:PerturbedSurface_p(waterLine_z),
                     1:AtRest(),
                     2:AtRest()}
