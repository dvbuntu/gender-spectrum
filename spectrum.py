import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

# use normal pdfs to make mixture with local mins
#x = np.linspace(0,1,100)
#y1 = ss.norm.pdf(x, 0.75, .15)
#y2 = ss.norm.pdf(x, 0.25, .15)
#y = 1.5*y1+y2
#plt.plot(x,-y)

def make_multi(mins, weights, x, sig=None):
    if sig is None:
        sig = .3 / 2**(len(mins)-1)
    y = np.zeros_like(x)
    for m,w in zip(mins,weights):
        y += w*ss.norm.pdf(x, m, sig)
    return y


## test triplot
#plt.plot(x, -make_multi([.25,.5,.75], [1,2,1], x))
## test quadplot, still works, but not as nice
#plt.plot(x, -make_multi([.2,.4,.6, .8], [1,2,1,2], x))

def make_plot(mins=None, weights=None, n=100, x=None, y=None, title='Stress and the Gender Spectrum'):
    '''
    Make spectrum plot given points on [0,1] (mins) with given weights.

    Or if precomputed y vals (or even x vals), pass those in.

    Else compute x at n different points.  If you pass in x and y with different
    shape, you get what you deserve.
    '''
    # prep data
    if x is None:
        x = np.linspace(0,1,n)
    if y is None:
        y = -make_multi(mins, weights, x)
    fig = plt.figure()
    plt.plot(x,y)
    plt.ylabel('Stress')
    ym = np.min(y)
    yM = np.max(y)
    plt.yticks([ym, (yM-ym)/2 + ym, yM], ['Low', 'Neutral', 'High'])
    plt.xlabel('Gender Identity')
    plt.xticks(np.linspace(0,1,5), ['M','m', 'NB', 'f', 'F'])
    plt.title(title)
    return fig

masc = make_plot([.25], [1], title='Masc Preference')
fem = make_plot([.75], [1], title='Fem Preference')

big_f = make_plot([.25,.75], [1,2], title='Bigender Fem Preference')
big_m = make_plot([.25,.75], [2,1], title='Bigender Masc Preference')
tri_m = make_plot([.25,.5,.75], [2,1,1], title='Multigender Example')
    

