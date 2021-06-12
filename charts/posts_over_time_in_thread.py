import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np


def postsOverTimeInThread(timeDates):
    plt.style.use('classic')
    plt.title(r'Posts in a thread over time')
    plt.ylabel(r'Post')
    plt.xlabel(r'Time')
    posts = [i for i in range( len(timeDates) )]
    plt.plot(timeDates,posts,'o',color="k")
    plt.show()

def meanPostsPerCountryFlag(data):
    plt.style.use('classic')
    plt.title(r'Average post length by country flag')
    plt.ylabel(r'Mean post length')
    plt.xlabel(r'Country')
    x = [x[0] for x in data]
    y = [y[1] for y in data] 
    plt.bar(x,y)
    plt.show()
    
