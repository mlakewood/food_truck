

var AppRouter = Backbone.Router.extend({
    routes: {
        "*path": "mapView" // matches http://example.com/#anything-here
    },

    mapView: function(){
        var mapView = new mapsView({'el': '#map-canvas'});
        mapView.render();
        mapView.addPoint();
        // var mapOptions = {
        //   center: new google.maps.LatLng(37.788, -122.391),
        //   zoom: 12,
        //   mapTypeId: google.maps.MapTypeId.ROADMAP
        // };
        // var map = new google.maps.Map(document.getElementById("map-canvas"),
        //     mapOptions);
      // google.maps.event.addDomListener(window, 'load', initialize);
    }
});


