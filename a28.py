import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
z = ['a','b','c','d','e']
a = [50,40,70,80,20]
b = [80,20,20,50,60]
c = np.arange(len(z))
pl.bar(c,a,width = 0.50,color = 'blue',label = 'science')
pl.bar(c+.5,b,width = 0.50,color = 'black',label = 'maths')
pl.xlabel('months')
pl.ylabel('subject')
pl.title('information')
pl.legend(loc = 'center')
pl.show()
