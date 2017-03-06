from __future__ import print_function
import os
import sys
import random

companies = ['Uber', 'Facebook', 'Twitter', 'YouTube', 'Foursquare',
             'Napster', 'Airbnb', 'Snapchat', 'Dropbox', 'Amazon',
             'LinkedIn', 'eBay', 'Groupon', 'Craigslist']
nouns = []

if os.path.isfile('nouns.txt'):
    with open('nouns.txt') as f:
        nouns = f.read().splitlines()
else:
    print('Nouns not found. Run getnouns.py first.')
    sys.exit(1)

def random_idea():
    return 'Like %s but for %s' % (random.choice(companies),
                                   random.choice(nouns))

if __name__ == '__main__':
    for _ in xrange(10):
        print(random_idea())
