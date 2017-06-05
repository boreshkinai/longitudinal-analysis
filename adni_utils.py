import pandas as pd


ADNI_DATA_DIR = 'data/ADNI1/'


def get_rid_to_ptid():
    '''Get dictionary to convert from RID used in diadnostics data file DXSUM_PDXCONV_ADNIALL.csv in the format NNNN to
    PTID used in the MRI data file ADNI1_Complete_3Yr_1.5T_6_01_2017.csv in the format 137_S_NNNN'''
    roster_feed = pd.read_csv(ADNI_DATA_DIR + 'ROSTER.csv')
    rid_to_ptid = dict((rid, ptid) for rid, ptid in zip(roster_feed.RID.values, roster_feed.PTID.values))
    return rid_to_ptid

def get_ptid_to_rid():
    '''Get dictionary to convert from PTID used in the MRI data file ADNI1_Complete_3Yr_1.5T_6_01_2017.csv
    in the format 137_S_NNNN to  RID used in diadnostics data file DXSUM_PDXCONV_ADNIALL in the format NNNN
    '''
    roster_feed = pd.read_csv(ADNI_DATA_DIR + 'ROSTER.csv')
    ptid_to_rid = dict((ptid, rid) for ptid, rid in zip(roster_feed.PTID.values, roster_feed.RID.values))
    return ptid_to_rid

def get_visit_num_to_code():
    '''Get transformation of the field Visit in the data file ADNI1_Complete_3Yr_1.5T_6_01_2017.csv to the
    value of the field VISCODE in the data file DXSUM_PDXCONV_ADNIALL.csv
    The validity of transition can be verified using Image Data Details tab on the adni website'''
    dic = {1 : 'bl', 2 : 'N/A', 3 : 'm06', 4 : 'm12', 5 : 'm18', 6 : 'm24', 7 : 'N/A', 8 : 'm36'}
    return dic


def dxcurren_num_to_label():
    '''Transform current diagnosis from number to label. this is based on DATADIC.csv'''
    return {1:'NL', 2:'MCI',3:'AD'}

def dxcurren_label_to_num():
    '''Transform current diagnosis from label to number. this is based on DATADIC.csv'''
    return {'NL':1, 'MCI':2,'AD':3}