from flask import Flask, redirect

app = Flask(__name__)

# Hardcoded mappings (edit daily as needed)
url_map = {
    "newsupdate": "https://www.canva.com/design/DAGyLu6Nvhg/SVCIkHF7mryi0dJ-dU51sg/view?utm_content=DAGyLu6Nvhg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hfd21626c30",
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
