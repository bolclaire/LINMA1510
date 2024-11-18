import numpy as np

# Third laboratory : control of a three - tank system

# The system is linearized around an equilibrium point that we have to find experimentally
# Legend : a is a function (will vary), a_ is an equilibrium point (arbitrarily chosen or found experimentally)

# Here are the system values
u1_ = 60        # mL/s   # water flow pump 1 to tank 3
u2_ = 60        # mL/s   # water flow pump 2 to tank 1

Sf  = 16*1e-2   # cm^2   # section of the front valves
v1_ = Sf        # cm^2   # tank 1 front valve section
v2_ = Sf        # cm^2   # tank 2 front valve section
v3_ = Sf        # cm^2   # tank 3 front valve section 

So  = 16*1e-2   # cm^2   # section of the outgoing tube
Si  = 16*1e-2   # cm^2   # section of the intermediates tubes
St  = 43        # cm^2   # section of the tanks
g   = 9.81*1e2  # cm/s^2  # gravitational constant

# Report here the equilibrium values (found at C.2.1)
x1_ = 10       # cm     # water level tank1
x2_ = 20       # cm     # water level tank2
x3_ = 20       # cm     # water level tank3

# Linearized system matrices
A = np.array( [[ -((Si+v1_)/St)*np.sqrt(g/(2*x1_)) , (Si/St)*np.sqrt(g/(2*x2_))          , 0                                    ],
               [ (Si/St)*np.sqrt(g/(2*x2_))        , -((v2_+2*Si)/St)*np.sqrt(g/(2*x2_)) , (Si/St)*np.sqrt(g/(2*x3_))           ],
               [ 0                                 , (Si/St)*np.sqrt(g/(2*x2_))          , -((Si+So+v3_)/St)*np.sqrt(g/(2*x3_)) ]] )

B = np.array( [[ 0   , 1/St ],
               [ 0   , 0    ],
               [ 1/St, 0    ]] )

D = np.array( [[ (-1/St)*np.sqrt(2*g*x1_) , 0                        , 0                        ],
               [ 0                        , (-1/St)*np.sqrt(2*g*x2_) , 0                        ],
               [ 0                        , 0                        , (-1/St)*np.sqrt(2*g*x3_) ]] )

# Model intern stability
A_eigenvals, A_eigenvects = np.linalg.eig(A)
print(A_eigenvals)