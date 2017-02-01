from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")
@app.route('/dashboard/')
def dash():
	return render_template("dashboard.html")
"""

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
@app.route('/another')
def anot():
	return "another page"
@app.route('/another/yetanother')
def anot2():
	return "yet another"
"""

if __name__ == "__main__":
    app.run(debug=True)
