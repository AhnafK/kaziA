#Ahnaf Kazi
#SoftDev1 pd6
#
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
    return "I like butts"

@app.route("/auth")
def auth():
    print(app)
    print(request)
    print(request.args)
    return "Waaa hooHAHA"


    
if __name__ == "__main__":
    app.debug = True
    app.run()
    
