import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = [10,10,100]
b = [20,50,200]
c = [30,100,300]
d = np.arange(3)
pl.bar(d,a,color = ['r','b','k'], width = 0.25)
pl.bar(d+0.25,b,color = ['g','y','w'], width = 0.20)
pl.bar(d+0.50,c,color = ['c','pink','m'], width = 0.25)
pl.show()
