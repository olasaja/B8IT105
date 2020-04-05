# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 07:52:14 2020

@author: 10540429

Website:  https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption

cURL; curl "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Connection: keep-alive" -H "Cookie: WMF-Last-Access=24-Mar-2020; WMF-Last-Access-Global=24-Mar-2020; GeoIP=IE:L:Dublin:53.33:-6.25:v4; enwikimwuser-sessionId=88367bedd1fbbb66e16b" -H "Upgrade-Insecure-Requests: 1" -H "TE: Trailers"

python wikipedia_page.py

1. Upload to gitHub
2. Write unittest

Github location : https://github.com/olasaja/B8IT105
"""

import requests
from bs4 import BeautifulSoup
import csv


cookies = {
    'WMF-Last-Access': '24-Mar-2020',
    'WMF-Last-Access-Global': '24-Mar-2020',
    'GeoIP': 'IE:L:Dublin:53.33:-6.25:v4',
    'enwikimwuser-sessionId': '88367bedd1fbbb66e16b',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}

response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption', headers=headers, cookies=cookies)

#Using BeautifulSoup to scrape the page content
soup = BeautifulSoup(response.content, features="html.parser")

#getting table title 
def get_title(soup):  
    title = soup.title.text
    return title

print(get_title(soup))

#getting table body located within <tbody> tag
#getting the first table from the page using [0]
def get_body(soup):
    table_body = soup.find_all('tbody')[0] 
    return table_body
#table_text = table_body.text
#print(table_text)


#Column names found within <th> table header tags
def get_content(soup):    
    #global column_names
    column_names = []
    for column in  get_body(soup).findAll('th'):    
        column_t = column.text
        column_names.append(str(column_t).strip('\xa0\n').replace('\n',''))       
#writing content of the table into rows list 
    content = []      
    #column names written into rows list 
    content.append(column_names)    
    #rows located within <tr> tag  
    #appended to rows list 
    for row in get_body(soup).find_all('tr')[1:]: #ignoring first blank line  
        cells = []
        content.append(cells)
        #cells located within <td> tag
        for cell in row.find_all('td'):
            cell_text = cell.text
            cell_text = cell_text.strip('\xa0,\n')
            if ',' in cell_text:
                cell_text = '"'+ str(cell_text) +'"'
            cells.append(cell_text)
    return content

content = get_content(soup)   
for row in content:
     row = ",".join(row)      
     print(row)
     
#save as csv file 
#add newline = '' to prevent new line from being written         
with open('wiki2.csv', 'w',newline = '') as file: 
    writer = csv.writer(file)
    writer.writerows(get_content(soup))