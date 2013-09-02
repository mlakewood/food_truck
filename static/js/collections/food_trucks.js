var foodTruckCollection = Backbone.Collection.extend({
    model: foodTruckModel,
    url: '/food_trucks',
    parse: function(response){
        return response.items;
    }
})