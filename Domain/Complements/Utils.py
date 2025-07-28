import json
from dateutil.parser import parse
from sqlalchemy.orm import class_mapper


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def json_data_match(json_data=None, key=None, value=None):
    result = False
    if json_data.get(key, '') != '':
        result = json_data.get(key) == value
    return result

def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]

    #del columns['fecha_creacion']
    # then we return their values in a dict
    result= dict((c, getattr(model, c)) for c in columns)

    return result
