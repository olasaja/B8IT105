# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:47:21 2020

@author: xx-Ol
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 07:52:14 2020

@author: xx-Ol

Website:  https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption

cURL; curl "https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Connection: keep-alive" -H "Cookie: WMF-Last-Access=24-Mar-2020; WMF-Last-Access-Global=24-Mar-2020; GeoIP=IE:L:Dublin:53.33:-6.25:v4; enwikimwuser-sessionId=88367bedd1fbbb66e16b" -H "Upgrade-Insecure-Requests: 1" -H "TE: Trailers"

python wikipedia_page.py

1. Upload to gitHub
2. Write unittest
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
title = soup.title.text
print(title)

#getting table body located within <tbody> tag
#getting the first table from the page using [0]
table_body = soup.find_all('tbody')[0] 

table_text = table_body.text
#print(table_text)


#writing content of the table into rows list
rows = []

#Column names found within <th> table header tags
column_names = []
for column in  table_body.findAll('th'):    
    column_t = column.text
    column_names.append(str(column_t).strip('\n').replace('\n',''))
        
#column names written into rows list 
rows.append(column_names)
        
#rows located within <tr> tag  
#appended to rows list 
for row in table_body.find_all('tr')[1:]:  
    cells = []
    rows.append(cells)
    #cells located within <td> tag
    for cell in row.find_all('td'):
        cell_text = cell.text
        cell_text = cell_text.strip('\n')
        cell_text = cell_text.strip(',')
        if ',' in cell_text:
            cell_text = '"'+ str(cell_text) +'"'
        cells.append(cell_text)

# #display rows        
# for row in rows:        
#     row = ",".join(row)
#     print(row)
            
#save as csv file 
#add newline = '' to prevent new line from being written             
with open('wiki2.csv', 'w',newline = '') as file: 
    writer = csv.writer(file)
    writer.writerows(rows)



