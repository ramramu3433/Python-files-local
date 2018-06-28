# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:08:15 2018

@author: janakiraman.r
"""


from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

if __name__=="__main__":
    
   app.run()