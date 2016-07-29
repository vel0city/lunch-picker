# README #

This app connects to Yelp and grabs a random restaurant and announces the lunch pick through Hipchat's API. Useful to put on a cron job just before the lunch rush to settle any question about where to go to lunch. Saves hundreds of hours of debate of where a team should go to lunch. Improves morale by removing said debate.

Let /dev/urandom control your life. Maybe just a little. What could go wrong?

### HOW TO RUN ###
Grab a HipChat token for whatever room you want to announce the lunch choice from your group admin. You'll also need to know the room ID.

Get Yelp API credentials:
https://www.yelp.com/developers/manage_api_keys

Build the docker container:
`docker build -t lunch_picker .`

Run the docker container:
`docker run --rm --env-file example_env lunch_picker`

Put it in on a cron job to run Monday through Friday at 10:30AM:
```
crontab -e
30 10 * * MON-FRI docker run --env-file /path/to/example_env --rm lunch_picker
```


### ENV File Options ###
The env file has a lot of self explanatory options. Some non-obvious ones are:

#### SEARCH_RADIUS ####
Pretty straight forward. In meters.

#### SEARCH_OFFSET ####
Yelp's API returns 20 results. So, we randomly choose an offset from 0 to this value to move the window of 20 choices.


### External Sites ###
Categories are listed on the Yelp's API documentation here:
https://www.yelp.com/developers/documentation/v2/category_list

Documentation on the Python Yelp API can be found here:
https://github.com/Yelp/yelp-python

### Contribution guidelines ###

* Acknowledge the power of the lunch dictator
* Stay strong comrade, your lunch choice will rise soon.
