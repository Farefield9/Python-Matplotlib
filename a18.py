import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = [9,10,11,12]
b = [5,6,7,8]
c = [1,2,3,4]
d = ['a','b','c','d']
pl.bar(d,a, color = 'r')
pl.bar(d,b,bottom = a, color = 'blue')
pl.bar(d,c,bottom = b, color = 'green')
pl.show()
