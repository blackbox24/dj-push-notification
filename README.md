# Django Push Notification

## STEPS
[X] Create django project 
[X] Create a django app `notification`
[X] Migration data to database
[X] Create a super user
[X] Create a templates directory in `notification` app with `notification_page.html` inside it
[X] create views for template
[X] create urls for view and add it to rootURLconf
[X] create models for `notification` app
[X] define channels in setting file
[x] Create Channel layers to handle our websockets by storin info
[x] install `uvicorn[standard]` to handle async request using asgi
[X] change directory to the rootconfig directory and type `uvicorn config.asgi:application --port 8000 --workers 4 --log-level debug --reload`
[X] create urls to handle websocket connect and requests
[X] create consumers to act as views and build it