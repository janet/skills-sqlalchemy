"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == "1903", Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(128)

# Get any model whose brand_name is not Chevrolet.
# db.session.query(Model.name, Brand.name).join(Brand).filter(Model.brand_name != 'Chevrolet').all()
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    list_of_tuples = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year)

    for m_name, m_brand_name, b_headquarters in list_of_tuples:
    	print m_name, m_brand_name, b_headquarters

def get_brands_summary(brand_name):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     list_of_tuples = db.session.query(Model.name, Model.brand_name).filter(Model.brand_name == brand_name)

     for m_name, m_brand_name in list_of_tuples:
     	print m_name, m_brand_name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
	""" takes in any string as parameter, and returns a list of objects that are brands
	whose name contains or is equal to the input string."""

	return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()

def get_models_between(start_year, end_year):
	""" takes in a start year and end year (two integers), and returns a list of objects
	that are models with years that fall between the start year and end year."""

	return Model.query.filter(Model.year > start_year, Model.year < end_year).all()

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

""" returned value <flask_sqlalchemy.BaseQuery object at 0x108a5db50>
It is the query object and asks the question: "What are the brands with name 'Ford'? """

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

"""  """


