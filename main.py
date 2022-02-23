from flask import Flask, jsonify , request 
import csv
allarticles = [] 

with open("articles.csv", encoding ="utf-8" )as f:
    reader= csv.reader(f)
    data = list(reader)
    allarticles = data[1:]

likedmovie = []
notlikedmovies = []
notwatchedmovies = []
app = Flask(__name__)

@app.route("/get-articles")
def getmovies() :
    return jsonify({
        "data":allarticles[0],
        "status":"succees"
    })

@app.route("/liked-movie",methods = ["POST"])
def likedmovie() :
    movie = allarticles[0]
    allarticles = allarticles[1:]
    likedmovie.append(movie)
    return jsonify({
        "status":"succees"
    }),201

@app.route("/notwatched-movie",methods = ["POST"])
def notwatchedmovies() :
    movie = allarticles[0]
    allarticles = allarticles[1:]
    notwatchedmovies.append(movie)
    return jsonify({
        "status":"succees"
    }),201

@app.route("/notliked-movie",methods = ["POST"])
def notlikedmovies() :
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notlikedmovies.append(movie)
    return jsonify({
        "status":"succees"
    }),201

if __name__ == "__main__":
    app.run()