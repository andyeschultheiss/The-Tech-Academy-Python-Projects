## Functional Programming in Python
## Course on Real Python

## FP: Paradigm in which mainly immutable data structures are used, and side effects are avoided by using evaluation of mathematical functions for computation

## One way to store a table of scientists and simple bio info, use a dictionary
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': '1815', 'nobel': False },
    {'name': 'Emmy Noether', 'field': 'math', 'born': '1882', 'nobel': False },
]

## However, we can then easily access and modify the contents, and also have the issue of typos:
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': '1815', 'nobel': False },
    {'name': 'Emmy Noether', 'feild': 'math', 'born': '1882', 'nobel': False },  ## notice the typo for "field" here
]

## Additionally, we are repeating ourselves for each dictionary object, which is wasteful and leads back to typo issue above
## Instead, let's use collections.namedtuple

import collections
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

print(Scientist)

ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

print(ada.name)
print(ada.field)

## Can't reset attributes
## ada.name = 'Kath'

## okay, maybe we make a list of tuples then?

scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False)
]

## But we can still delete individual items from a list of tuples, so maybe we should make a tuple of tuples

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=False),
)

from pprint import pprint

pprint(scientists)

