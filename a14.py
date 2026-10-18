import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = [74,76,69,72,81]
pl.bar(range(len(a)),a, width = 0.100)
pl.xlim(-2,10)
pl.title('prices')
pl.show()
