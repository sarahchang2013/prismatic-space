from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Article


#edit this section and the txt file to update the article
embeded_code = 'https://www.youtube.com/embed/IJbnLlUYnuM'
title = "Why The Idea of a Space Nation is Challenging"
slug = "why-the-idea-of-a-space-nation-is-challenging"
article_id = 8



#store new text in a file with the new slug and read it
article_file = open (slug+".txt", "r")
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


# Update the article

editedArticle = session.query(Article).filter_by(id=article_id).one()
editedArticle.title = title
editedArticle.slug = slug
editedArticle.embeded_code = embeded_code
editedArticle.text = text

#must commit the transaction, otherwise the previous operations are not applied.
session.commit()

