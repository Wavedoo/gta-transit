from flask import Flask, request, jsonify
from urllib.request import urlopen

import json

app = Flask(__name__)

BASE_URL = "https://myttc.ca/"

@app.route("/")
def home():
    return "Welcome tester"

@app.route("/near")
def near():
    long = request.args.get("longitude")
    lat = request.args.get("latitude")

    print("long", long)
    print("lat", lat)


    if long and lat:
        url = BASE_URL +"near/"+long +"," +lat + ".json"
        return "Trying to access " + url + ", but there are some issues. Look into GTFS."
        # return processUrl(url), 200
    else:
        url = BASE_URL + "kennedy_station.json"
        return processUrl(url), 200


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

def processUrl(url):
    print(url)
    # store the response of URL
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    return data_json

if __name__ == "__main__":
    app.run(debug=True)
# print("Hello world!")