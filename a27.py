import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
x = ['A', 'B', 'C', 'D']
y1 = [10, 20, 10, 30]
y2 = [20, 25, 15, 25]
pl.bar(x, y1, color='r')
pl.bar(x, y2, bottom=y1, color='b')
pl.grid(True,axis = 'y')
pl.show()
