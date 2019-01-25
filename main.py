from bs4 import BeautifulSoup
import requests

strPrefix = 'gvwSel_ctl'
strSuffixArray = ['_lblUnit','_lblTitle','_lblPsnCnt','_lblSelectBeginDate','_lblSelectEndDate','_btnRegisterDocu']

def search_column(css_class):
    global strSuffixArray
    if(css_class != None):
        for i in range(len(strSuffixArray )):
            if strSuffixArray [i] in css_class:
                return css_class    
head_Html='https://reg.ntuh.gov.tw/WebApplication/Administration/NtuhGeneralSelect/Entry.aspx'
res = requests.get(head_Html, timeout=30)
#print(res.text)
soup = BeautifulSoup(res.text,'lxml')
#print(soup2.prettify())
header_Info = soup.find_all(id=strPrefix)
for item in header_Info:
    print(item)