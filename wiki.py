import requests
import json 
import os
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML
from wlinks import waifulinks

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main():

    outer = []
    inner = []
    imageLinks = []

    searchurl = "https://waifu.wiki/images/"

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.findAll('a') # m=true (for m to exist while scrapping(a conditional)) 

    print(len(waifulinks))

    for lin in links:
        end = lin['href']
        if len(end) <= 2 and end != '/':
            outer.append(searchurl + str(end))

    for out in outer:
        searchurl = out
        resp = requests.get(searchurl, headers=usr_agent)
        htmll = resp.text

        soup = BeautifulSoup(htmll, 'html.parser')
        links = soup.findAll('a')

        for lin in links:
            end = lin['href']
            if len(end) <= 3 and end != '/':
                inner.append(searchurl + str(end))

    for inn in inner:
        searchurl = inn
        resp = requests.get(searchurl, headers=usr_agent)
        htmlll = resp.text

        soup = BeautifulSoup(htmlll, 'html.parser')
        links = soup.findAll('a')

        for lin in links:
            inn = lin['href']
            imageLinks.append(searchurl + str(inn))

    return(str(imageLinks))
    with open('wlinks.txt', 'w') as doc:
        doc.write(str(imageLinks))


if __name__ == '__main__':
    main()