from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Movie

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/socialmarketing')
def socialmarketing():
    return render_template('socialmarketing.html')

@app.route('/digitalmarketing')
def digitalmarketing():
    return render_template('digitalmarketing.html')

@app.route('/dataanalysis')
def dataanalysis():
    return render_template('dataanalysis.html')

@app.route('/contentmarketing')
def contentmarketing():
    return render_template('contentmarketing.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')


@app.route("/purchase/<int:id>")
def purchase_movie(id):
    movie = Movie.query.get_or_404(id)
    return render_template("purchase.html")

@app.route("/cart")
def cart(id):
    pass





  

  


