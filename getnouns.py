from nltk.corpus import wordnet
from pattern.en import pluralize

with open('nouns.txt', 'w') as ofile:
    for synset in wordnet.all_synsets(wordnet.NOUN):
        for lemma in synset.lemmas():
            word = lemma.name().replace('_', ' ')
            plural = pluralize(word)
            ofile.write(plural)
            ofile.write('\n')
