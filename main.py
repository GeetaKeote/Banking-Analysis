from flask import Flask
from Banking.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info('we r testing our app')
    return "Hello World"

if __name__=="__main__":
    app.run(debug=True)