import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
fb=(120,90,110,100,95)
yt=(80,90,75,85,95)
ig=(50,40,55,35,45)
x = ['Monday','Tuesday','Wednesday','Thursday','Friday']
pl.figure(figsize=(5,2))
pl.bar(x,fb,color='royalblue',width=0.2,label='FB')
pl.bar(x,yt,bottom=fb,color='red',width=0.2,label='YT')
pl.bar(x,ig,bottom=yt,color='purple',width=0.2,label='IG')
pl.xlabel('Day')
pl.ylabel('Time Speed in minutes')
pl.title("Time spend on socail media")
pl.xticks(x)
pl.legend(loc = 'center', title = 'SM')
pl.show()
