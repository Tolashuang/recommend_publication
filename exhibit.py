#coding=utf-8
import sys

sys.path.append("/home/toby/Desktop/recommend_publication/app")
from flask import render_template, redirect, request, make_response
from app import app
import search
import recommend
import visualize


@app.route('/search', methods=['POST', 'GET'])
def search():
    option = request.values.get("optionsRadios")
    inputs = request.values.get("input")
    if option == 'option1':
        data = search.query_book_by_name(name=inputs.replace(" ", "_"))
        recomendation = recommend.recommand_by_most_same(name=inputs.replace(" ", "_"))
    elif option == 'option2':
        data = search.query_movie_by_name(name=inputs)
        recomendation = recommend.recommand_by_movie_name(name=inputs)
    else:
        data = search.query_videogame_by_name(name=inputs.replace(" ", "_"))
        recomendation = recommend.recommand_by_most_same(name=inputs.replace(" ", "_"))

    response = make_response(render_template("show_result.html",
                                             data=data, recomendation=recomendation, inputs=inputs))
    return response


@app.route('/')
@app.route('/index')
def index():
    data = data_visualization.get_director_movies()
    response = make_response(render_template("index.html", data=data))
    return response


@app.route('/greet')
def greet():
    return render_template("greeting.html")
