#Ahnaf Kazi
#SoftDev1 pd6
#K24
#2018-11-13

from flask import Flask, render_template
import json, urllib

app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
    return urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=bw5ysm0VMzQSxOx5E762RuVWkbyPUPwt98pJesBV")
#return index.html

if __name__ == "__main__":
    app.debug = True
    app.run()
