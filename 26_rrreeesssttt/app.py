#Ahnaf Kazi
#SoftDev1 pd6
#K #26: Getting More REST
#2018-11-15

from flask import Flask, render_template
import json, urllib

app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
    key = "https://api.pokemontcg.io/v1/cards?name=mimikyu"
    req = urllib.request.Request(key)
    req.add_header('User-Agent','Mozilla/5.0')
    req = urllib.request.urlopen(req)
    data = req.read()
    dic = json.loads(data)
    
    kitty=json.loads(urllib.request.urlopen('https://aws.random.cat/meow').read())

    poe = json.loads(urllib.request.urlopen("https://www.poemist.com/api/v1/randompoems").read())
    
    return render_template("index.html", image=dic["cards"][0]["imageUrl"], kat=kitty["file"], poem=poe[0]["content"], Titile=poe[0]["title"])

if __name__ == "__main__":
    app.debug = True
    app.run()
