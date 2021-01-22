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
        data_dict = request.get_json()

        latitude = data_dict["latitude"]
        longitude = data_dict["longitude"]
        nan = data_dict["nan"]
        shopping_mall = data_dict["shopping_mall"]
        clothing_store = data_dict["clothing_store"]
        natural_feature = data_dict["natural_feature"]
        travel_agency = data_dict["travel_agency"]
        food = data_dict["food"]
        point_of_interest = data_dict["point_of_interest"]
        store = data_dict["store"]
        meal_delivery = data_dict["meal_delivery"]
        park = data_dict["park"]
        liquor_store = data_dict["liquor_store"]
        gas_station = data_dict["gas_station"]
        restaurant = data_dict["restaurant"]
        cafe = data_dict["cafe"]
        meal_takeaway = data_dict["meal_takeaway"]
        movie_theater = data_dict["movie_theater"]
        grocery_or_supermarket = data_dict["grocery_or_supermarket"]
        night_club = data_dict["night_club"]
        hair_care = data_dict["hair_care"]
        finance = data_dict["finance"]
        bar = data_dict["bar"]
        art_gallery = data_dict["art_gallery"]
        tourist_attraction = data_dict["tourist_attraction"]
        cemetery = data_dict["cemetery"]
        supermarket = data_dict["supermarket"]
        real_estate_agency = data_dict["real_estate_agency"]
        bakery = data_dict["bakery"]
        jewelry_store = data_dict["jewelry_store"]
        place_of_worship = data_dict["place_of_worship"]
        church = data_dict["church"]
        local_government_office = data_dict["local_government_office"]
        home_goods_store = data_dict["home_goods_store"]
        museum = data_dict["museum"]
        car_wash = data_dict["car_wash"]
        car_repair = data_dict["car_repair"]
        aquarium = data_dict["aquarium"]
        establishment = data_dict["establishment"]
    
    
        #req = request.form

        #nan = data_dict["nan"]
        shopping_mall = request.form.get("shopping-mall")
        # clothing_store = data_dict["clothing_store"]
        # natural_feature = data_dict["natural_feature"]
        # travel_agency = data_dict["travel_agency"]
        # food = data_dict["food"]
        # point_of_interest = data_dict["point_of_interest"]
        # store = data_dict["store"]
        # meal_delivery = data_dict["meal_delivery"]
        # park = data_dict["park"]
        # liquor_store = data_dict["liquor_store"]
        # gas_station = data_dict["gas_station"]
        # restaurant = data_dict["restaurant"]
        # cafe = data_dict["cafe"]
        # meal_takeaway = data_dict["meal_takeaway"]
        # movie_theater = data_dict["movie_theater"]
        # grocery_or_supermarket = data_dict["grocery_or_supermarket"]
        # night_club = data_dict["night_club"]
        # hair_care = data_dict["hair_care"]
        # finance = data_dict["finance"]
        # bar = data_dict["bar"]
        # art_gallery = data_dict["art_gallery"]
        # tourist_attraction = data_dict["tourist_attraction"]
        # cemetery = data_dict["cemetery"]
        # supermarket = data_dict["supermarket"]
        # real_estate_agency = data_dict["real_estate_agency"]
        # bakery = data_dict["bakery"]
        # jewelry_store = data_dict["jewelry_store"]
        # place_of_worship = data_dict["place_of_worship"]
        # church = data_dict["church"]
        # local_government_office = data_dict["local_government_office"]
        # home_goods_store = data_dict["home_goods_store"]
        # museum = data_dict["museum"]
        # car_wash = data_dict["car_wash"]
        # car_repair = data_dict["car_repair"]
        # aquarium = data_dict["aquarium"]
        # establishment = data_dict["establishment"]


        X_predict = [[latitude, longitude, nan, shopping_mall, clothing_store, natural_feature, travel_agency, food, point_of_interest,store, meal_delivery, park, liquor_store, gas_station, restaurant, cafe, meal_takeaway, movie_theater, grocery_or_supermarket, night_club, hair_care, finance, bar, art_gallery, tourist_attraction, cemetery, supermarket, real_estate_agency, bakery, jewelry_store, place_of_worship, church, local_government_office, home_goods_store, museum, car_wash, car_repair, aquarium, establishment]]
    
        rating = lr.predict(X_predict)[0]
        print(rating)
        return render_template("index_copy.html", prediction=rating)

        # probabily_of_rating = lr.predict_proba(X_predict)[0][1]

    # return jsonify({
    # "rating": rating
    # })
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)