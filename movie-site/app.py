from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ryhrrstbikgwxx:7b079307f3c0ea564a38d25763c2037ed84aa6a990f2fcbc96d939eb0bf48833@ec2-34-204-22-76.compute-1.amazonaws.com:5432/d9jdlq655pat8a"

db = SQLAlchemy(app)
from model import Movie
from model import Tvshow
from model import Trailer
from model import Kid



@app.route("/")
def say_hello():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/movie")
def movie_route():
    movies = Movie.query.all()
    return render_template("movie.html", movies=movies)

@app.route("/tvshow")
def tvshow_route():
    tvshows = Tvshow.query.all()
    return render_template("tvshow.html", tvshows=tvshows)

@app.route("/trailer")
def trailer_route():
    trailers = Trailer.query.all()
    return render_template("trailer.html", trailers=trailers)

@app.route("/kid")
def kid_route():
    kids = Kid.query.all()
    return render_template("kid.html", kids=kids)
@app.route("/movie/<int:movie_id>")
def detail_movie_route(movie_id):
  elemnt = Movie.query.get_or_404(movie_id)
  return render_template("movie_detail.html", movie=elemnt)

@app.route("/tvshow/<int:tvshow_id>")
def detail_tvshow_route(tvshow_id):
  elemnt = Tvshow.query.get_or_404(tvshow_id)
  return render_template("tvshow_detail.html", tvshow=elemnt)

@app.route("/trailer/<int:trailer_id>")
def detail_trailer_route(trailer_id):
  elemnt = Trailer.query.get_or_404(trailer_id)
  return render_template("trailer_detail.html", trailer=elemnt)

@app.route("/kid/<int:kid_id>")
def detail_kid_route(kid_id):
  elemnt = Kid.query.get_or_404(kid_id)
  return render_template("kid_detail.html", kid=elemnt)
@app.route("/add-movie", methods=['GET'])
def add_movie():
    return render_template("addMovie.html")

@app.route("/add-tvshow", methods=['GET'])
def add_tvshow():
    return render_template("addTvshow.html")

@app.route("/add-trailer", methods=['GET'])
def add_trailer():
    return render_template("addTrailer.html")
@app.route("/add-kid", methods=['GET'])
def add_kid():
    return render_template("addKid.html")
@app.route("/post-add-movie", methods = ['POST'])
def post_add_movie():
    default_name = '0'
    movie_name = request.form.get('movie_name', default_name)
    movie_year = request.form.get('movie_year', default_name)
    movie_description = request.form.get('movie_description', default_name)
    movie_type = request.form.get('movie_type', default_name)
    
    #movie_name, movie_year, movie_descreption, movie_type
    try:
        movie = Movie(
            name=movie_name,
            year=movie_year,
            description=movie_description,
            typeofMovie=movie_type
        )
        db.session.add(movie)
        db.session.commit()
        return render_template("success.html")
    except Exception as err:
        print(err)
        pass

@app.route("/post-add-tvshow", methods = ['POST'])
def post_add_tvshow():
    default_name = '0'
    tvshow_name = request.form.get('tvshow_name', default_name)
    tvshow_year = request.form.get('tvshow_year', default_name)
    tvshow_description = request.form.get('tvshow_description', default_name)
    tvshow_type = request.form.get('tvshow_type', default_name)
    
    #tvshow_name, tvshow_year, tvshow_descreption, tvshow_type
    try:
        tvshow = Tvshow(
            name=tvshow_name,
            year=tvshow_year,
            description=tvshow_description,
            typeofTvshow=tvshow_type
        )
        db.session.add(tvshow)
        db.session.commit()
        return render_template("success.html")
    except Exception as err:
        print(err)
        pass

@app.route("/post-add-trailer", methods = ['POST'])
def post_add_trailer():
    default_name = '0'
    trailer_name = request.form.get('trailer_name', default_name)
    trailer_year = request.form.get('trailer_year', default_name)
    trailer_description = request.form.get('trailer_description', default_name)
    trailer_type = request.form.get('trailer_type', default_name)
    
    #trailer_name, trailer_year, trailer_descreption, trailer_type
    try:
        trailer = Trailer(
            name=trailer_name,
            year=trailer_year,
            description=trailer_description,
            typeofTrailer=trailer_type
        )
        db.session.add(trailer)
        db.session.commit()
        return render_template("success.html")
    except Exception as err:
        print(err)
        pass
@app.route("/post-add-kid", methods = ['POST'])
def post_add_kid():
    default_name = '0'
    kid_name = request.form.get('kid_name', default_name)
    kid_year = request.form.get('kid_year', default_name)
    kid_description = request.form.get('kid_description', default_name)
    kid_type = request.form.get('kid_type', default_name)
    
    #kid_name, kid_year, kid_descreption, kid_type
    try:
        kid = Kid(
            name=kid_name,
            year=kid_year,
            description=kid_description,
            typeofKid=kid_type
        )
        db.session.add(kid)
        db.session.commit()
        return render_template("success.html")
    except Exception as err:
        print(err)
        pass
@app.route("/delete-movie/<int:movie_id>", methods=["GET"])
def delete_movie(movie_id):
    try:
        print(movie_id)
        Movie.query.filter_by( id = movie_id).delete()
        db.session.commit()
        return redirect("/movie")
    except expression as identifier:
        pass

@app.route("/delete-tvshow/<int:tvshow_id>", methods=["GET"])
def delete_tvshow(tvshow_id):
    try:
        print(tvshow_id)
        Tvshow.query.filter_by( id = tvshow_id).delete()
        db.session.commit()
        return redirect("/tvshow")
    except expression as identifier:
        pass

@app.route("/delete-trailer/<int:trailer_id>", methods=["GET"])
def delete_trailer(trailer_id):
    try:
        print(trailer_id)
        Trailer.query.filter_by( id = trailer_id).delete()
        db.session.commit()
        return redirect("/trailer")
    except expression as identifier:
        pass
@app.route("/delete-kid/<int:kid_id>", methods=["GET"])
def delete_kid(kid_id):
    try:
        print(kid_id)
        Kid.query.filter_by( id = kid_id).delete()
        db.session.commit()
        return redirect("/kid")
    except expression as identifier:
        pass
@app.route("/movie/update/<int:movie_id>")
def movie_update(movie_id):
    elemnt = Movie.query.get_or_404(movie_id)
    return render_template("updateMovie.html", movie=elemnt)

@app.route("/tvshow/update/<int:tvshow_id>")
def tvshow_update(tvshow_id):
    elemnt = Tvshow.query.get_or_404(tvshow_id)
    return render_template("updateTvshow.html", tvshow=elemnt)

@app.route("/trailer/update/<int:trailer_id>")
def trailer_update(trailer_id):
    elemnt = Trailer.query.get_or_404(trailer_id)
    return render_template("updateTrailer.html", trailer=elemnt)
@app.route("/kid/update/<int:kid_id>")
def kid_update(kid_id):
    elemnt = Kid.query.get_or_404(kid_id)
    return render_template("updateKid.html", kid=elemnt)
@app.route("/update-movie/<int:movie_id>", methods=["POST"])
def update_movie(movie_id):
    try:
        default_name = '0'
        movie_name = request.form.get('movie_name', default_name)
        movie_year = request.form.get('movie_year', default_name)
        movie_description = request.form.get('movie_description', default_name)
        movie_type = request.form.get('movie_type', default_name)
        Movie.query.filter_by(id = movie_id).update({
            "name":movie_name,
            "year":movie_year,
            "description":movie_description,
            "typeofMovie":movie_type
        })
        db.session.commit()
        return redirect("/movie")
    except expression as identifier:
        pass

@app.route("/update-tvshow/<int:tvshow_id>", methods=["POST"])
def update_tvshow(tvshow_id):
    try:
        default_name = '0'
        tvshow_name = request.form.get('tvshow_name', default_name)
        tvshow_year = request.form.get('tvshow_year', default_name)
        tvshow_description = request.form.get('tvshow_description', default_name)
        tvshow_type = request.form.get('tvshow_type', default_name)
        Tvshow.query.filter_by(id = tvshow_id).update({
            "name":tvshow_name,
            "year":tvshow_year,
            "description":tvshow_description,
            "typeofTvshow":tvshow_type
        })
        db.session.commit()
        return redirect("/tvshow")
    except expression as identifier:
        pass

@app.route("/update-trailer/<int:trailer_id>", methods=["POST"])
def update_trailer(trailer_id):
    try:
        default_name = '0'
        trailer_name = request.form.get('trailer_name', default_name)
        trailer_year = request.form.get('trailer_year', default_name)
        trailer_description = request.form.get('trailer_description', default_name)
        trailer_type = request.form.get('trailer_type', default_name)
        Trailer.query.filter_by(id = trailer_id).update({
            "name":trailer_name,
            "year":trailer_year,
            "description":trailer_description,
            "typeofMovie":trailer_type
        })
        db.session.commit()
        return redirect("/trailer")
    except expression as identifier:
        pass
@app.route("/update-kid/<int:kid_id>", methods=["POST"])
def update_kid(kid_id):
    try:
        default_name = '0'
        kid_name = request.form.get('kid_name', default_name)
        kid_year = request.form.get('kid_year', default_name)
        kid_description = request.form.get('kid_description', default_name)
        kid_type = request.form.get('kid_type', default_name)
        Kid.query.filter_by(id = kid_id).update({
            "name":kid_name,
            "year":kid_year,
            "description":kid_description,
            "typeofKid":kid_type
        })
        db.session.commit()
        return redirect("/kid")
    except expression as identifier:
        pass

   

