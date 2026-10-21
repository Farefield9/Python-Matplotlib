import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
col = [8000,12000,9800,11200,15500,7300]
pl.bar(range(6), col,color = 'olive')
pl.xticks(np.arange(6),['mon','tue','wed','thu','fri','sat'])
pl.show()
