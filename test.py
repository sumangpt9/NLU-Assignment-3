

import sys
import pickle
pickle_in = open("PCFG","rb")
grammar = pickle.load(pickle_in)


# CKY Algo

import sys
from nltk.parse import ViterbiParser
from nltk import tokenize
from nltk.parse import pchart




# Tokenize the sentence.
tokens=sys.argv[1:]

parser = ViterbiParser(grammar)


# Replacing unknown words with UNK....

replace_with_UNK_token = []
for i,item in enumerate(tokens):
    try:
        grammar.check_coverage([item])
    except:
        replace_with_UNK_token.append(tokens[i])
        tokens[i] = 'UNK'


trees = parser.parse_all(tokens)
for tree in trees:
    pass



UNK_str = tree.__str__()

output_parse= UNK_str
for i in replace_with_UNK_token:
    output_parse = output_parse.replace("UNK",i,1)
    
print(output_parse)

