from nltk.corpus import wordnet
from pattern.en import pluralize

with open('nouns.txt', 'w') as ofile:
    words = set(lemma.name().replace('_', ' ')
                for synset in wordnet.all_synsets(wordnet.NOUN)
                for lemma in synset.lemmas())
    for word in sorted(words):
        plural = pluralize(word)
        if plural.endswith('ss'):
            ofile.write(word)
        else:
            ofile.write(plural)
        ofile.write('\n')
