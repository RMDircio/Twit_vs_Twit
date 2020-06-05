
from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from twit_app.models import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_user():
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return render_template("tweets.html", message="These are your lastest Tweets:", tweets=tweets)

@tweet_routes.route("/tweet/new")
def new_tweet():
    return render_template("new_tweets.html")

@tweet_routes.route("/tweet/created", methods=["POST"])
def created_tweet():
    print("FORM DATA:", dict(request.form))
    new_tweet = Tweet(tweet=request.form["tweet"], subject_id=request.form["subject_category"])
    db.session.add(new_tweet)
    db.session.commit()
    return jsonify({
        "message": "Tweet was created",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")
