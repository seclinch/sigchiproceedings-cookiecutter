# -*- coding: utf-8 -*-
import string

from jinja2.ext import Extension


def short_title(value):
    """Return the portion of a value string that preceeds the first
     occurance of `breaking` punctuation within that string. Breaking
     punctuation excludes quotes (which are removed from the string).

    >>> short_title("Hello! My name is 'Bob'.")
    'Hello'
    >>> short_title("One option remains: press on.")
    'One option remains'
    >>> short_title("How High?")
    'How High'
    >>> short_title("And this one has no punctuation at all")
    'And this one has no punctuation at all'
    """

    value = value.replace('"', '').replace("''", '')
    punctuation_indices = sorted([
        value.find(c) for c in string.punctuation if value.find(c) > -1
    ])
    for punctuation_index in punctuation_indices:
        value = value[:punctuation_index]
        break
    return value


def slug(value):
    """Returns a short, lowercase, hypen-separated string derived from value
    for use in filenames etc.

    >>> slug("Hello! My name is 'Bob'.")
    'hello'
    >>> slug("One option remains: press on.")
    'one-option-remains'
    >>> slug("How High?")
    'how-high'
    >>> slug("And this one has no punctuation at all")
    'and-this-one-has-no'
    """

    return truncate(short_title(value.lower())).replace(' ', '-')


def truncate(value, length=30, killwords=False, end='', leeway=0):
    """Return a truncated copy of the string. The length is specified with
    the `length` parameter which defaults to 30. If `killwords` is true,
    then the filter will cut the text at length. Otherwise it will discard
    the last word(s). The `end' parameter (default '') is appended to the
    end of any truncated string. Strings that only exceed the length by the
    tolerance margin given in the fourth parameter will not be truncated.

    >>> truncate("Hello! My name is 'Bob'.")
    "Hello! My name is 'Bob'."
    >>> truncate("One option remains: press on.", length=10)
    'One option'
    >>> truncate("How High?", length=8, end='...')
    'How...'
    >>> truncate("And this one has no punctuation at all", leeway=8)
    'And this one has no punctuation at all'
    """

    if len(value) <= length + leeway:
        return value

    if killwords:
        return value[:length-len(end)] + end

    rtn = ''
    for word in value.split(' '):
        tmp = rtn + " " + word
        if len(tmp) <= length-len(end):
            rtn = tmp.strip()
        else:
            break
    return rtn + end


class PaperTitleExtension(Extension):
    def __init__(self, environment):
        super(PaperTitleExtension, self).__init__(environment)
        environment.filters['short_title'] = short_title
        environment.filters['slug'] = slug
