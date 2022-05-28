import numpy as np
import matplotlib.pyplot as plt
plt.ion()
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

def make_plot(mins=None, weights=None, sig=None, n=100, x=None, y=None, title='Dysphoria and the Gender Spectrum'):
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
        y = make_multi(mins, weights, x, sig=sig)
    fig = plt.figure()
    plt.plot(x,y)
    plt.ylabel('Stress')
    ym = np.min(y)
    yM = np.max(y)
    plt.yticks([ym, (yM-ym)/2 + ym, yM], ['Dysphoric', 'Neutral', 'Euphoric'])
    plt.xlabel('Gender Expression')
    plt.xticks(np.linspace(0,1,5), ['M','m', 'NB', 'f', 'F'])
    plt.title(title)
    return fig

fem = make_plot([.75], [1], sig=.15, title='Fem Preference')
fem.savefig('fem.png')
nb = make_plot([.5], [1], sig=.2, title='NB Preference')
nb.savefig('nb.png')

big_m = make_plot([.25,.75], [2,1], title='Bigender Masc Preference')
big_m.savefig('big_m.png')
big_mf = make_plot([.25,.75], [1,1], title='Bigender No Preference')
big_mf.savefig('big_mf.png')
tri_m = make_plot([.25,.5,.75], [2,1,1], title='Multigender Example')
tri_m.savefig('tri_m.png')

agen = make_plot([],[], title='Possible Agender')
agen.savefig('agen.png')

masc = make_plot([.25], [1], sig=.15, title='Masc Preference')
masc.savefig('masc.png')
# add some notes
masc.axes[0].annotate("He'd be happier here...",
            xy=(.3, .95), xycoords='axes fraction',
            xytext=(200, 0), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

masc.axes[0].annotate('But AFAB raised here',
            xy=(.75, .05), xycoords='axes fraction',
            xytext=(-100, 0), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')
masc.savefig('trans_masc.png')


big_f = make_plot([.25,.75], [1,2], title='Bigender Fem Preference')
big_f.savefig('big_f.png')
# add some notes
big_f.axes[0].annotate('AMAB living here...',
            xy=(.27, .45), xycoords='axes fraction',
            xytext=(30, 100), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

big_f.axes[0].annotate("But she'd be happier here",
            xy=(.73, .97), xycoords='axes fraction',
            xytext=(0, -200), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')
big_f.savefig('trans_big_f.png')


