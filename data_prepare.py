import pandas as pd
import os

os.getcwd()

###########             MASTER DATA             ###########
# C:\Projects\NeptuneX_Py\
path_data_source = "\\data_preprocess\\"
fileName_source_data = "Processed_Data_20200213.tsv"
metadata_name= "Trasns_Metadata.xlsx"


###########             MASTER FUNCTIONS             ###########
def buildFileName(fileName):
    # filePath =
    return(path_data_source + "\\" + fileName)


# data_all = pd.read_csv(buildFileName(fileName_source_data), sep="\t")
data_all = pd.read_csv("ProcessedData20200213.tsv", sep="\t")


print(data_daily[1:5])
print(metadata_structure [1:10])

