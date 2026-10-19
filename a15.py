import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = range(4)
b = [23.5,25,26,28]
pl.xticks(range(0,4))
pl.bar(a,b,width = 0)
pl.bar(a,b,width = 0.25)
pl.show()
