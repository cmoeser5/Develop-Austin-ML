from flask import Flask, request, jsonify
from joblib import load

clf = load("../notebooks/lr.joblib")

app = Flask(__name__)

@app.route("/")
def status():
    return "Ready!"

@app.route("/predict", methods=["POST"])
def predict():
    data_dict = request.get_json()

    latitude = data_dict["latitude"]
    longitude = data_dict["longitude"]
    types = [False for i in range(37)]
    types_dd = []
    for i in types:
        types_dd.append(data_dict[i])
    
    X_predict = [[latitude, longitude, *types_dd]]

    rating = lr.predict(X_predict)[0]
    probabily_of_rating = lr.predict_proba(X_predict)[0][1]

    return jsonify({
        "rating": rating,
        "probabily_of_rating": float(probabily_of_rating)
    })

if __name__ == "__main__":
    app.run(debug=True)