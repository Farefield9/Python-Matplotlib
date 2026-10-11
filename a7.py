import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
p = [1,2,3,4]
q = [2,4,6,8]
r = [3,6,9,12]
pl.plot(p,q, marker = 'D', markersize = 20, markeredgecolor = 'r')
pl.plot(p,r, 'r+')
pl.xticks(range(0,5,1))
pl.yticks(r)
pl.show()
