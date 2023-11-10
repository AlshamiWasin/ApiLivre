# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:13:55 2023

@author: Admi Super Bob
"""

from flask import Flask, jsonify

app = Flask(__name__)





@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, API!')

if __name__ == '__main__':
    app.run()
    
# salut c'est moi Henri