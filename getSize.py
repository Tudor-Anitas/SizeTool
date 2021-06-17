import os
import sys
import progressbar

# will store all subfiles from the provided folder
folder_files = []

# this class stores a file name along with its size
class Subfile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def toString(self):
        if self.size>1024:
            print(self.name.ljust(100, '-') + str(round(self.size / 1024)).rjust(10) + ' GB')
        else:
            print(self.name.ljust(100, '-') + str(round(self.size)).rjust(10) + ' MB')

# calculates the size of the directory given
def getFolderSize(directory):
    size = 0

    # first check if it is a folder, if it is,
    # iterate through the files within and calculate the size of the parent
    if os.path.isdir(directory):
        for path, dirs, files in os.walk(directory):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        # after the size is calculated, put the path and size inside a subfile and store it into the list
        folder_files.append(Subfile(directory, size/(1024*1024)))

    # in case the path given is a file, calculate the size and put it into the list
    else:
        size = os.path.getsize(directory)
        folder_files.append(Subfile(directory, size / (1024 * 1024)))


directory = str(sys.argv[1])
#directory = 'D:\Vst'



# iterate through all the files inside the given folder
# and calculate their size
files = os.listdir(directory)

bar = progressbar.ProgressBar(maxval=len(files)).start()
i = 0
for file in files:
    getFolderSize(directory + '\\' + file)
    i+=1
    bar.update(i)



# the key to sort the list
def sizeKey(obj):
    return obj.size

# after the size of all files have been measured, sort the list from big to small
# and print it to screen
folder_files.sort(key=sizeKey ,reverse=True)
for file in folder_files:
    file.toString()





