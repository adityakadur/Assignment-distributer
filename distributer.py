import os
import shutil
import errno

# Creating directory and variables storing Matlab submissions
matlab_subs = []
try:
    os.makedirs("./matlab_submissions")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
dest_m = "./matlab_submissions"

# Creating directory and variables storing Octave submissions
octave_subs = []
try:
    os.makedirs("./octave_submissions")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
dest_o = "./octave_submissions"

# Creating directory and variables storing Python submissions
python_subs = []
try:
    os.makedirs("./python_submissions")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
dest_p = "./python_submissions"

# Creating directory and variables storing Unclassified submissions
other_subs = []
try:
    os.makedirs("./unclassified_submissions")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
dest_u = "./unclassified_submissions"

# Sifting through and dividing submissions
for root, dirs, files in os.walk("./submissions"):
    path = root.split('/')
    if len(path) >= 4 :
        for file in files:
            if len(files)!=1:
                other_subs.append(root+'/'+file)
            elif "matlab" in file.lower():
                matlab_subs.append(root+'/'+file)
            elif "octave" in file.lower():
                octave_subs.append(root+'/'+file)
            elif "python" in file.lower():
                python_subs.append(root+'/'+file)
            elif "ps0" in file.lower() :
                other_subs.append(root+'/'+file)

# Copying Matlab submissions
print "Matlab submissions ("+str(len(matlab_subs))+"): \n"
for file in matlab_subs:
    print file
    path_split = file.split('/')
    src = '/'.join(path_split[:-1])
    dst = dest_m+'/'+src[2:]
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

# Copying Octave submissions
print "\n\nOctave submissions ("+str(len(octave_subs))+"): \n"
for file in octave_subs:
    print file
    path_split = file.split('/')
    src = '/'.join(path_split[:-1])
    dst = dest_o+'/'+src[2:]
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

# Copying Python submissions
print "\n\nPython submissions ("+str(len(python_subs))+"): \n"
for file in python_subs:
    print file
    path_split = file.split('/')
    src = '/'.join(path_split[:-1])
    dst = dest_p+'/'+src[2:]
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

# Copying Unclassified submissions
print "\n\nUnclassified submissions ("+str(len(other_subs))+"): \n"
for file in other_subs:
    print file
    path_split = file.split('/')
    src = '/'.join(path_split[:-1])
    dst = dest_u+'/'+src[2:]
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

# Important Summary
print "*******************************************\nSummary:\n*******************************************\n"
print "Matlab submissions :"+str(len(matlab_subs))
print "Octave submissions :"+str(len(octave_subs))
print "Python submissions :"+str(len(python_subs))
print "Unclassified submissions :"+str(len(other_subs))
print "\n\nTotal submissions processed : "+str(len(matlab_subs)+
      len(octave_subs)+len(python_subs)+len(other_subs))+\
      "\nPlease match this with the T-square count !"