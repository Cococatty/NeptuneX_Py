
# acct_name_daily = "A0315920567389000-23Jul09.csv"
# acct_name_CC = "AXXXX_XXXX_XXXX_6608-13Feb13.csv"
# acct_name_homeLoan = "A0315920567389091-05Jul17.csv"
# acct_name_saver = "A0315920567389017-23Jul09.csv"
# acct_name_homebill = "A0315920567389025-10Mar14.csv"
#
# acct_dict = {
#     "daily" : "A0315920567389000-23Jul09.csv",
#     "CC" : "AXXXX_XXXX_XXXX_6608-13Feb13.csv",
#     "homeLoan" : "A0315920567389091-05Jul17.csv",
#     "saver" : "A0315920567389017-23Jul09.csv",
#     "homebill" : "A0315920567389025-10Mar14.csv",
# }


def load_data(acct_dict):
    for name in acct_dict:
        # acctName, fileName
        fileName = acct_dict[name]
        acctName = "data_" + name
        acctData = pd.read_csv(buildFileName(fileName))
        globals()[acctName] = acctData
# TBC
        # globals or exec()
#         https: // stackoverflow.com / questions / 14764088 / set - the - name - of - a - python - object - variable -
#         with-a - string


load_data(acct_dict)

# data_daily = pd.read_csv(buildFileName(acct_name_daily))



###########             LOAD MASTER DATA             ###########
# metadata_structure = pd.DataFrame(
#     pd.read_excel(buildFileName(metadata_name), sheet_name="AccountMapping")
# )


