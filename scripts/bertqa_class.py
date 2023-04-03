# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:58:13 2023

@author: Md Mamunur Rahman
"""

from transformers import BertForQuestionAnswering, AutoTokenizer, pipeline
    
class BertQA:
  def __init__(self):
      modelname = 'deepset/bert-base-cased-squad2'
      model = BertForQuestionAnswering.from_pretrained(modelname)
      tokenizer = AutoTokenizer.from_pretrained(modelname)
      self.nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
      
  def set_context(self,context):
      self.context = context

  def process_qa(self, question):
      result={}
      result = self.nlp({
         'question': question,
         'context': self.context
         })
      return result
