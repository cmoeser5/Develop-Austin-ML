// const form = d3.select('form')

typeList = [
    "shopping_mall",
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
    "establishment"
]

const handleClick = () => {

    function loadType () {
        let selectedBoxes = []
        let booleanList = [true,]
        let boxes = d3.select("#categories")

        boxes.each(function (d, i) {
            let currentOption = d3.select(this)
            if (currentOption.property("checked")) {
                selectedBoxes.push((
                    Object.entries(typeList).forEach((e) => {
                        booleanList.append(selectedBoxes.includes(e))
                    }
                    currentBox._groups[0].name)
                )}
        }

        let lat = d3.select("#lat").property("value")
        let long = d3.select("#long").property("value")

        var entry = {
            latitude: lat,
            longitude: long
            types: selectedBoxes,
            
        }
    }

d3.selectAll('#submit').on('click', handleClick)





    // typeList = d3.select("#categories")
    // let options = d3.select("#cat-type").selectAll("options")
    // op   
    // // get user inputs
    // let location = d3.select('#lat-long').property('value')
    // let categories = d3.select('#categories').property('value')

}

