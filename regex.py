import re
from dateutil import parser

# seps = r"/-'.,"
# '''TEXT EXAMPLES'''
# t1 = '>: 22/05/2019 Time + 00:50' # ALL NUMS SEPS
# t2 = 'feb 18\'19' #AL SPACE NUMS SEP NUMS
# t22 = r'sep 29,2018'
# t222 = r"sep29'10"
# t3 = r"4 MAY.19" # NUM ALS SPACE AND NO SPACE
# t4 = r'03/jun/2019'

# txt = 'DATE AND TIME PAX TABLE\n266 09/12/2012 6:14 PH 6 SZ\nCASHTER :caGHTER\n\nWAITER swarTer\n\nFRENCH FRIES\n\nOPEN Foop\n\nVAT NO\n\nASEATHANK'

# '''PATTERNS'''
# import re
seps = r"/-'.,"


def isPat1(txt):
    ''' N/N/N all nums with diff seps 
    return type - dict 
    ex = {'/': 12/12/12}'''
    sepDates = {}
    finalDates ={}
    for sep in seps:
        if sep=='.':
            sep = '\\'+sep
        pat1 = re.compile(r"\d{1,4}"+sep + r"\d{1,2}" + sep + r"\d{1,4}")  # <- IMP all nums
        found = re.findall(pat1,txt)
        for f in found:
            sepDates[sep] = f
    for s in sepDates:
        if s in sepDates[s]:
            finalDates[s] = sepDates[s]    
    return finalDates

def isPat2(txt):
    '''alpha nums space -> feb 18-19'''
    sepDates = {}
    finalDates ={}
    for sep in seps:
        if sep=='.':
            sep = '\\'+sep
        pat2 = re.compile(r"\w{3} ?\d{1,2}"+sep + r"\d{1,4}")        
        found = re.findall(pat2,txt)
        for f in found:
            sepDates[sep] = f
    for s in sepDates:
        if s in sepDates[s]:
            finalDates[s] = sepDates[s]    
    return finalDates

def isPat3(txt):
    '''' now  nums alpah SPACE AND NO space -> 18 feb-19 AND feb 18-19'''
    sepDates = {}
    finalDates ={}
    for sep in seps:
        if sep=='.':
            sep = '\\'+sep
        pat3 = re.compile(r"\d{1,2} ?\w{3}"+sep + r"\d{1,4}")        
        found = re.findall(pat3,txt)
        for f in found:
            sepDates[sep] = f
    for s in sepDates:
        if s in sepDates[s]:
            finalDates[s] = sepDates[s]    
    return finalDates


def isPat4(txt):
    ''' NUM SEP AL SEP NUM 
    ex- 2019-jun-12'''
    sepDates = {}
    finalDates ={}
    for sep in seps:
        if sep=='.':
            sep = '\\'+sep
        pat4 = re.compile(r"\d{1,4}"+sep + r"\w{3}" + sep + r"\d{1,4}")  # <- IMP all nums
        found = re.findall(pat4,txt)
        for f in found:
            sepDates[sep] = f
    for s in sepDates:
        if s in sepDates[s]:
            finalDates[s] = sepDates[s]    
    return finalDates


# import pandas as pd

# df = pd.read_csv('ExtracdText38.csv')

# for imgTxt in df.text:
#     dates = ''
