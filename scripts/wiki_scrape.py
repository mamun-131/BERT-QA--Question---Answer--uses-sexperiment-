# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 07:05:19 2023

@author: ThinkPad
"""

import requests
from bs4 import BeautifulSoup
import wikipedia
import re

def wikidatasearch(topic):
    search_result = []
    
    search_result = wikipedia.search(topic)
    
    print (search_result)
    text = ''
    
    count = 0
    for node in search_result:
        # Specify the title of the Wikipedia page
        print (node.replace(" ","_"))
        # wiki = wikipedia.page(node.replace(" ","_"))
        # # Extract the plain text content of the page
        # text +=  wiki.content
      

        response = requests.get(
         	url="https://en.wikipedia.org/wiki/" + node,
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        for paragraph in soup.find_all('p'):
            text += paragraph.text

        count=count+1
        if count>0:
            break
        
    # Clean text
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')
    return text




