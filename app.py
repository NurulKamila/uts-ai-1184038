# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:54:08 2021

@author: Nurul Kamila (1184038)
"""

from flask import Flask
from textblob import TextBlob
from flask import render_template
from flask import request
import re

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST': 
        URL = request.form['URL']
        remove = URL.replace(('-'),' ')
        change = r"https?://(www\.)?"
        text = re.sub(change, ' ', remove)
        sentiment = TextBlob(text).sentiment.polarity
        print (sentiment)
        
        if sentiment < 0:
            analysis = "Negative"
        elif sentiment == 0:
            analysis = "Netral"
        else:
            analysis = "Positive"
            
        return render_template('hasil.html', URL=URL, sentiment=sentiment, analysis=analysis)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)