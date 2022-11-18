# %%
# Make sure you have pip installed uncertainties first
from uncertainties import ufloat
import math

# %% [markdown]
# 1. There is a rectangle whose sides are 2 ± 0.1 m and 4 ± 0.2 m, what is its area and area uncertainty?

# %%
x = ufloat(2, 0.1)
y = ufloat(4, 0.2)

print("Area with uncertainty:", x * y)

# %% [markdown]
# 2. We live in a rectangular room of size (6 ± 0.1 m) x (8 ± 0.1 m) x (3 ± 0.1 m), what is the mass of the air in the room? What is your uncertainty in the answer?

# %%
x = ufloat(6, 0.1)
y = ufloat(8, 0.1)
z = ufloat(3, 0.1)

v = x * y * z
d = 1.3
m = v * d
print("Mass of air:", m)

# %% [markdown]
# 3. We are trying to estimate g, the gravitational acceleration near earth surface by measuring a pendulum period. If the pendulum's length is L and its period is T, g is given by
# [Insert Formula]
# we measure L = 1 ± 0.01 meter, T = 1.99 ± 0.04 second, what is g and its uncertainty?

# %%
L = ufloat(1, 0.01)
T = ufloat(1.99, 0.04)

print("g =", ((2 * math.pi) ** 2) * (L / T) ** 2)
