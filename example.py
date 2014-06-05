import numpy as np
from scipy import optimize
import sympy as sp 

# define some symbolic variables
C_0, C_1, K_0, K_1, L_0 = sp.var('C_0:2, K_0:2, L_0')

# define some symbolic parameters
alpha, beta_0, beta_1, sigma, L_bar = sp.var('alpha, beta_0, beta_1, sigma, L_bar')

# define some symbolic prices
r = sp.var('r')

# fixed labor supply
L_1 = L_bar - L_0

# some functions defining output in different sectors
Y_0 = K_0**beta_0 * L_0**(1 - beta_0)
Y_1 = K_1**beta_1 * L_1**(1 - beta_1)

# must eat everything you produce (less cost of capital)
C_0 = Y_0 - r * K_0
C_1 = Y_1 - r * K_1

# define the social planner's objective
rho = (sigma - 1) / sigma
U = (alpha * C_0**rho + (1 - alpha) * C_1**rho)**(1 / rho)

# compute first order conditions
foc_K_0 = sp.diff(U, K_0)
foc_K_1 = sp.diff(U, K_1)
foc_L_0 = sp.diff(U, L_0)

# compute the jacobian
sym_system_focs = sp.Matrix([foc_K_0, foc_K_1, foc_L_0])
sym_jacobian = sym_system_focs.jacobian([K_0, K_1, L_0])

# wrap the symbolic expressions as callable NumPy functions!
variables = (K_0, K_1, L_0)
params = (alpha, beta_0, beta_1, sigma, L_bar, r)
args = variables + params 

numeric_system = sp.lambdify(args, sym_system_focs, modules='numpy')
numeric_jacobian = sp.lambdify(args, sym_jacobian, modules='numpy')

def final_system(X, params):
    """Numeric system of FOCs."""
    # extract the vars
    K_0, K_1, L_0 = X

    # extract the parameters
    alpha = params['alpha']
    beta_0 = params['beta_0']
    beta_1 = params['beta_1']
    sigma = params['sigma']
    L_bar = params['L_bar']
    r = params['r']

    # don't forget to flatten the output array!
    tmp_out = numeric_system(K_0, K_1, L_0, alpha, beta_0, beta_1, sigma,
                             L_bar, r)
    final_out = np.array(tmp_out).flatten() 

    return final_out

def final_jacobian(X, params):
    """Numeric Jacobian of FOCs."""
    # extract the vars
    K_0, K_1, L_0 = X

    # extract the parameters
    alpha = params['alpha']
    beta_0 = params['beta_0']
    beta_1 = params['beta_1']
    sigma = params['sigma']
    L_bar = params['L_bar']
    r = params['r']

    tmp_out = numeric_jacobian(K_0, K_1, L_0, alpha, beta_0, beta_1, sigma,
                               L_bar, r)
    final_out = np.array(tmp_out) 
    
    return final_out

# specify some "sensible" parameter values
model_params = {'alpha':0.5, 'beta_0':0.33, 'beta_1':0.66, 'sigma':0.9, 
                'L_bar':1e3, 'r':1.0}

# solve the system of equations
initial_guess = np.array([1e2, 2e2, 5e2])
result = optimize.root(final_system, 
                       x0=initial_guess, 
                       args=(model_params,),
                       jac=final_jacobian,
                       method='hybr',
                       tol=1e-12,
                       )

