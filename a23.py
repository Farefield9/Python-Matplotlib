import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = [1,2,3,1,1,1,4,4,3]
pl.hist(a, bins=5, histtype = 'step')
pl.show()
