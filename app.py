from flask import Flask, render_template, request, redirect
from database import*
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


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
	history_links = get_all_links_with_the_specific_type(name, "history")
	biology_links = get_all_links_with_the_specific_type(name, "biology")

	return render_template("visual.html", type_name=name,
	 math_links_html=math_links,
	 hebrew_links_html=hebrew_links, 
	 english_links_html=english_links,
	 arabic_links_html=arabic_links,
	 history_links_html=history_links,
	 biology_links_html=biology_links)

@app.route('/create', methods=['GET', 'POST'])
def Add_Link():
	print(request.form)
	URL = request.form['link'] ### the LINK that the user ensert
	Subject = request.form['group2'] ### the SUBJECT that the usert chose for the link he put in - history,math
	Type = request.form['type'] ### the TYPE of the link = visual...

	create_link(Type, Subject, URL)        
	return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)

