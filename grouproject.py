from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name = "Index", title = "Index")

@app.route('/about')
def about():
    return render_template("about.html", name = "About", title = "About")

@app.route('/audio')
def audio():
    return render_template("audio.html", name = "Audio Formats", title = "Audio Formats")

@app.route('/video')
def video():
    return render_template("video.html", name = "Video Formats", title = "Video Formats")

@app.route('/data')
def data():
    return render_template("data.html", name = "Data Formats", title = "Data Formats")

@app.route('/film')
def film():
    return render_template("film.html", name = "Film Formats", title = "Film Formats")

@app.route('/galleries')
def galleries():
    return render_template("galleries.html", name = "Galleries", title = "Galleries")

@app.route('/news')
def news():
    return render_template("news.html", name = "News", title = "News")

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':	#Start the Development server
    app.run(debug=True)
