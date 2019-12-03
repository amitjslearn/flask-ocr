import re

# -------------for pat1 validn -------------
def isValidPat1(finalDates):
    ''' pat = 22/05/2019
    input - dict  ex = {'/': 12/12/12}
    checks and asserts and extracts YYYY-MM-DD
    Retutn type tuple(arrays)'''
    years, months, days = [], [], []
    for d in finalDates:
        numDates = finalDates[d].split(d)
        dym, dm, ymd = numDates # PAT 1 NNN {1,4} {1,2} {1,4}
        year = dym if len(dym)>= len(ymd) else ymd
        day = ymd if year== dym else dym
        if int(dm.strip())<=12:
            month = dm 
        else:
            month, day = day, dm
        years.append(year)
        months.append(month)
        days.append(day)
    return years, months, days

# txt = 'DATE AND TIME PAX TABLE\n266 09/12/2012 6:14 PH 6 SZ\nCASHTER :caGHTER\n\nWAITER swarTer\n\nFRENCH FRIES\n\nOPEN Foop\n\nVAT NO\n\nASEATHANK'


    #print(ymd)
# ---------------------------------------
# ==================================================
def isValidPat2(finalDates):
    '''pat2 = feb 18/19
    input - dict  ex = {'/': feb 18/19}
    checks, asserts and extracts YYYY-MM-DD
    Retutn type tuple(arrays) '''
    years, months, days = [], [], []
    for k in finalDates:
        fd = finalDates[k]
        mon =None
        month = re.findall(r"\w{3}", fd)
        for m in month:
            if m.isalpha():
                mon = m 
                yd = fd.replace(m, '')
        day, year = yd.split(k)
        day, year = day.strip(), year.strip()
        if len(year)==2:
            # works for real receipts
            if int(year) <= 19: # for receipts only after 2000
                year = '20'+ year
            else: # for receipts afer 1900s
                year = '19'+ year
        years.append(year)
        months.append(mon)
        days.append(day)

    return years, months, days

#print(isValidPat2(rx.isPat2(t222)))

    #print(str(parser.parse(ymd)).split()[0])
# ==============================================================
# -------------------------------------------------
def isValidPat3(finalDates):
    '''pat3 = 4 MAY.19
    input - dict  ex = {'/': feb 18/19}
    checks, asserts and extracts YYYY-MM-DD
    Retutn type tuple(arrays) '''
    years, months, days = [], [], []
    for k in finalDates:
        fd = finalDates[k]
        mon =None
        month = re.findall(r"\w{3}", fd)
        for m in month:
            if m.isalpha():
                mon = m 
                yd = fd.replace(m, '')
                day, year = yd.split(k)
                day, year = day.strip(), year.strip()
                assert len(year) >= len(day), "len year !>= len day"
                if len(year)==2:
                    # works for real receipts
                    if int(year) <= 19: # for receipts only after 2000
                        year = '20'+ year
                    else: # for receipts afer 1900s
                        year = '19'+ year
                years.append(year)
                months.append(mon)
                days.append(day)

    return years, months, days




# -------------------------------------------------------
# ===============================
def isValidPat4(finalDates):
    '''pat3 = 03/jun/2019 
    checks and asserts and extracts YYYY-MM-DD
    Retutn type tuple(arrays)'''
    years, months, days = [], [], []
    for d in finalDates:
        numDates = finalDates[d].split(d)
        dy, m, yd = numDates # PAT 1 NNN {1,4} {1,2} {1,4}
        year = yd if len(yd)>= len(dy) else dy
        day = dy if year== yd else yd
        month = m
        years.append(year)
        months.append(month)
        days.append(day)
    return years, months, days

# finalDates = rx.isPat4(t4)

#print(finalDates)
#print()


#print(parsePat4(isValidPat4(finalDates)))
# =============================================