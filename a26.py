import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
df = pd.DataFrame({'High Temp': [28, 30, 34, 38, 45, 42,
                                 38, 35, 32, 28, 25, 21],
                   'Low Temp': [22, 26, 30, 32, 41, 38,
                                32, 31, 28, 22, 15, 15],
                   'Avg Temp': [25, 28, 32, 35, 43, 40, 
                                35, 33, 30, 25, 20, 18]},
                  index=['Jan', 'Feb', 'Mar', 'Apr', 'May',
                         'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                         'Nov', 'Dec'])
df.plot(kind='bar', stacked=True, color=['red', 'skyblue', 'green'])
pl.xlabel('Months')
pl.ylabel('Temp ranges in Degree Celsius')
pl.show()
