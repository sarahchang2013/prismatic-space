
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Article




#edit this section and the txt file
category_of_article = "Science and Technology"
embeded_code = 'https://www.youtube.com/embed/IJbnLlUYnuM'
title = "Why the Idea of a Space Nation is Challenging"
slug = "why-the-idea-of-a-space-nation-is-challenging"




#store text in a file and read it
article_file = open ("new_article.txt", "r")
#string was utf-8 encoded, so decode it to store in database
text=article_file.read().decode('utf-8')

engine = create_engine('sqlite:///vlogsite.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Articles for Science and Technology
category1 = Category(name=category_of_article)

session.add(category1)
session.commit()

article1 = Article(title=title, slug=slug,embeded_code=embeded_code, text=text, category=category1)

session.add(article1)
session.commit()

