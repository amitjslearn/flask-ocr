from dateutil import parser


def parsePat1(ymd):
    '''input: tuple([y],[m],[d])
    returns only one YYYY-MM-DD'''
    # ya, ma, da = isValidPat1(isPat1(txt))
    ya, ma, da = ymd
    for y, m, d in zip(ya, ma, da):
        yyyymmdd = '-'.join([y,m,d])
        # print(yyyymmdd)
        # yyyymmdd = str(parser.parse(yyyymmdd, yearfirst= True)).split()[0]
        try:
            yyyymmdd = str(parser.parse(yyyymmdd, yearfirst = True)).split()[0]
            return yyyymmdd
        except ValueError:
            pass # conflict between month and date
        m, d = d, m
        yyyymmdd = '-'.join([y,m,d])
        # print(yyyymmdd)
        try:
            yyyymmdd = str(parser.parse(yyyymmdd, yearfirst = True)).split()[0]
        except ValueError as e:
            return "null"
        # return yyyymmdd

def parsePat2(ymd):
    '''input: tuple([y],[m],[d])
    returns only one YYYY-MM-DD'''
    ya, ma, da = ymd

    for y, m, d in zip(ya, ma, da):
        yyyymmdd = '-'.join([y,m,d])
        try:
            yyyymmdd = str(parser.parse(ymyyyymmddd, yearfirst = True)).split()[0]
        except ValueError as e:
            return "null"
        return yyyymmdd

def parsePat3(ymd):
    '''input: tuple([y],[m],[d])
    returns only one YYYY-MM-DD'''
    ya, ma, da = ymd
    # #print('ymd=',ymd)

    for y, m, d in zip(ya, ma, da):
        # #print(y,m,d)
        ymd = '-'.join([y,m,d])
        try:
            yyyymmdd = str(parser.parse(ymd, yearfirst = True)).split()[0]
        except ValueError as e:
            return "null"
        return yyyymmdd

def parsePat4(ymd):
    '''input: tuple([y],[m],[d])
    returns only one YYYY-MM-DD'''
    ya, ma, da = ymd
    # #print('ymd=',ymd)

    for y, m, d in zip(ya, ma, da):
        # #print(y,m,d)
        ymd = '-'.join([y,m,d])
        try:
            yyyymmdd = str(parser.parse(ymd, yearfirst = True)).split()[0]
        except ValueError as e:
            return "null"
        return yyyymmdd