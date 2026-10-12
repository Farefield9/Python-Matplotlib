import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
height = [121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
weight = [19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
df = pd.DataFrame({'height':height,'weight':weight})
pl.xlabel('weight in kg')
pl.ylabel('height in cm')
pl.title('average weight with respect to average height')
pl.plot(df.weight,df.height,'g', marker = '*', markersize = 15, linewidth = 2, linestyle = '--')
pl.xticks(weight,rotation = 45)
pl.yticks(height)
pl.show()
