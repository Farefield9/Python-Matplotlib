import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
a = ['gold','silver','bronze','total']
aus = [80,59,59,198]
ind = [26,20,20,66]
pl.bar(a,aus, color = ['r','b','g','k'])
pl.bar(a,ind, width = [0.7,0.5,0.3,1], bottom = aus)
pl.xlabel('Medals')
pl.ylabel('Australia, India')
pl.show()
