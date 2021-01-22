from flask import Flask, request, jsonify, render_template
from joblib import load

lr = load("notebooks/lr.joblib")

app = Flask(__name__)

@app.route("/")
def status():
    return "Ready!"

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        data_dict = request.form
        latitude = data_dict["latitude"]
        longitude = data_dict["longitude"]
        latitude = float(latitude)
        longitude = float(longitude)
        nan = True
        default_false_checkbox = ["shopping_mall",
            "clothing_store",
            "natural_feature",
            "travel_agency",
            "food",
            "point_of_interest",
            "store",
            "meal_delivery",
            "park",
            "liquor_store",
            "gas_station",
            "restaurant",
            "cafe",
            "meal_takeaway",
            "movie_theater",
            "grocery_or_supermarket",
            "night_club",
            "hair_care",
            "finance",
            "bar",
            "art_gallery",
            "tourist_attraction",
            "cemetery",
            "supermarket",
            "real_estate_agency",
            "bakery",
            "jewelry_store",
            "place_of_worship",
            "church",
            "local_government_office",
            "home_goods_store",
            "museum",
            "car_wash",
            "car_repair",
            "aquarium",
            "establishment"]
        x_checkboxes = []
        for checkbox in default_false_checkbox:
            try:
                if data_dict[checkbox]:
                    x_checkboxes.append(True)
            except:
                x_checkboxes.append(False)
        print(x_checkboxes)
    
        X_predict = [[latitude, longitude, nan] + x_checkboxes]
        print(X_predict)
        
        rating = lr.predict(X_predict)
        print(rating)
    
        return render_template("index_predict.html", prediction=rating)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)