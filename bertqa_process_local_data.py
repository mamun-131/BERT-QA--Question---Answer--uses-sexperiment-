# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:58:13 2023

@author: Md Mamunur Rahman
"""
import textract
import scripts.bertqa_class as BERTQA

bertqa = BERTQA.BertQA()

# inject data for reading
context = str(textract.process('data/data1.docx')).replace("\\n", " ").replace("\\t"," ").replace("  "," ").replace("  "," ")
print(context)
bertqa.set_context(context)

# ask question
def askqa():
    question = input("Ask question: ")  
    result = bertqa.process_qa(question)
    print(result)
    askqa()

askqa()
