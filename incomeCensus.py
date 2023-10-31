import numpy as np
from matplotlib import pyplot as plt
import pandas

# Get dada
df = pandas.read_csv("adult.data", header = None)

## Note: header = None ---> Columns have no labels 

def interpolate_gaps(values, limit=None):
    """
    Fill gaps using linear interpolation, optionally only fill gaps up to a
    size of `limit`.
    """
    values = np.asarray(values)
    i = np.arange(values.size)
    valid = np.isfinite(values)
    filled = np.interp(i, i[valid], values[valid])

    if limit is not None:
        invalid = ~valid
        for n in range(1, limit+1):
            invalid[:-n] &= invalid[n:]
        filled[invalid] = np.nan

    return filled

age = df[0].values
hours = df[12].values


fig, ax = plt.subplots()

ax.scatter(age, hours, color = 'crimson', s = 5, alpha = 0.2)
ax.grid()
ax.set(xlabel = 'Age', ylabel = 'Hours per Week',
       title = 'Age vs Hours per Week')

average = np.zeros(73)
hours1 = np.zeros(73)
hours2 = np.zeros(73)

age1 = np.arange(17,90, 1)
'''
check
mask1 = (df[0] == check)
seven = df[mask1]
'''
for i in range(17,91):# For loop calculate the hour mean for every age
    mask = (df[0] == i)
    hold = df[mask]
    hours1[i-18] = (hold[12]).mean()

hours1 = interpolate_gaps(hours1, limit = 1) # getting rid of NaN

ax.plot(age1, hours1, color = 'black') # plotting the hour mean

for j in range(17,91):# For loop calculate the hour mean for every age
    mask2 = (df[0] == j)
    hold2 = df[mask2]
    hours2[j-18] = np.median(hold2[12])
    


hours2 = interpolate_gaps(hours2, limit = 1)

ax.plot(age1,hours2, color = 'cyan')

ax.legend(['Hours','Average','Median'])

fig.savefig("ageHours.pdf")




    







