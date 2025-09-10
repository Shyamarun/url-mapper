from flask import Flask, redirect

app = Flask(__name__)

# Hardcoded mappings (edit daily as needed)
url_map = {
    "newsupdate": "https://example.com/today-news",
    "community": "https://aiforeveryone.community.com"
}

@app.route("/<alias>")
def redirect_alias(alias):
    if alias in url_map:
        return redirect(url_map[alias])
    return "Alias not found", 404

@app.route("/")
def home():
    return "✅ URL Mapper is live! Use /alias in the URL."
