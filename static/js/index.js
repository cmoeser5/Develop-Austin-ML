// [START maps_event_click_latlng]
function initMap() {
    const myLatlng = { lat: 30.265, lng: -97.738 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 11,
      center: myLatlng,
    });
    // Create the initial InfoWindow.
    let infoWindow = new google.maps.InfoWindow({
      content: "Click the map to get Lat/Lng!",
      position: myLatlng,
    });
    infoWindow.open(map);
    // [START maps_event_click_latlng_listener]
    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
      // Close the current InfoWindow.
      infoWindow.close();
      // Create a new InfoWindow.
      infoWindow = new google.maps.InfoWindow({
        position: mapsMouseEvent.latLng,
      });
      infoWindow.setContent(
        JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
      );
      infoWindow.open(map);
      var latlong = JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
            console.log(
              JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
            );
            console.log(latlong);
            infoWindow.open(map);
            // document.getElementById('latlong').innerHTML = latlong;
            var obj = JSON.parse(latlong);
  console.log(obj)
              // Accessing individual value from JS object
            var userlat = obj.lat;
            var userlng = obj.lng;
              // alert(obj.lng);
              document.getElementById('userlat').value = userlat;
              document.getElementById('userlng').value = userlng;
              console.log(document.getElementById('userlat'))
              
    });
    // [END maps_event_click_latlng_listener]
  }
  
  function autoFill() {
    document.getElementById('userlat').value = obj.lat();
    document.getElementById('userlng').innerHTML = obj.lng;
    document.querySelector("Latitude").value = obj.lat;
  }
  // [END maps_event_click_latlng]
  
  
  
  