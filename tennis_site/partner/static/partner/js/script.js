function myMap() {
var mapProp= {
  center:new google.maps.LatLng(37.3382,-121.8863),
  zoom:12,
};
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}

myMap();