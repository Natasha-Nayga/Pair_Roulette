import sys
import random
from itertools import zip_longest

def get_names(fname):
        name_list = []
        with open(fname) as f:
                for line in f:
                        name_list.append(line.rstrip("\n")) #strip the new line
                        #random.shuffle(name_list)
                #print(name_list)
                return name_list

def grouper(iterable, n, fillvalue=None):
    #"Collect data into fixed-length chunks or blocks"
    # Taken from itertools recipes:
    # https://docs.python.org/2/library/itertools.html#recipes
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

filename = sys.argv[1]
name_list = get_names(filename)
random.shuffle(name_list)

for first_colleague, second_colleague in grouper(name_list, 2):
    print (first_colleague, "and", second_colleague)


#send email extension?


#spare code below
'''
get_names = open("names.txt", "r")
print (get_names.readlines())

name_list = get_names.readlines()

random.shuffle(name_list)
print (name_list)

get_names.close()


'''
