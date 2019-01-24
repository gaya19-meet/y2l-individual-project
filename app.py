from flask import Flask, render_template
from database import*
app = Flask(__name__)

@app.route('/')
def HomePage():
	return render_template("Homepage.html")

@app.route('/Method/<name>') #example route: /Method/game, the variable name would be 'game'
def Method(name):
	print(name)
	math_links = get_all_links_with_the_specific_type(name, "math") ## type is name 
	#return render_template("visual.html", type_name=name, math_links_html=math_links) ##### the page take the variables - the type&the links list for the specific subject
	#if name=="Visual":
	hebrew_links = get_all_links_with_the_specific_type(name, "hebrew") ## type is name 
	#return render_template("visual.html", type_name=name, math_links_html=math_links, hebrew_links_html=hebrew_links)
	english_links = get_all_links_with_the_specific_type(name, "english") ## type is name 
	arabic_links = get_all_links_with_the_specific_type(name, "arabic")
	return render_template("visual.html", type_name=name,
	 math_links_html=math_links,
	 hebrew_links_html=hebrew_links, 
	 english_links_html=english_links,
	 arabic_links_html=arabic_links)



if __name__ == '__main__':
    app.run(debug=True)

