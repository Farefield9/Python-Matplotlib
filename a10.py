import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = ['gold','silver','bronze','total']
aus = [80,59,59,198]
pl.bar(a,aus)
pl.xlabel('Medals')
pl.ylabel('Australia')
pl.show()
