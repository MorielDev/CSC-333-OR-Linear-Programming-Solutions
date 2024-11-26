#!/usr/bin/env python
# coding: utf-8

# In[5]:


# QUESTION 1
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=3x+4y
SUBJECT TO

            2x + 3y ≤ 12
            x + 2y ≤ 8
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: 2x + 3y ≤ 12 → y = (12 - 2x) / 3
y1 = (12 - 2 * x) / 3

# Constraint 2: x + 2y ≤ 8 → y = (8 - x) / 2
y2 = (8 - x) / 2

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$2x + 3y \leq 12$')
plt.plot(x, y2, label=r'$x + 2y \leq 8$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 1: Maximizing Profit for a Factory')

# Plot the objective function (Z = 3x + 4y)
# Example level curves of the objective function
for z in [10, 20, 30]:
    y_obj = (z - 3 * x) / 4
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[7]:


# QUESTION 2
import numpy as np
import matplotlib.pyplot as plt

"""
MINIMIZE 
            Z=2x+5y
SUBJECT TO

            x + 2y ≤ 6
            2x + y ≤ 5
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: x + 2y ≤ 6 → y = (6 - x) / 2
y1 = (6 - x) / 2

# Constraint 2: 2x + y ≤ 5 → y = (5 - 2 * x)
y2 = (5 - 2 * x)

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$x + 2y \leq 6$')
plt.plot(x, y2, label=r'$2x + y \leq 5$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 2: Minimizing Cost for a Manufacturer')

# Plot the objective function (Z = 2x + 5y)
for z in [10, 20, 30]:
    y_obj = (z - 2 * x) / 5
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[8]:


# QUESTION 3
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=5x+4y
SUBJECT TO

            2x + y ≤ 20
            3x + 2y ≤ 30
            x + 2y ≤ 18
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 20, 400)

# Constraint 1: 2x + y ≤ 20 → y = 20 - 2x
y1 = 20 - 2 * x

# Constraint 2: 3x + 2y ≤ 30 → y = (30 - 3 * x) / 2
y2 = (30 - 3 * x) / 2

# Constraint 3: x + 2y ≤ 18 → y = (18 - x) / 2
y3 = (18 - x) / 2

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$2x + y \leq 20$')
plt.plot(x, y2, label=r'$3x + 2y \leq 30$')
plt.plot(x, y3, label=r'$x + 2y \leq 18$')

# Shade the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 3: Maximizing Production with Multiple Resources')

# Plot the objective function (Z = 5x + 4y)
for z in [20, 40, 60]:
    y_obj = (z - 5 * x) / 4
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[9]:


# QUESTION 4
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=4x+5y
SUBJECT TO

            x + 2y ≤ 20
            2x + y ≤ 15
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 15, 400)

# Constraint 1: x + 2y ≤ 20 → y = (20 - x) / 2
y1 = (20 - x) / 2

# Constraint 2: 2x + y ≤ 15 → y = (15 - 2 * x) / 1
y2 = (15 - 2 * x)

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$x + 2y \leq 20$')
plt.plot(x, y2, label=r'$2x + y \leq 15$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 15)
plt.ylim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 4: Maximizing Revenue from Sales')

# Plot the objective function (Z = 4x + 5y)
for z in [20, 40, 60]:
    y_obj = (z - 4 * x) / 5
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[10]:


# QUESTION 5
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=8x+7y
SUBJECT TO

            3x + 2y ≤ 12
            2x + y ≤ 6
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 12, 400)

# Constraint 1: 3x + 2y ≤ 12 → y = (12 - 3 * x) / 2
y1 = (12 - 3 * x) / 2

# Constraint 2: 2x + y ≤ 6 → y = (6 - 2 * x)
y2 = (6 - 2 * x)

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$3x + 2y \leq 12$')
plt.plot(x, y2, label=r'$2x + y \leq 6$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 12)
plt.ylim(0, 8)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 5: Resource Allocation for Two Projects')

# Plot the objective function (Z = 8x + 7y)
for z in [20, 40, 60]:
    y_obj = (z - 8 * x) / 7
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[11]:


# QUESTION 6
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=5x+3y
SUBJECT TO

            x + 2y ≤ 8
            3x + 2y ≤ 12
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: x + 2y ≤ 8 → y = (8 - x) / 2
y1 = (8 - x) / 2

# Constraint 2: 3x + 2y ≤ 12 → y = (12 - 3 * x) / 2
y2 = (12 - 3 * x) / 2

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$x + 2y \leq 8$')
plt.plot(x, y2, label=r'$3x + 2y \leq 12$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 6: Production Planning for a Bakery')

# Plot the objective function (Z = 5x + 3y)
for z in [10, 20, 30]:
    y_obj = (z - 5 * x) / 3
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[13]:


#QUESTION 7
import numpy as np
import matplotlib.pyplot as plt

"""
MINIMIZE 
            Z=6x+7y
SUBJECT TO

            3x + 2y ≤ 18
            2x + y ≤ 10
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: 3x + 2y ≤ 18 → y = (18 - 3 * x) / 2
y1 = (18 - 3 * x) / 2

# Constraint 2: 2x + y ≤ 10 → y = (10 - 2 * x)
y2 = (10 - 2 * x)

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$3x + 2y \leq 18$')
plt.plot(x, y2, label=r'$2x + y \leq 10$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 7: Minimizing Cost for a Transport Company')

# Plot the objective function (Z = 6x + 7y)
for z in [20, 40, 60]:
    y_obj = (z - 6 * x) / 7
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[14]:


# QUESTION 8
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=10x+12y
SUBJECT TO

            4x + y ≤ 30
            2x + 2y ≤ 18
            3x + 3y ≤ 24
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: 4x + y ≤ 30 → y = 30 - 4x
y1 = 30 - 4 * x

# Constraint 2: 2x + 2y ≤ 18 → y = (18 - 2 * x) / 2
y2 = (18 - 2 * x) / 2

# Constraint 3: 3x + 3y ≤ 24 → y = (24 - 3 * x) / 3
y3 = (24 - 3 * x) / 3

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$4x + y \leq 30$')
plt.plot(x, y2, label=r'$2x + 2y \leq 18$')
plt.plot(x, y3, label=r'$3x + 3y \leq 24$')

# Shade the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 8: Maximizing Revenue from Two Products')

# Plot the objective function (Z = 10x + 12y)
for z in [20, 40, 60]:
    y_obj = (z - 10 * x) / 12
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[16]:


# QUESTION 9
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=500x+400y
SUBJECT TO

            4000x + 2000y ≤ 5000
            2000x + 2500y ≤ 4500
            1000x + 1500y ≤ 3000
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 1.5, 400)  # Range adjusted for smaller coefficients

# Constraint 1: 4000x + 2000y ≤ 5000 → y = (5000 - 4000 * x) / 2000
y1 = (5000 - 4000 * x) / 2000

# Constraint 2: 2000x + 2500y ≤ 4500 → y = (4500 - 2000 * x) / 2500
y2 = (4500 - 2000 * x) / 2500

# Constraint 3: 1000x + 1500y ≤ 3000 → y = (3000 - 1000 * x) / 1500
y3 = (3000 - 1000 * x) / 1500

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$4000x + 2000y \leq 5000$')
plt.plot(x, y2, label=r'$2000x + 2500y \leq 4500$')
plt.plot(x, y3, label=r'$1000x + 1500y \leq 3000$')

# Shade the feasible region
plt.fill_between(
    x,
    np.minimum(np.minimum(y1, y2), y3),
    0,
    color='red',
    alpha=0.3,
    label='Feasible Region'
)

# Labels and legends
plt.xlim(0, 1.5)
plt.ylim(0, 1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 9: Advertising Campaign Budget Allocation')

# Plot the objective function (Z = 500x + 400y)
for z in [1000, 2000, 3000]:
    y_obj = (z - 500 * x) / 400
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[19]:


#Question 10: Meal Planning for a School Cafeteria (`question_10.py`)

import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z=6x+5y
SUBJECT TO

            2x + 3y ≤ 30
            4x + 2y ≤ 24
            x + 2y ≤ 20
            x ≥ 0, y ≥ 0 (non-negativity constraints)
"""
# Define the constraints
x = np.linspace(0, 15, 400)

# Constraint 1: 2x + 3y ≤ 30 → y = (30 - 2 * x) / 3
y1 = (30 - 2 * x) / 3

# Constraint 2: 4x + 2y ≤ 24 → y = (24 - 4 * x) / 2
y2 = (24 - 4 * x) / 2

# Constraint 3: x + 2y ≤ 20 → y = (20 - x) / 2
y3 = (20 - x) / 2

# Feasibility conditions (non-negative)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$2x + 3y \leq 30$')
plt.plot(x, y2, label=r'$4x + 2y \leq 24$')
plt.plot(x, y3, label=r'$x + 2y \leq 20$')

# Shade the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Labels and legends
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Question 10: Meal Planning for a School Cafeteria')

# Plot the objective function (Z = 6x + 5y)
for z in [20, 40, 60]:
    y_obj = (z - 6 * x) / 5
    plt.plot(x, y_obj, linestyle='--', label=f'Z={z}')

plt.legend()
plt.show()


# In[ ]:




