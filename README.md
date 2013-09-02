Food Trucks for Uber: Mark Lakewood


What is this?
-------------

This is a coding challenge answer for Uber. I chose the Food trucks challenge found here:
    https://github.com/uber/coding-challenge-tools.
I've deployed this solution to heroku which can be found here:
    http://aqueous-citadel-9608.herokuapp.com/

I chose to use heroku, flask, SQLAlchemy, backbone.js and the google maps api v3.

I have only used Backbone.js in a production environment, although I have played around with the others in a non-production environment.


Restful Flask
-------------

The backend restful api has been built in flask, using SQLAlchemy as the ORM and sqlite as the database.

The database can be created using the create_db python script like so:
    $ python create_db.py

The data for the trucks can be then loaded into the database using the load_data.py script like so:
    $ python load_data.py

This script will remove all current rows from the sqlite database, download the data from https://data.sfgov.org/Permitting/Mobile-Food-Facility-Permit/rqzj-sfat and then load that data into the database.

Tests for the api can be run by excuting:
    $ python -m 'unittest' discover -vf

This is the report from coverage:

    $coverage run --include=food_trucks/* -m  'unittest' discover -vf

    $ coverage report -m
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
food_trucks/__init__                               2      0   100%
food_trucks/app                                   18      2    89%   34, 38
food_trucks/db                                    12      0   100%
food_trucks/exceptions                            18      0   100%
food_trucks/models/__init__                        0      0   100%
food_trucks/models/food_truck                     22      0   100%
food_trucks/resources/__init__                     0      0   100%
food_trucks/resources/base_resource               12      0   100%
food_trucks/resources/food_trucks_view            39      0   100%
food_trucks/tests/__init__                         0      0   100%
food_trucks/tests/models/__init__                  0      0   100%
food_trucks/tests/models/test_food_truck          25      0   100%
food_trucks/tests/resources/__init__               0      0   100%
food_trucks/tests/resources/test_food_trucks      68      0   100%
----------------------------------------------------------------------------
TOTAL                                            216      2    99%

The pyflakes log can be found in pyflakes.log. I normally use pylint, but I decided to try out pyflakes
this time around. I think overall in production code I would use pylint, as I think it checks many more
code attributes, and therefore as a team you can enforce them. 

The service can be run by executing:
    $ python food_trucks/runserver.py


Backbone.js
-----------

The Javascript side of things can be found in static/js. There is an app.js that contains the router. And
really only one view, the maps_views.js that renders the google map, and places the markers for the trucks.

This all works pretty well, as its a very small backbone.js app. I havent really worried to much about cleaning up memory at this point, as 

1) Its a prototype and so needs to be polished.
2) Its quite small so doesnt take up much memory in the first place.

Issues, things that could be done better
----------------------------------------

Flask:

    1) As I havent used Flask in a production environment I had to spend quite a bit of time getting it to work. As I chose a much more modular approach to setting out the service, I had a few issues laying out where things needed to go. I'm still not totally happy with the configuration with regards to the db.py, app.py and run_server.py. Specifically im not happy with the lack of external configuration file (ie like a settings.py file or someother format), and due to the way run_server.py is written, Heroku runs the Procfile fine in production but foreman has issues with it. So I feel that the base level of the stack needs some work.

    2) I did have an issue with a module stomping on my main package due to a naming clash that had me stumped for a while, which slowed me down quite a bit. But its not something I have come across before, but will be something I remember for quite a while.

    3) At the moment the loading of the data is a batch job. This could be improved to just proxy the source data, but as the data doesnt change that much, I think the load_data.py could for example be put in a cron job.

Backbone.js:
    
    1) The maps_view.js file might need to be broken up. The view itself is doing three seperate things. 
            1. Rendering the google maps
            2. Rendering the overlays
            3. Rendering the distance buttons on the side.
       These seem like jobs that should go in different views, but at this point it was easier to put it all in one view.

    2) It would be nice to have some extra information about what the food truck is. At the moment there is a tool tip for the name, that comes up if you hover over the marker. This is a minor addition, as we have the information we just need to surface it. But I decided that it was out of scope for a prototype, as normally a prototype is about fleshing out the big parts of 'how this is going to get done, and can we do it?', and it seemed that it wasnt essential in answering that question.

    3) Memory is a constant issue with client side single page apps. Mainly because we as developers are unused to caring about memory in HTML and javascript. Correct disposal of events, views, models and collections so that they can be garbage collected is critical in large single page applications. As mentioned above, I havent really worried about this as there arent really any transitions as such and we are working with not much data.

Timings:

    So it took quite a bit longer than the 4-5 hours suggested in the challenge. When looking at the challenge initially I didnt think the timeframe was realistic for myself. Due to having to standup an unfamiliar stack (although small) from scratch, and issues encountered along the way, its taken me probably 2 days elapsed time, but a day and a half actual time. This was about how long I estimated it would take me. So I believe that although I'm not in line with the estimate in the challenge I am accurate in estimating my own timeframes.



