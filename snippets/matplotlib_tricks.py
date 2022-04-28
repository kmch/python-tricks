#
#“frontend” is the user facing code, i.e., the plotting code, whereas the “backend” does all the hard work behind-the-scenes to make the figure. There are two types of backends: user interface backends (for use in pygtk, wxpython, tkinter, qt4, or macosx; also referred to as “interactive backends”) and hardcopy backends to make image files (PNG, SVG, PDF, PS; also referred to as “non-interactive backends”)
##

# SETTING FONT SIZE OF AXIS AND TICKS LABELS
s = 20
plt.xlabel('label text', fontsize=s)
ax.tick_params(labelsize=s) # THIS ONE IS PARTICULARLY USEFUL!!!
##

# FINER CONTROL OVER A GRID OF SUBPLOTS
from matplotlib.gridspec import GridSpec

##

# CHECK THE PATH TO CONFIG DIR
import matplotlib
matplotlib.get_configdir()
##

# CREATE A DIR FOR CUSTOM STYLES WHERE MPL CAN FIND IT 

# Alternatively, you can make your style known to Matplotlib by placing your 
# <style-name>.mplstyle file into mpl_configdir/stylelib. You can then load your 
# custom style sheet with a call to style.use(<style-name>). By default 
# mpl_configdir should be ~/.config/matplotlib, but you can check where yours 
# is with matplotlib.get_configdir(); you may need to create this directory. 
# You also can change the directory where Matplotlib looks for the stylelib/ 
# folder by setting the MPLCONFIGDIR 
# environment variable, see matplotlib configuration and cache directory locations.


# SCIENTIFIC COLORMAPS (https://matplotlib.org/cmocean/)

> sudo pip install cmocean
from cmocean.cm import *
Plot(..., cmap=deep, ...)
##
# RAINBOW COLORS
colors = iter(cm.rainbow(np.linspace(0, 1, len(list_of_plots))))
plot(..., c = next(colors))
##


# ORDER OF PLOT LAYERS (FRONT/BACK)
plt.plot(..., zorder=0) # BACK
plt.plot(..., zorder=1) # FRONT (OR JUST SET A BIG NUMBER)

# 'Setting aspect ratio of 3D plot'
ax.auto_scale_xyz([0, 500], [0, 500], [0, 0.15])
##

# Not-square axis of 3D plot:

# 1. edit the get_proj function inside site-packages\mpl_toolkits\mplot3d\axes3d.py: !!!!!!!!!!!!!
xmin, xmax = self.get_xlim3d() / self.pbaspect[0]
ymin, ymax = self.get_ylim3d() / self.pbaspect[1]
zmin, zmax = self.get_zlim3d() / self.pbaspect[2]
# 2. then add one line to set pbaspect:
ax = fig.gca(projection = '3d')
ax.pbaspect = [2.0, 0.6, 0.25]

##

# REVERSED COLORMAP
# add '_r' at the end of the name of the  standard cmap, e.g.:
viridis_r
##


# CAUTION 
# pcolormesh pecularity/bug
# it trims edges, so x & z must be +1 larger
# (pcolormesh fills space between the point defined by  X,Y, so this way 
# you get the number of intervals less than the number of points)

  x = np.arange(1, nx1 + 2) # pcolormesh TRIMS LAST
  z = np.arange(1, nx3 + 2) # ROW/COLUMN => +2 NOT +1!
##


#This combination (and values near to these) seems to "magically" work for me to keep
#the colorbar scaled to the plot, no matter what size the display.
plt.colorbar(im,fraction=0.046, pad=0.04)
#It also does not require sharing the axis which can get the plot out of square.



# TICKS
    for tic in ax.xaxis.get_major_ticks():
      if (i % 5) != 0:
        tic.label1On = tic.label2On = False
      i += 1

    #for axi in (ax.xaxis, ax.yaxis):
    #  for tic in axi.get_major_ticks()[::5]: # HIDE EVERY FIFTH
    #    tic.tick1On = tic.tick2On = True
    #    tic.label1On = tic.label2On = True
##


# EQUAL ASPECT OF BOTH AXES
plt.gca().set_aspect('equal', adjustable = 'box')
##

#
plt.axis('square')
##

#
cb = plt.colorbar(cax, orientation = 'horizontal')#, ticks=[0, glob_max])# plt.colorbar(im,fraction=0.046, pad=0.04)
tick_locator = ticker.MaxNLocator(nbins = 5)
cb.locator = tick_locator
cb.update_ticks()
##

#
fig.tight_layout()
##

# TICKS
ax.tick_params(direction = 'in', length = tick_length, width = tick_width, colors = 'k')
##

# FLIP Y-AXIS
plt.gca().invert_yaxis()
# OR
ax.set_ylim(ax.get_ylim()[::-1])
##

# EMPTY CIRCLES IN SCATTER PLOT (s - size)
plt.scatter(y_max, x_max, marker = 'o', facecolors = 'none', edgecolors = 'r', s = 100)
##

# SET LIMITS OF IMSHOW!!! (DOESN'T HAVE SIDE EFFECTS LIKE extent ALONE!)
cax = ax.imshow(P,  cmap = 'hot', interpolation = 'none', extent = [v_min, new_v_max, prof, 0], aspect = 'auto')
ax.set_xlim(1, 6)
##

# dont show the 1st xtick (prevent overlapping)
plt.gca().xaxis.set_major_locator(MaxNLocator(prune = 'lower')) 
##

# rotate ticks
plt.setp(ax.get_xticklabels(), rotation = 30, horizontalalignment = 'right')
##

# prevent too-many-figures-open error (warning)
plt.figure()
...
plt.close()
##

# problems with ssh
#The main problem is that (on your system) matplotlib chooses an x-using backend by default. I just had the same problem on one of my servers. The solution for me was to add the following code in a place that gets read before any other pylab/matplotlib/pyplot import:
import matplotlib
matplotlib.use('Agg')# Force matplotlib to not use any Xwindows backend.
#import specific matplotlib components AFTER above line 
##

#
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
##

# histogram from already binned data
matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
# make a bar plot with rectangles bounded by: left, left + width, bottom, bottom + height
##

# 'turn off' blurry effect of imshow() in matplotlib
im = plt.imshow(..., interpolation='none')
##


# font size of plot labels
import matplotlib
font = {'size'   : 22}
matplotlib.rc('font', **font)
##

# dashed lines
'-' or 'solid' 	solid line
'--' or 'dashed' 	dashed line
'-.' or 'dashdot' 	dash-dotted line
':' or 'dotted' 	dotted line
##

# math on plot labels
fig, ax = plt.subplots()
ax.set(title=r'This is an expression $\mathregular{e^{\sin(\omega\phi)}}$',
       xlabel='meters $\mathregular{10^1}$',
       ylabel=r'Hertz $\mathregular{(\frac{1}{s})}$')
plt.show()
##

#
plt.plot(vs, depths, 'o', label = mod_file, color = next(colors), lw=2) # good
plt.plot(vs, depths, label = mod_file, color = next(colors), lw=2, 'o') # error (order, after descriptive ones)
##

#
plt.plot(... 'k.', markersize = 10)
##


#
plt.legend(loc = 'lower right', frameon = False, prop={'size':9})
##

#
plt.plot(..., alpha = 0.5) # przezroczystosc 50%
##

		plt.subplot(N_rows, N_cols, N_figure) # max N_figure = N_rows*N_cols. 
		# example:
		# (2,3,1) | (2,3,2) | (2,3,3)
		# (2,3,4) | (2,3,5) | (2,3,6)   

plt.subplots_adjust(hspace = .001) # space between subplots


		colors:
        c: cyan
        m: magenta 
        k: black


plt.tick_params(
	axis='y',          # changes apply to the y-axis
	which='both',      # both major and minor ticks are affected
	left='off',      # ticks along the bottom edge are off
	right='off',         # ticks along the top edge are off
	labelleft='on') # labels along the bottom edge are on
plt.tick_params(
	axis='x',          # changes apply to the y-axis
	which='both',      # both major and minor ticks are affected
	bottom='on',         # ticks along the top edge are off
	labelbottom='on') # labels along the bottom edge are on
plt.xticks(np.arange(0, 7500, 500))
#plt.yticks(np.arange(0, 7500, 500))
plt.gca().xaxis.grid(True)
plt.gca().yaxis.grid(True)
plt.tight_layout(0.1)
plt.plot(geo)




		figure = plt.gcf() # get current figure
		figure.set_size_inches(12, 8)
		plt.savefig('noise_for_place%d' % j)


plt.suptitle('Main title') # one title for all subplots



		fig = plt.figure()
		ax = fig.add_subplot(1,1,1) 
		cax = plt.imshow(grid)#,cmap=cm.Greys_r)

		cax.set_clim()
		cbar = fig.colorbar(cax, orientation='vertical')
		cbar.set_label('time delay in ms',rotation=270) # ROTATION IS IMPORTANT (otherwise can not display)
		
		ticks = np.arange(0, 14, 1)                                                                                          
		ax.set_xticks(ticks)
		ax.set_yticks(ticks)
		
