git push heroku master
heroku ps:scale web=0 clock=1
heroku ps
heroku logs --tail
