var mapsView = Backbone.View.extend({
    initialize: function(){
        _.bindAll(this, 'render', 'renderFoodTrucks','addPoint', 'deleteOverlays', 'getCenter', 'radiusControl', 'refreshCollection');
        this.markersArray = [];
    },

    refreshCollection: function(center, distance){
        console.log('refresh collection');
        
        this.deleteOverlays();
        this.collection.once('sync', this.renderFoodTrucks);

        if((center !== undefined) && (distance !== undefined)){
            center_location = center.ob + ',' + center.pb
            this.collection.fetch({ data: { current_location: center_location, distance: distance  },
                                    processData: true});
        }else{
            this.collection.fetch();
        }

        // current_location = center

    },

    render: function(){
        var self = this;
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
        this.control = this.radiusControl()
        this.map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(this.control);


    },

    getCenter: function(){
        console.log(this.map.getCenter());
    },

    renderFoodTrucks: function(){
        for(var i= 0; i < this.collection.length; i++){
            this.addPoint(this.collection.models[i]);
        }
    },

    addPoint: function(model){
        if(model !== undefined){
            var myLatlng = new google.maps.LatLng(model.get('latitude'), model.get('longitude'));

            var marker = new google.maps.Marker({
                position: myLatlng,
                title: model.get('name'),
            });

            marker.setMap(this.map);
            this.markersArray.push(marker) 
        }

    },

    // Deletes all markers in the array by removing references to them
    deleteOverlays: function() {
      if (this.markersArray) {
        for (i in this.markersArray) {
          this.markersArray[i].setMap(null);
        }
        this.markersArray.length = 0;
      }
    },

    radiusControl: function (){
        var self = this;

        var controlDiv = document.createElement('div');


        // Set CSS styles for the DIV containing the control
        // Setting padding to 5 px will offset the control
        // from the edge of the map.
        controlDiv.style.padding = '5px';

        // Set CSS for the control border.
        var controlUIOneMile = document.createElement('div');
        controlUIOneMile.style.backgroundColor = 'white';
        controlUIOneMile.style.borderStyle = 'solid';
        controlUIOneMile.style.borderWidth = '2px';
        // controlUIOneMile.style.paddingTop = '20px';
        controlUIOneMile.style.cursor = 'pointer';
        controlUIOneMile.style.textAlign = 'center';
        controlUIOneMile.title = 'Click to include food vans within 1 Miles';
        controlUIOneMile.id = '1-mile';
        controlDiv.appendChild(controlUIOneMile);

        // Set CSS for the control interior.
        var controlTextOneMile = document.createElement('div');
        controlTextOneMile.style.fontFamily = 'Arial,sans-serif';
        controlTextOneMile.style.fontSize = '12px';
        controlTextOneMile.style.paddingLeft = '4px';
        controlTextOneMile.style.paddingRight = '4px';
        controlTextOneMile.innerHTML = '<strong>1 Mile</strong>';
        controlUIOneMile.appendChild(controlTextOneMile);

        google.maps.event.addDomListener(controlUIOneMile, 'click', function() {
          self.refreshCollection(self.map.getCenter(),1);
        });

        // Set CSS for the control border.
        var controlUITwoMile = document.createElement('div');
        controlUITwoMile.style.backgroundColor = 'white';
        controlUITwoMile.style.borderStyle = 'solid';
        controlUITwoMile.style.borderWidth = '2px';
        controlUITwoMile.style.cursor = 'pointer';
        controlUITwoMile.style.textAlign = 'center';
        controlUITwoMile.title = 'Click to include food vans within 2 Miles';
        controlUITwoMile.id = '2-mile';
        controlDiv.appendChild(controlUITwoMile);

        // Set CSS for the control interior.
        var controlTextTwoMile = document.createElement('div');
        controlTextTwoMile.style.fontFamily = 'Arial,sans-serif';
        controlTextTwoMile.style.fontSize = '12px';
        controlTextTwoMile.style.paddingLeft = '4px';
        controlTextTwoMile.style.paddingRight = '4px';
        controlTextTwoMile.innerHTML = '<strong>2 Mile</strong>';
        controlUITwoMile.appendChild(controlTextTwoMile);

        google.maps.event.addDomListener(controlUITwoMile, 'click', function() {
          self.refreshCollection(self.map.getCenter(),2);
        });

        // Set CSS for the control border.
        var controlUIFiveMile = document.createElement('div');
        controlUIFiveMile.style.backgroundColor = 'white';
        controlUIFiveMile.style.borderStyle = 'solid';
        controlUIFiveMile.style.borderWidth = '2px';
        controlUIFiveMile.style.cursor = 'pointer';
        controlUIFiveMile.style.textAlign = 'center';
        controlUIFiveMile.title = 'Click to include food vans within 5 Miles';
        controlUIFiveMile.id = '5-mile';
        controlDiv.appendChild(controlUIFiveMile);

        // Set CSS for the control interior.
        var controlTextFiveMile = document.createElement('div');
        controlTextFiveMile.style.fontFamily = 'Arial,sans-serif';
        controlTextFiveMile.style.fontSize = '12px';
        controlTextFiveMile.style.paddingLeft = '4px';
        controlTextFiveMile.style.paddingRight = '4px';
        controlTextFiveMile.innerHTML = '<strong>5 Mile</strong>';
        controlUIFiveMile.appendChild(controlTextFiveMile);

        google.maps.event.addDomListener(controlUIFiveMile, 'click', function() {
          self.refreshCollection(self.map.getCenter(),5);
        });

        // Set CSS for the control border.
        var controlUI = document.createElement('div');
        controlUI.style.backgroundColor = 'white';
        controlUI.style.borderStyle = 'solid';
        controlUI.style.borderWidth = '2px';
        controlUI.style.cursor = 'pointer';
        controlUI.style.textAlign = 'center';
        controlUI.title = 'Click to include all food vans';
        controlUI.id = 'all';
        controlDiv.appendChild(controlUI);

        // Set CSS for the control interior.
        var controlText = document.createElement('div');
        controlText.style.fontFamily = 'Arial,sans-serif';
        controlText.style.fontSize = '12px';
        controlText.style.paddingLeft = '4px';
        controlText.style.paddingRight = '4px';
        controlText.innerHTML = '<strong>All</strong>';
        controlUI.appendChild(controlText);

        google.maps.event.addDomListener(controlUI, 'click', function() {
          self.refreshCollection();
        });

        return controlDiv;
    }

});

