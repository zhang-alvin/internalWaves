from math import *
import proteus.MeshTools
from proteus import Domain
from proteus.default_n import *   
from proteus.Profiling import logEvent
   
#  Discretization -- input options  
#Refinement = 20#45min on a single core for spaceOrder=1, useHex=False
Refinement = 20#45min on a single core for spaceOrder=1, useHex=False
genMesh=True
movingDomain=False
applyRedistancing=True
useOldPETSc=False
useSuperlu=False#True
timeDiscretization='be'#'vbdf'#'be','flcbdf'
#timeDiscretization='vbdf'#'be','flcbdf'
spaceOrder = 1
useHex     = False
useRBLES   = 0.0
useMetrics = 1.0
applyCorrection=True
useVF = 1.0
useOnlyVF = False
useRANS = 0 # 0 -- None
            # 1 -- K-Epsilon
            # 2 -- K-Omega
    
#  Discretization   
nd = 2
if spaceOrder == 1:
    hFactor=1.0
    if useHex:
        basis=C0_AffineLinearOnCubeWithNodalBasis
        elementQuadrature = CubeGaussQuadrature(nd,2)
        elementBoundaryQuadrature = CubeGaussQuadrature(nd-1,2)     	 
    else:
        basis=C0_AffineLinearOnSimplexWithNodalBasis
        elementQuadrature = SimplexGaussQuadrature(nd,3)
        elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,3) 	    
    
# Domain and mesh
#L = (0.584,0.350)
#L = (1.0,0.5)
L = (1.0,0.5)
#L = (4.0,1.0)
he = L[0]/float(4*Refinement-1)
#he*=0.5
#he*=0.5
#he*=0.5
#he*=0.5
weak_bc_penalty_constant = 100.0
nLevels = 1
parallelPartitioningType = proteus.MeshTools.MeshParallelPartitioningTypes.element
#parallelPartitioningType = proteus.MeshTools.MeshParallelPartitioningTypes.node
nLayersOfOverlapForParallel = 0


structured=False
boundaries=['bottom','right','top','left']
boundaryTags=dict([(key,i+1) for (i,key) in enumerate(boundaries)])
if useHex:   
    nnx=4*Refinement+1
    nny=4*Refinement+1
    #hex=True    
    quad=True
    domain = Domain.RectangularDomain(L)
else:
    #boundaries=['left','right','bottom','top','front','back']
    if structured:
        nnx=4*Refinement
        nny=4*Refinement
        Domain.RectangularDomain(L)
        triangleFlag=1
    else:
        vertices=[[0.0,0.0],#0
                  [L[0],0.0],#1
                  [L[0],L[1]],#2
                  [0.0,L[1]],#3
                 ]#7
        vertexFlags=[boundaryTags['bottom'],
                     boundaryTags['bottom'],
                     boundaryTags['top'],
                     boundaryTags['top'],
                     ]
        segments=[[0,1],
                  [1,2],
                  [2,3],
                  [3,0],
                ]
        segmentFlags=[boundaryTags['bottom'],
                      boundaryTags['right'],
                      boundaryTags['top'],
                      boundaryTags['left'],
                     ]
        regions=[[0.5*L[0],0.5*L[1]]]
        regionFlags=[1]
        holes=[]
        domain = Domain.PlanarStraightLineGraphDomain(vertices=vertices,
                                                      vertexFlags=vertexFlags,
                                                      segments=segments,
                                                      segmentFlags=segmentFlags,
                                                      regions=regions,
                                                      regionFlags=regionFlags,
                                                      holes=holes)
        #go ahead and add a boundary tags member 
        domain.MeshOptions.setParallelPartitioningType('element')
        domain.boundaryTags = boundaryTags
        domain.writePoly("mesh")
        domain.writePLY("mesh")
        domain.writeAsymptote("mesh")
        triangleOptions="VApq30Dena%8.8f" % ((he**2)/2.0,)

#logEvent("""Mesh generated using: tetgen -%s %s"""  % (triangleOptions,domain.polyfile+".poly"))
# Time stepping
T=200.0
dt_fixed = 2.0#0.1
dt_init = min(0.1*dt_fixed,0.1*he)
runCFL=0.9
nDTout = int(round(T/dt_fixed))

# Numerical parameters
ns_forceStrongDirichlet = True
if useMetrics:
    ns_shockCapturingFactor  = 0.25
    ns_lag_shockCapturing = True
    ns_lag_subgridError = True
    ls_shockCapturingFactor  = 0.25
    ls_lag_shockCapturing = True
    ls_sc_uref  = 1.0
    ls_sc_beta  = 1.0
    vof_shockCapturingFactor = 0.25
    vof_lag_shockCapturing = True
    vof_sc_uref = 1.0
    vof_sc_beta = 1.0
    rd_shockCapturingFactor  = 0.25
    rd_lag_shockCapturing = False
    epsFact_density    = 3.0
    epsFact_viscosity  = epsFact_curvature  = epsFact_vof = epsFact_consrv_heaviside = epsFact_consrv_dirac = epsFact_density
    epsFact_redistance = 0.33
    epsFact_consrv_diffusion = 0.1
    redist_Newton = True
    kappa_shockCapturingFactor = 0.25
    kappa_lag_shockCapturing = True#False
    kappa_sc_uref = 1.0
    kappa_sc_beta = 1.0
    dissipation_shockCapturingFactor = 0.25
    dissipation_lag_shockCapturing = True#False
    dissipation_sc_uref = 1.0
    dissipation_sc_beta = 1.0
else:
    ns_shockCapturingFactor  = 0.9
    ns_lag_shockCapturing = True
    ns_lag_subgridError = True
    ls_shockCapturingFactor  = 0.9
    ls_lag_shockCapturing = True
    ls_sc_uref  = 1.0
    ls_sc_beta  = 1.0
    vof_shockCapturingFactor = 0.9
    vof_lag_shockCapturing = True
    vof_sc_uref  = 1.0
    vof_sc_beta  = 1.0
    rd_shockCapturingFactor  = 0.9
    rd_lag_shockCapturing = False
    epsFact_density    = 1.5
    epsFact_viscosity  = epsFact_curvature  = epsFact_vof = epsFact_consrv_heaviside = epsFact_consrv_dirac = epsFact_density
    epsFact_redistance = 0.33
    epsFact_consrv_diffusion = 1.0
    redist_Newton = False
    kappa_shockCapturingFactor = 0.9
    kappa_lag_shockCapturing = True#False
    kappa_sc_uref  = 1.0
    kappa_sc_beta  = 1.0
    dissipation_shockCapturingFactor = 0.9
    dissipation_lag_shockCapturing = True#False
    dissipation_sc_uref  = 1.0
    dissipation_sc_beta  = 1.0

ns_nl_atol_res = max(1.0e-8,0.001*he**2)
vof_nl_atol_res = max(1.0e-8,0.001*he**2)
ls_nl_atol_res = max(1.0e-8,0.001*he**2)
rd_nl_atol_res = max(1.0e-8,0.005*he)
mcorr_nl_atol_res = max(1.0e-8,0.001*he**2)
kappa_nl_atol_res = max(1.0e-8,0.001*he**2)
dissipation_nl_atol_res = max(1.0e-8,0.001*he**2)

#turbulence
ns_closure=0 #1-classic smagorinsky, 2-dynamic smagorinsky, 3 -- k-epsilon, 4 -- k-omega
if useRANS == 1:
    ns_closure = 3
elif useRANS == 2:
    ns_closure == 4
# Water
rho_0 = 1045.0
nu_0  = 1.004e-6

# Air
rho_1 = 1025.0
nu_1  = nu_0#1.004e-6

# Surface tension
sigma_01 = 0.0

# Gravity
g = [0.0,-9.8]
#g = [0.0,0.0]

# Initial condition
waterLine_x = L[0]*2.0
waterLine_z = L[1]/4.0#0.292

def signedDistance(x):
    phi_x = x[0]-waterLine_x
    phi_z = x[1]-waterLine_z
    if phi_x < 0.0:
        if phi_z < 0.0:
            return max(phi_x,phi_z)
        else:
            return phi_z
    else:
        if phi_z < 0.0:
            return phi_x
        else:
            return sqrt(phi_x**2 + phi_z**2)

eps=1.0e-8
#def getPDBC(x,tag):
#    if x[0] < eps or x[0] > L[0] - eps:
#        return np.array([0.0,round(x[1],5),0.0])
