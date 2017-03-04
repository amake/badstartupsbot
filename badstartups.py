from __future__ import print_function
import os
import random

nouns = []

if os.path.isfile('nouns.txt'):
    with open('nouns.txt') as f:
        nouns = f.read().splitlines()
else:
    print('Nouns not found. Run getnouns.py first.')
    exit(1)

def random_idea():
    return 'Like Uber but for %s' % random.choice(nouns)

if __name__ == '__main__':
    for _ in xrange(10):
        print(random_idea())
