# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:01:34 2018

@author: 816000026
"""

from flask import Flask
from flask import render_template
#import getCsv

app = Flask(__name__) #__main__

@app.route('/') 
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=2007)