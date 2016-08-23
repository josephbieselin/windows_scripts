#!/usr/bin/python

'''
Script for renaming items in directories with identical structure.
An absolute directory pathname should be passed as the second command line
argument (after the script) and the common separator should be the third
command line argument. The trailing slashes should be passed with the
absolute directory name.
The program will recursively go through the passed in directory and it
sub-directories renaming files and directories that contain the specified
separator. Only the last element after the separator will be kept during
the renaming. If files/directories do not contain the separator, no renaming
is done.
'''

import os, sys

def changeDir(path):
    '''Changes the working directory to passed in arg "path" and appends
    a "/" to it to work with os.chdir function.'''
    os.chdir(os.path.dirname(path + '/'))

def printDiff(old, new):
    print
    print (old)
    print ("|")
    print ("|")
    print ("V")
    print (new)
    print

def rename(item, sep):
    '''Splits item by sep and stores the last element in the split list.
    os.rename is then called renaming item to the last element.
    The old and new name are printed out.'''
    newName = item.split(sep).pop().strip()
    if (item != newName):
        printDiff(item, newName)
        os.rename(item, newName)

def changeNames(sep):
    '''Iterate over items in a directory renaming items.
    The items are renamed by the "rename" function which makes use of sep.
    This function is recursively called on any sub-directories.'''
    cwd = os.getcwd()
    items = os.listdir(os.getcwd())

    for item in items:
        cur = os.path.join(os.getcwd(), item)
        # if item is a directory, recurse down
        if (os.path.isdir(cur)):
            # recurse
            changeDir(cur)
            changeNames(sep)
            changeDir(cwd)
        # change name
        rename(item, sep)


def main():
    if (len(sys.argv) < 3):
        sys.exit("ERROR:\tExpected at least 3 command line arguments")

    if (not os.path.isdir(sys.argv[1])):
        sys.exit("ERROR:\tExpected an absolute directory path as second command line argument")

    absDir = sys.argv[1]
    sep = sys.argv[2]

    changeDir(absDir)
    changeNames(sep)


if __name__ == '__main__':
    main()


__author__ = "Joe Bieselin"
__credits__ = ["Joe Bieselin"]
__version__ = "1.0.0"
__maintainer__ = "Joe Bieselin"
__email__ = "joebieselin@gmail.com"
__status__ = "Production"
