# PYTHON DOES NOT HAVE POINTERS!!!!

# DELETING NEW LINES FROM A STRING
# you probably want to use a space ' ' to replace `\n`
mystring = mystring.replace('\n', ' ').replace('\r', '')
##


# LIST OF OBJECT ATTRIBUTES NOT BEING METHODS
vars(instance)
##

# OBJECT-ATTRIBUTES HANDLING
hasattr, getattr, setattr
##

# ACCESS CLASS ATTRIBUTES USING THEIR NAMES
values = [getattr(proj, a) for a in attributes]

# CHECK IF None
if var is not None:
  do sth...
##

# SELECTING A SUBDICTIONARY
keys_subset = [k1, k2, ...]
d = {key : d[key] for key in keys_subset}

# SORT DICTIONARY + PRINT IT
for key, value in sorted(dictionary.items(), reverse=False):
  f.write(key + ' : ' + str(value) + '\n')
##


# CHECK THE PATH OF THE USED MODULE
# (USEFUL IF MORE THAN 1 PYTHON ENV. IS INSTALL)

#For a pure python module you can find the source by looking at 
module_name.__file__# WHERE module_name IS E.G. numpy

# OR
import inspect
inspect.getfile(module_name)
##

# CHECK IF THE VARIABLE IS A LIST
if type(variable) == list:
  ...
## 

# ELLPISIS (WIELOKROPEK)
# SHAPE OF imageT IS (nx,ny,nz,nalphas)
imageT[..., -1] = alphas 
# ELLPISIS IS EQUIVALENT TO :,:,: HERE CAN BE ALSO [2:4,...,-4:-2] ETC.
##


# IF 1-LINERS
line2 = lines[-1] if len(lines) == 2 else 0
#x for x in list1 if l <= x <= r
##


# GENERATE PNG OF CLASS STRUCTURE
pyreverse lib_fwi_project_CLASS.py -o png
##

# PRINT ALL ATTRIBUTES AND METHODS OF AN INSTANCE OF A ClASS 
instance = My_Class()
print dir(instance)
##

# RECIPROCAL OF EACH ARRAY'S ELEMENT
slowness3D = np.reciprocal(vel3D)
##

# List attributes of an object
objectt = Classs(...)
objectt.__dict__.keys()
##

# COMMON SNIPPETS TO PASTE 
  verbos = Kwarg('verbos', 1, kwargs)
  if verbos == verbos_func:
    print this_func + 'START'
##

# UPDATE PACKAGE (E.G. matplotlib)
sudo python -mpip install -U matplotlib

# CONCATENATE 2 DICTS
a = {'a': 1}
b = {'b': 2}
# FASTER
d3 = dict(a)
d3.update(b)
# SLOWER
d3 = dict(a.items() + b.items())
##

# CHECK IF FILE EXISTS (IT FOLLOWS THE SYMLINKS)
from os.path import isfile
if not isfile(fname):
  print fname, ' not found.'
##

# SELECT SUBSET OF THE LIST USING IF
print [i for i in li if i >= 0]

# PERFORM LOGIC ON LIST-ELEMENTS
print [i if i > 0 else -i for i in li]
##

# DIVISION
>> 5 // 2 # INTEGER DIVISION IN BOTH PYTHON 2 AND 3
>> 2
##

###
## INSTALLING 
###
# IF STH IS WRONG WITH pip
pip install --upgrade setuptools
##
###

# COLLAPSING A 1-ELEMENT TUPLE (THE 'HANGING' COMMA)
a, = plt.plot(...)
##

# SLICING A MULTI-DIM ARRAY
B = A[x1:x2, y1:y2, z1:z2]
# NOT A[x1:x2][y1:y2][z1:z2]!!

# SHEBANG ENABLING RUNNING BY: ./script.py (WORKS SLOWER THAN: python script.py THOUGH)
#!/usr/bin/env python
##

# ALTHOUGH PYTHON ALLOWS TO PRINT A ROW OF THE 2D ARRAY BY SLICING
row2 = A[1][:]
# IT DOES NOT ALLOW TO PRINT A COLUMN IN A SIMILAR WAY, I.E. THIS OPERATION:
col2 = A[:][1] 
# WOULD GIVE THE SAME RESULT AS row2. INSTEAD WE NEED TO WRITE:
col2 = [i[1] for i in A]
# EDIT, CHECK ALSO:
col2 = A[:, 1]
##

# SPLIT PATH INTO PATH AND FILE
path, file_name = ntpath.split(full_path)
##

# MULTIDIM SLICING
data = data3d[:, coord] # ONLY FOR ARRAYS (NOT LIST OF LISTS)
##


# KEEP TRACK OF index IN THE LIST
for i, ll in enumerate(l):
...     print i, ll
##

# CHECK PYTHONPATHS
import sys
print sys.path
##


# TERMINATING THE PROGRAM
eprint('ERROR! ...\n')  
quit()
##


# MIN/MAX OF MULTIDIM.ARRAY A
# NUMPY!
np.max(array)
np.min(array)

# OBSOLETE: (HERE 2D)
minn = min(A.min(axis = 1))
maxx = max(A.max(axis = 1))

##


# NAMING FILES WITH NUMBERS SO THAT UNIX ORDER IS PRESERVED (PROCEED WITH ZEROS)
t = 5
no = str(t).rjust(7, '0')
##

# STRIPPING OF LEADING/TRAILING ZEROS (OR OTHER SUBSTRINGS)
string.strip(substring)
# ONLY LEADING
string.lstrip(substring)
# ONLY TRAILING
string.rstrip(substring)
##

# REPLACE NaN OF THE ARRAY WITH AN ARBITRARY NUMBER, E.G. 0
A[np.isnan(A)] = 0
##

# MERGE LISTS INTO LIST OF TUPLES
x = [1, 2, 3]
y = [3, 2, 1]
points = zip(xs, ys)
##

# SOLVE 'command 'x86_64-linux-gnu-gcc' failed with exit status 1'
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
##

# TYPICAL, VERY DANGEROUS MISTAKE:
depths, vs = depths[i], vs[i] # UNPACK FROM LIST OF LISTS
# LOOK THAT depths AND vs ARE NOT LISTS ANY MORE, SO ANOTHER ITERATION:
depths, vs = depths[i], vs[i] # TAKES ELEMENTS OF E.G. FLOAT
# INSTEAD RENAME:
depths = depths_list[i] # ETC.
##

# CLIP ARRAY/LIST (E.G. TO GET RID OF NEGATIVE VALUES)
R = np.clip(R, 0, 1e6) # VALUES < 0 BECOME 0, VALUES > 1e6 BECOME 1e6
##

# MULTIPLY 2D ARRAY BY SCALAR (ELEMENT-WISE)
R = [[10 * i for i in j] for j in R]
##

# CONCATENATE 2 ARRAYS
a = np.zeros(4)
b = np.ones(4)
print np.concatenate((a, b))
##

# CONCATENATE 2 LISTS
mergedlist = listone + listtwo
##

# Assuming you are talking about a list, 
# you specify the step in the slice (and start index). The syntax is 
li[start:end:step]
# E.g. even  - start at the beginning at take every second item:
li[::2]         
##

# REVERT A LIST BY SLICING (YES, SEE ABOVE):
reverse_lst = lst[::-1]
##

### PASSING AS ARGUMENTS:

# functions
def myfunc(anotherfunc, extraArgs):
    anotherfunc(*extraArgs) 
##

#
# The *args and **keywordargs forms are used for passing lists of arguments and dictionaries 
# of arguments, respectively. So if I had a function this:
def printlist(*args):
    for x in args:
        print x
# I could call it like this:
printlist(1, 2, 3, 4, 5) # or as many more arguments as I'd like
# For this
def printdict(**kwargs):
    print repr(kwargs)
printdict(john=10, jill=12, david=15)
# *args behaves like a list, and **keywordargs behaves like a dictionary, but you don't have to explicitly pass a list or 
# a dict to the function.
##

### HANDLING EXCEPTIONS (I.E. ERRORS)
#
try:
  file_name = sys.argv[1]
except ValueError:  
  print "Error. You should type a program argument: RF_file_name. Try again..."
##

#
try:
  file_name, sampling_freq, alpha = sys.argv[1: ]
except ValueError:  
  print "Error. You should type 3 program arguments: RF_file_name.txt, sampling_freq_in_Hz, alpha_in_Hz.  Try again..."
##

#
try:
    mode=int(raw_input('Input:'))
except ValueError:
    print "Not a number"
##

# check if float is a whole numbers
(1.0).is_integer()
>> True


#
def is_number(s):
  try:
    float(s)
    return True
  except ValueError: # it can (must) be other error in other cases, Index, Name etc.
    return False
##

##

# import function read_file from own file my_plotlib.py residing in prog
import sys
sys.path.append('home/chkajetan/Pulpit/mgr/prog')
from my_plotlib import read_file
##

# check if string contains a substring
if substring in string:
##

# sentence (1 string) from list of strings (words)
string = " ".join(lista) # between " " there can be any separator
##

#
from subprocess import call
call(["to_mod_only_vs.sh", "std*dat", "mean.dat", "mode.dat"], shell=True) # shell True enables | >, < etc.!
##

# iterate backwards
for i in reversed(li):
##

# rysowanie jak pliku mod, majac plik data
f = interpolate.interp1d(depths, vels, 'nearest')
# 2 to stopien wielomianu-spline'a. dowolnie duzy. mozna tez string: 'slinear', 'quadratic', 'cubic' 
f = interpolate.interp1d(depths, vels, 2)
# attention! it returns FUNCTION
nvels = f(ndepths)
## 

# NIE MOZNA UTOZSAMIAC LIST
# Np. LISTA_VAR = LISTA_CONSTANS
# BO TO POWODUJE AKTUALIZCJE LISTY CONSTANS!
  new_content = []
  new_content = content
  #for line in content:
    #new_content.append(line)
  #for line in new_content:
    #print line
  
  new_content.append(lines[i])
  #print lines[i]
  new_content.append(zero_lines[i])
  #print zero_lines[i]
  
  #for line in new_content:
    #print line
  #f2 = open('../' + str(new_depth) + core + str(nr) + '.mod', 'w')
  #for line in new_content:
    #f2.write(line)
  #f2.close()
  
  if i == 1: break
##


# delete last element of the list (makes it shorter)
lista.pop()
##

# convert all items in a list to floats?
[float(i) for i in lst]
##

# removing anaconda
#
Python: TypeError: __init__() takes exactly 2 arguments (1 given)
# It means you invoked a constructor of object without any argument (one argument is this object itself and one more is needed)
##

#The anaconda installer adds a line in your ~/.bash_profile script that prepends the anaconda bin directory to your $PATH environment variable. Deleting the anaconda directory #should be all you need to do, but it's good housekeeping to remove this line from your setup script too.
##

#
After (successful) installation of package (e.g. module pyserial) with pip, it will not appear in neither synaptics nor in aptitude search results
##


#I have a list of lists: something like:
  data = [[240, 240, 239],
    [250, 249, 237], 
    [242, 239, 237],
    [240, 234, 233]]
#And I want to average this out like
  [average_column_1, average_column_2, average_column_3]
from __future__ import division # at the very beginning of the file!
def mean(a):
    return sum(a) / len(a)
a =  [[240, 240, 239],
      [250, 249, 237], 
      [242, 239, 237],
      [240, 234, 233]]
print map(mean, zip(*a))



# extract a column from matrix (list of lists). See also reshape
first_column = [row[0] for row in matrix]
##

#
 numpy.arange([start, ]stop, [step, ]dtype=None)

    Return evenly spaced values within a given interval.

    Values are generated within the half-open interval [start, stop) (in other words, the interval including start but excluding stop). For integer arguments the function is equivalent to the Python built-in range function, but returns an ndarray rather than a list.
##
#
 numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source]

    Return evenly spaced numbers over a specified interval.

    Returns num evenly spaced samples, calculated over the interval [start, stop].

    The endpoint of the interval can optionally be excluded.
##
filter(function, iterable)
#Construct an iterator from those elements of iterable for which function returns true. 
#iterable may be either a sequence, a container which supports iteration, or an iterator. 
#If function is None, the identity function is assumed, that is, all elements of iterable that 
#are false are removed.
#equivalent to the generator expression 
(item for item in iterable if function(item)) # if function is not None and 
(item for item in iterable if item) #if function is None.
# get core (no extension) from full txt-file name
  core = filter(None, file_name.split(".txt"))[0]
##



# Making a flat list out of list of lists
>>> import itertools
>>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
>>> merged = list(itertools.chain.from_iterable(list2d))
# OR
data = np.ravel(data)
##


# Remove empty strings from a list of strings
str_list = filter(None, str_list) # fastest
##

# splitting a string into array of characters
>>> s = "foobar"
>>> list(s)
['f', 'o', 'o', 'b', 'a', 'r']
##

#
$ python test.py arg1 arg2 arg3 # Number of arguments: 4 arguments.
This produce following result −
  Argument List: ['test.py', 'arg1', 'arg2', 'arg3']

##

# join array of string into one string using chosen separator
sentence = ['this','is','a','sentence']
'-'.join(sentence)
  'this-is-a-sentence'
##

#
new_array = np.concatenate(([0.5], np.arange(2., 6.), [10])) # glue sequence of arrays in parenthesis
##

# adding matrices element-wise
a = [1,1]
b = [1,2]
numpy.add(a,b) # gives [2,3]
##

#
100 random numbers from gaussian N(\mu, \sigma^2):
sigma * np.random.randn(100) + mu
##

#
for line in f: 
    line = line.split(',') # to split line in excel-like files (comma is separator there)! 
##

# divide list l into n-element pieces. It returns sth called 'generator' or so, which you can iterate on
def get_chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i+n]
chunks = get_chunks(my_list, 5)
for chunk in chunks:
  ...
##

#
raw_input('Write sth: ')
  #It seems that you are mixing different Pythons here (Python 2.x vs. Python 3.x)... This is basically correct:

  #nb = input('Choose a number: ')

  #The problem is that it is only supported in Python 3. As @sharpner answered, for older versions of Python (2.x), you have to use the function raw_input:

  #nb = raw_input('Choose a number: ')
##

#
for subfolder in subfolders[1:]: # iteration omits 1st element of the list!
##

#
lista[:] = [element / liczba for element in lista] # divide list by scalar
##

# CONVERT STRINGS TO FLOATS IN LIST OF LISTS (2D LIST)
R = [[float(i) for i in row] for row in R] 
##

#
for line in file: 
  line = line.split(None) # treat ANY white sign as a separator
##

#
ndarray.tolist() # convert given ndarray to list (ndarray e.g. does not have .index() method)
##

# ADVANCED STRING FORMATTING
keys = ['problem', 'io', 'kernel', 'domain', 'dim', 'equation', 
        'anisotropy', 'qp', 'qs']
values = [getattr(proj, key) for key in keys]

info = ''.join(['\n' + '{:<20}'.format(key) + ':' + '{:>20}'.format(value) 
                for key, value in zip(keys, values)])
##
  
#
for x in numbers:
    print "{:10.4f}".format(x)
prints
   23.2300
    0.1233 # really?
    1.0000
    4.2230
 9887.2000
#
three_decimal_places = "{0:.3f}".format(max_time / nsamples)
##

# Number covers 15 places altogether and has 7 decimal places and is in "scientific format" (E or e). 
print "{:15.7E}".format(-0.0395590482454475545)
 -3.9559048E-02
##

#
label='shotid=%s'%p.shot_id)
label='shotid=%d' % (int(p.shot_id)-1))
##

#
       plt.subplot(5,1,i)
      plt.title('Geophone no.%d'%i)
      figure = plt.gcf() # get current figure
      figure.set_size_inches(15, 15)
      axes = plt.gca()
      axes.set_xlim([3500,4500])
      plt.suptitle('Place no.%d'%j+', hit no.%d'%(hit_number),size=18)
      plt.plot(geo[hit_number-1])
      i = i+1
    plt.savefig('Place no.%d'%j+', hit no.%d.png'%(hit_number
##  




#
ctrl + arrow(up/down) # scroll in Kate
##

#
        a = [[1,1],[2,2],[3,3],[1,2]]
        print a
        print sorted(a,key=lambda x:x[0])
        print sorted(a,key=lambda x:x[1])
##
