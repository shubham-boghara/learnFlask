from flask import Flask, render_template, request
from data import channels, channels_package

app = Flask(__name__)


@app.route("/")
def home():
    channels_list = []
    if request.args.get("language"):
        language = request.args.get("language").upper()
        for ch in channels:
            if ch['language'] == language:
                channels_list = ch['channel_list']
                print(channels_list)

    return render_template("home.html",
                           data=channels,
                           channels=channels_list)


@app.route("/channels")
def channel():
    channels_list = channels_package
    return render_template("channel.html", channels=channels_list)
