#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Article

app = Flask(__name__)

engine = create_engine('sqlite:///vlogsite.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all categories
@app.route('/')
@app.route('/homepage/')
def homePage():
    categories = session.query(Category).all()
    #This page will show all categories
    return render_template('homepage.html', categories=categories)


# Show a list of all articles under a category
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/list/')
def showList(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    articles = session.query(Article).filter_by(
        category_id=category_id).all()
    return render_template('list.html', articles=articles, category=category)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
