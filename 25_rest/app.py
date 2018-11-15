#Ahnaf Kazi
#SoftDev1 pd6
#K 25: A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import json, urllib

app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
    url = 'https://api.twitch.tv/helix/streams'
    req = urllib.request.urlopen(url)
    req = req.add_header("Client-ID","du81t8trvj2pz2ebio05eybxqgmdtq")
    req = req.read()
    dic = json.loads(req)
    return render_template("index.html", image=dic["data"]["user_name"])

if __name__ == "__main__":
    app.debug = True
    app.run()
