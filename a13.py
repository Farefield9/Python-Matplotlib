import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = np.arange(4)
b = [5,25,45,20]
pl.barh(a,b)
pl.xlim(-4,1)
pl.show()
