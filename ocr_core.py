import cv2
import pytesseract
import regex as rx
import validation as vd
import pars as pr
from pre_process import pre_process

# pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
# pytesseract.pytesseract.tesseract_cmd ='/.apt/usr/share/tesseract-ocr/4.00/tessdata'
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
    text = pytesseract.image_to_string(pre_process(cv2.imread(filename)))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def ocr_date(filename):
    ''' returns the dates from the image file'''
    text = ocr_core(filename)
    # pattern 1 = 12/12/12
    finalDates1 = rx.isPat1(text)
    if len(finalDates1):
        validDates = vd.isValidPat1(finalDates1)
        yyyymmddd = pr.parsePat1(validDates)
        yyyymmddd = yyyymmddd if yyyymmddd != None else "null"
        return yyyymmddd

    finalDates2 = rx.isPat2(text)
    if len(finalDates2):
        validDates = vd.isValidPat2(finalDates2)
        yyyymmddd = pr.parsePat2(validDates)
        yyyymmddd = yyyymmddd if yyyymmddd != None else "null"
        return yyyymmddd

    finalDates3 = rx.isPat3(text)
    if len(finalDates3):
        validDates = vd.isValidPat3(finalDates3)
        yyyymmddd = pr.parsePat3(validDates)
        yyyymmddd = yyyymmddd if yyyymmddd != None else "null"
        return yyyymmddd

    finalDates4 = rx.isPat4(text)
    if len(finalDates4):
        validDates = vd.isValidPat4(finalDates4)
        yyyymmddd = pr.parsePat4(validDates)
        yyyymmddd = yyyymmddd if yyyymmddd != None else "null"
        return yyyymmddd
    
    return None


if __name__ == "__main__":

    # txt = 'DATE AND TIME PAX TABLE\n266 09/12/2012 6:14 PH 6 SZ\nCASHTER :caGHTER\n\nWAITER swarTer\n\nFRENCH FRIES\n\nOPEN Foop\n\nVAT NO\n\nASEATHANK'

    # print(ocr_date('/home/amit/internship/cv/Receipts/d50224be.jpeg'))

    # example: before parse 
    #     ya, ma, da = isValidPat2(rx.isPat2(t222))
    import argparse 

    parser = argparse.ArgumentParser(description='extract the dates from bills')
    parser.add_argument("-p",'--path',required=True, type=str, help='path to image')
    # parser.add_argument("-c",'--count',required=False, type=int, default=2000, help='number of images to be downloaded')
    args = vars(parser.parse_args())
    path = args['path']
    date = ocr_date(path)

    if date:
        print(date)
    else:
        print('date not found, try with a clearer image')
