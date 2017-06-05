import pandas as pd
import adni_utils


adni1_complete_feed = pd.read_csv(adni_utils.ADNI_DATA_DIR + 'ADNI1_Complete_3Yr_1.5T_6_01_2017.csv')


rid_to_ptid = adni_utils.get_rid_to_ptid()
print(rid_to_ptid)

a=1


