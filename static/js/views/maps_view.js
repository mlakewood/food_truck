var mapsView = Backbone.View.extend({
    initialize: function(){
        _.bindAll(this, 'render', 'renderFoodTrucks','addPoint', 'deleteOverlays');
        this.markersArray = [];
    },

    render: function(){
        var mapOptions = {
          center: new google.maps.LatLng(37.788, -122.391),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        this.map = new google.maps.Map(this.el,
            mapOptions);

        this.collection = new foodTruckCollection();
        this.collection.once('sync', this.renderFoodTrucks);
        this.collection.fetch();

    },

    renderFoodTrucks: function(){
        for(var i= 0; i < this.collection.length; i++){
            this.addPoint(this.collection.models[i].get('latitude'), this.collection.models[i].get('longitude'));
        }
    },

    addPoint: function(lat, lng){
        var myLatlng = new google.maps.LatLng(lat, lng);

        var marker = new google.maps.Marker({
            position: myLatlng,
            title:"Hello World!"
        });

        marker.setMap(this.map);
        this.markersArray.push(marker)
    },

    // Deletes all markers in the array by removing references to them
    deleteOverlays: function() {
      if (this.markersArray) {
        for (i in this.markersArray) {
          this.markersArray[i].setMap(null);
        }
        this.markersArray.length = 0;
      }
    }

});