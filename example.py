import sympy as sp 

# define some symbolic variables
C_0, C_1, K_0, K_1, L_0, L_1, L_bar = sp.var('C_0:2, K_0:2, L_0:2, L_bar')

# define some symbolic parameters
alpha, beta_0, beta_1, sigma = sp.var('alpha, beta_0, beta_1, sigma')

# define some symbolic prices
r = sp.var('r')

# some functions defining output in different sectors
Y_0 = K_0**beta_0 * L_0**(1 - beta_0)
Y_1 = K_1**beta_1 * L_1**(1 - beta_1)

# must eat everything you produce (less cost of capital)
C_0 = Y_0 - r * K_0
C_1 = Y_1 - r * K_1

# fixed labor supply
L_1 = L_bar - L_0

# define the social planner's objective
rho = (sigma - 1) / sigma
U = (alpha * C_0**rho + (1 - alpha) * C_1**rho)**(1 / rho)



