from flask import render_template
import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {
    "bbc": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "fox": "https://moxie.foxnews.com/google-publisher/sports.xml",
    "iol": "https://rss.iol.io/iol/sunday-tribune"
    }


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    all_articles = feed["entries"]
    return render_template("home.html", articles=all_articles)

if __name__ == "__main__":
    app.run(port=5000, debug=True)