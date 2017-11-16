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
    articles = session.query(Article).order_by(Article.id.desc()).limit(20).all()
    #This page will show all categories
    return render_template('homepage.html', articles=articles)


# Show a page of the selected article
@app.route('/category/<int:category_id>/<int:article_id>/<string:slug>/')
def showArticle(category_id, article_id, slug):
    category = session.query(Category).filter_by(id=category_id).one()
    article = session.query(Article).filter_by(id=article_id).one()
    return render_template('article.html', article=article, category=category)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
