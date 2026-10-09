import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = [1,7,21,35,35,21,7,1]
s = np.sin(a)
c = np.cos(a)
t = np.tan(a)
pl.plot(a,s)
pl.figure(figsize = (100,17))
pl.show()
