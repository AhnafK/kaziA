#Ahnaf Kazi
#SoftDev1 pd6
#
#2018-09-24

from flask import Flask, render_template


app = Flask(__name__) # create instance of class Flask

#homeroute
@app.route("/")
def home_page():
	return "<a href = '/occupations'>occupations</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
