import random
import string
import pandas as pd
import numpy as np
from numpy import randint

n_elements = 100
col_char = random.choices(string.ascii_letters, k=n_elements)
# col_int = random.sample(range(1, 20), k=n_elements)
col_int = random.choices(range(1, 20), k=n_elements)
col_ran = random.choices(range(1, 1000), k=n_elements)

df_test = pd.DataFrame({
    "col_char": col_char,
    "col_int": col_int,
    "col_ran":col_ran
    #, dtype=
})

df_test.head()
df_test.index
# by rows
df_test[1:5]

df_test.iloc[1:3, 2:5]
df_test.iloc[:, 2:5]

df_test.loc[:, "col_ran"]

# by cols
df_test["col_char"]

print(col_char)