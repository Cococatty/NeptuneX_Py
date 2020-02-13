import pandas as pd
import os

import numpy as np
import datetime as dt


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
data_all = pd.read_csv("Processed_Data_20200213.tsv", sep="\t")

###########             DATA PREP             ###########

data_all.head()

# original type
data_all.dtypes

data_all_processed = data_all

data_all_processed = data_all_processed.astype({"Amount": np.float32,
                                                "randomized": np.bool_,
                                                "Date": np.dtype("M")})
te = 2.11
type(te)
data_all_processed.dtypes
data_all_processed.dtypes[["Amount"]]



data_all_processed[["Amount"]] = data_all_processed[["Amount"]].astype(np.round(decimals=2))

data_all_processed["Date"] = pd.to_datetime(data_all_processed["Date"])

x_dt = dt.date(year=2020, month=2, day=14)
print(data_all.iloc[1:5, 1:3])
# print(metadata_structure [1:10])

# del objName

data_all_processed.head()
del data_all_processed