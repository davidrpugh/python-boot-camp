import matplotlib.pyplot as plt
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

# solve for the optimal capital demand functions
optimal_K_0 = sp.solve(sp.diff(C_0, K_0), K_0)[0]
optimal_K_1 = sp.solve(sp.diff(C_1, K_1), K_1)[0]

# define the social planner's objective
rho = (sigma - 1) / sigma
tmp_U = (alpha * C_0**rho + (1 - alpha) * C_1**rho)**(1 / rho)

# substitute for K_0 and K_1 using demand functions
U = tmp_U.subs({'K_0':optimal_K_0, 'K_1':optimal_K_1})

# compute the first order condition
_symbolic_foc = sp.diff(U, L_0)

# compute the jacobian (this may take a few minutes!)
_symbolic_jacobian = sp.diff(_symbolic_foc, L_0)

# ...and the hessian (this may take a few more minutes!)
_symbolic_hessian = sp.diff(_symbolic_foc, L_0, 2)

# convert to numeric functions
args = (L_0, alpha, beta_0, beta_1, sigma, L_bar, r)
numeric_foc = sp.lambdify(args, _symbolic_foc, modules='numpy')
numeric_jacobian = sp.lambdify(args, _symbolic_jacobian, modules='numpy')
numeric_hessian = sp.lambdify(args, _symbolic_hessian, modules='numpy')

# params: alpha, beta_0, beta_1, sigma, L_bar, r
model_params = (0.5, 0.33, 0.66, 0.9, 1e3, 1.0)

# plot the first-order condition to see where the root lies...
plt.figure(figsize=(8,6))
grid = np.linspace(1e-3, 1e3 - 1e-3, 1e3)
plt.plot(grid, numeric_foc(grid, *model_params))
plt.axhline(0, linestyle='dashed')
plt.xlabel('Labor supply in sector 0, $L_0$', fontsize=15)
plt.ylabel(r'$\frac{\partial U}{\partial L_0}$', fontsize=25, 
           rotation='horizontal')
plt.title("It would appear that the solution is unique!", fontsize=15)
plt.grid()
plt.show()

# now solve using the various scalar root finding routines
eps = 1e-3 
root_brentq, result_brentq = optimize.brentq(numeric_foc, 
                                             a=eps, 
                                             b=1e3 - eps, 
                                             args=model_params,
                                             full_output=True,
                                             xtol=1e-12,
                                            )

root_brenth, result_brenth = optimize.brenth(numeric_foc, 
                                             a=eps, 
                                             b=1e3 - eps, 
                                             args=model_params,
                                             full_output=True,
                                             xtol=1e-12,
                                            )

root_ridder, result_ridder = optimize.ridder(numeric_foc, 
                                             a=eps, 
                                             b=1e3 - eps, 
                                             args=model_params,
                                             full_output=True,
                                             xtol=1e-12,
                                            )

root_bisect, result_bisect = optimize.bisect(numeric_foc, 
                                             a=eps, 
                                             b=1e3 - eps, 
                                             args=model_params,
                                             full_output=True,
                                             xtol=1e-12,
                                            )

# newton is more efficient, but convergence not guaranteed!
root_newton = optimize.newton(numeric_foc, 
                              x0=5e2,
                              args=model_params,
                              tol=1e-12,
                              fprime=numeric_jacobian,
                              fprime2=numeric_hessian,
                             )

# comparative statics exercise: effect of a change in the cost of capital
N = 1000
interest_rates = np.linspace(eps, 2.0 - eps, N)
roots = np.empty(N)

for i, interest_rate in enumerate(interest_rates):
    tmp_params = (0.5, 0.33, 0.66, 0.9, 1e3, interest_rate)
    tmp_root = optimize.newton(numeric_foc, 
                               x0=5e2,
                               args=tmp_params,
                               tol=1e-12,
                               fprime=numeric_jacobian,
                               fprime2=numeric_hessian,
                              )
    roots[i] = tmp_root

# plot L_0 as a function of the interest rate
plt.figure(figsize=(8,6))
plt.plot(interest_rates, roots)
plt.xlabel('Interest rate', fontsize=15)
plt.ylabel('$L_0$', fontsize=20, rotation='horizontal')
plt.grid()
plt.show()







