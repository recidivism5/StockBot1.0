import requests
from bs4 import BeautifulSoup

def getEthPrice():
    # the target we want to open
    url='https://ethereumprice.org/'

    #open with GET method
    resp=requests.get(url)

    #http_respone 200 means OK status
    if resp.status_code==200:

        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')

        # l is the list which contains all the text i.e news
        l=soup.find("span",{"class":"value"})

        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
        return "$" + l.text
    else:
        return "Error"

def getBtcPrice():
    # the target we want to open
    url='https://www.coindesk.com/price/bitcoin'

    #open with GET method
    resp=requests.get(url)

    #http_respone 200 means OK status
    if resp.status_code==200:

        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')

        # l is the list which contains all the text i.e news
        l=soup.find("div",{"class":"price-large"})

        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
        return l.text
    else:
        return "Error"
