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
    first_article=feed["entries"][0]
    return """
<html>
	<body>
		<h1> HEADLINES </h1>
		<b>{0}</b> <br/>
		<i>{1}</i> <br/>
		<p>{2}</p> <br/>
	</body>
</html>""".format(first_article.get("title"), first_article.get("published"),
                  first_article.get("summary"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)