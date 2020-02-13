# Dynamic source data files load


from os import listdir
from os.path import isfile, join

all_data_file = [f for f in listdir(path_data_source) if isfile(join(path_data_source, f))]