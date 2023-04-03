# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:58:13 2023

@author: Md Mamunur Rahman
"""
import scripts.bertqa_class as BERTQA
import scripts.wiki_scrape as wiki

bertqa = BERTQA.BertQA()
topic = input("Topic: ")  
context = wiki.wikidatasearch(topic)
print(context)
bertqa.set_context(context)
# ask question
def askqa():
    
    question = input("Ask question: ")  

    result = bertqa.process_qa(question)
    print(result)
    askqa()

askqa()
