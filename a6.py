import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
week = [1,2,3,4,5]
onion = [20,50,70,80,150]
tomato = [30,50,80,1200, 1]
gold = [50,100,300,500,1000]
pl.plot(week,onion, 'b', linestyle = 'dashdot', linewidth = 1)
pl.plot(week,tomato,'c', linewidth = 10, linestyle = '-.')
pl.plot(week,gold,'k', ls = ':')
pl.ylabel('prices of onion, tomato, gold')
pl.xlabel('week')
pl.grid()
pl.show()
