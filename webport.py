from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name = "Index", title = "Index")

@app.route('/about')
def about():
    return render_template("about.html", name = "About", title = "About")

@app.route('/contact')
def contact():
    return render_template("contact.html", name = "Contact", title = "Contact")

@app.route('/currentprojects')
def currentprojects():
    return render_template("currentprojects.html", name = "Current Projects", title = "Current Projects")

@app.route('/index')
def index():
    return render_template("index.html", name = "Index", title = "Index")

@app.route('/project1')
def project1():
    return render_template("project1.html", name = "Project 1", title = "Project 1")

@app.route('/project2')
def project2():
    return render_template("project2.html", name = "Project 2", title = "Project 2")

@app.route('/resume')
def resume():
    return render_template("resume.html", name = "Resume", title = "Resume")

@app.route('/sketchbook')
def sketchbook():
    return render_template("sketchbook.html", name = "Sketchbook", title = "Sketchbook")

#http://flask.pocoo.org/docs/0.10/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")
    #return render_template("404.html"), 404

#@app.errorhandler(500)
#def page_not_found(e):
    #return render_template("500.html"), 500

if __name__ == '__main__':	#Start the Development server
    app.run(debug=True)
