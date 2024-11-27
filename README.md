# Django Push Notification

## STEPS
* [X] Create django project 
* [X] Create a django app `notification`
* [X] Migration data to database
* [X] Create a super user
* [X] Create a templates directory in `notification` app with `notification_page.html` inside it
* [X] create views for template
* [X] create urls for view and add it to rootURLconf
* [X] create models for `notification` app
* [X] define channels in setting file
* [X] Create Channel layers to handle our websockets by storin info
* [X] install `uvicorn[standard]` to handle async request using asgi
* [X] change directory to the rootconfig directory and type `uvicorn config.asgi:application --port 8000 --workers 4 --log-level debug --reload`
* [X] create urls to handle websocket connect and requests
* [X] create consumers to act as views and build it
* [X] create function to handle accepting and disconnecting and also pushing notification users 
* [X] add a context and template
* [X] modify admin template file for add_view
* [X] add channel layer to send notifications
* [X] add our custom url in `admin.py` for send message
* [X] create a client side to handle the websockets