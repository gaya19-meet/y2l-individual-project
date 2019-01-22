from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def HomePage():
	return render_template("Homepage.html")
@app.route('/Method')
def Method():
	return render_template("visual.html")


if __name__ == '__main__':
    app.run(debug=True)

