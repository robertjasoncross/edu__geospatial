# Chapter 13
# __init__.py
# by Silas Toms
#
# This script initiates the Arena application's app controler and 
# configures the connection to database tables 

#
#
import flask
app = flask.Flask(__name__)
conn_string = 'postgresql://postgres:postgres@localhost:5432/ch12'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string	
app.config['SECRET_KEY'] = "SECRET_KEY"
import application.views
