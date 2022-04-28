# block selection
# with pressed alt

# Add conda environment as a jupyter kernel
# I think, the current environment you're in (i.e. is activated), doesn't matter.
# Definitely works if you're already in conda_environment_name 
python -m ipykernel install --user --name=conda_environment_name



# -------------------------------------------------------------------------------
# Jupyter themes
# -------------------------------------------------------------------------------
# kmc:
# -t, --theme
# -T, --toolbar
jt -t grade3 -T   # light
jt -t gruvboxd -T # dark


# https://www.kaggle.com/getting-started/97540
pip3 install jupyterthemes
# list available themes
jt -l
# restore default theme
# NOTE: Need to delete browser cache after running jt -r
# If this doesn't work, try starting a new notebook session.
jt -r
# select theme
jt -t monokai
# (developer's words) I use below setting-
# my two go-to styles
# dark
jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T
jt -t monokai -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

# light
jt -t grade3 -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T
# 

# -------------------------------------------------------------------------------
# HTML
# -------------------------------------------------------------------------------

# Reload embedded (e.g. with ![title](path_to_figure.png)
# html figure
# --> reload the page in the browser! (NOT the kernel)
##

# COMMENT 
<!-- a_0 \sum_{k=0}^{n-1} r^k = -->

# NEW PARAGRAPH
<p>
</p>

# BREAK LINE WITHOUT CREATING NEW PARAGRAPH
<br>

# -------------------------------------------------------------------------------



# CONVERTING TO LATEX (HAVEN'T CHECKED IT THOUGH)
jupyter nbconvert --to latex nb.ipynb

# CONVERT TO HTML (PRESERVES EMBEDDED GIFS!)
jupyter nbconvert --to html notebook.ipynb  
##


# to slides and print correctly!!!!!!!
jupyter nbconvert --to slides --post serve /path/to/your/notebook.ipynb

This should fire up your browser and serve the presentation (e.g at http://127.0.0.1:8000/<some-title>.slides.html#/)

change the url to

 http://127.0.0.1:8000/<some-title>.slides.html?print-pdf




#No module autoreload error
#just delete trailing spaces from
%load_ext autoreload




# ESSENTIAL SHORTCUTS
ctr+c     # COPY/PASTE CELLS ACROSS DIFFERENT NOTEBOOKS!
ctr+v     ##
ctrl + /  # (un)comment line
ctrl + d  # delete line
##

# EMBEDD FIGURE 
![title](img/picture.png)



# (UN)FOLD SECTIONS ETC. 
# press left (right) arrow key
##

# GET INTERACTIVE WIDGETS (SLIDER ETC.) TO WORK 
%matplotlib notebook 
##

# -------------------------------------------------------------------------------
# INSTALLATION
# -------------------------------------------------------------------------------

# INSTALLING PYTHON 2 OR 3 KERNEL
# (FOR PYTHON 3, REPLACE python2 WITH python 3)
sudo python2 -m pip install --upgrade ipykernel # install the kernel package for Python 2
sudo python2 -m ipykernel install # register the Python 2 kernelspec

# INSTALL EXTENSIONS (RUN BOTH)
sudo pip install jupyter_contrib_nbextensions 
sudo jupyter contrib nbextension install 
##

# ENABLING/DISABLING EXTENSIONS MANUALLY
# IN BASH:
jupyter nbextension enable <nbextension require path>
# WHERE THE PATH CAN BE READ FROM THE BROWSER DESCRIPTIN, E.G. 
jupyter nbextension enable runtools/main
##

# plots
%matplotlib inline # must be in the first line (probably) of first cell
##

#
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20, 10) # set plots size
##

# starting on Windows (because in the browser you can't e.g. change drive (C:\ -> D:\)
put link to jupyter notebook in the working directory (or any other PARENT directory)
write in 'Rozpocznij w ' box the current path
##

# change 'code' to 'markdown' to write LaTeX, e.g.:
$$ e^x $$
##
