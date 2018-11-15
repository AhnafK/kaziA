#Ahnaf Kazi
#SoftDev1 pd6
#K 24: A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import json, urllib

app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
    f = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=bw5ysm0VMzQSxOx5E762RuVWkbyPUPwt98pJesBV").read()
    dic = json.loads(f)
    return render_template("index.html", image=dic["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
