


import nltk
from nltk import induce_pcfg
from nltk.corpus import treebank
from nltk.parse import pchart
from nltk import CFG
from nltk import treetransforms
from nltk import Nonterminal
import pickle



productions = []
for item in treebank.fileids()[:]:
    for tree in treebank.parsed_sents(item):
        tree.collapse_unary(collapsePOS = False)# Remove branches A-B-C into A-B+C
        tree.chomsky_normal_form(horzMarkov = 2)# Remove A->(B,C,D) into A->B,C+D->D
        productions += tree.productions()

lhs_prod = [p.lhs() for p in productions]
rhs_prod = [p.rhs() for p in productions]
set_prod = set(productions)


prod = list(set_prod)
token_rule = []
for item in prod:
    if item.is_lexical():
        token_rule.append(item)


list_of_rules = []
set_tok_rule = set(p.lhs() for p in token_rule)
tok_rule = list(set_tok_rule)
for word in tok_rule:
    if str(word).isalpha():
        list_of_rules.append(word)
        continue
print(list_of_rules)



temp = []
for rule in list_of_rules:
    lhs = 'UNK'
    rhs = [u'UNK']
    UNK_production = nltk.grammar.Production(lhs, rhs)   
    lhs2 = nltk.grammar.Nonterminal(str(rule))
    temp.append(nltk.grammar.Production(lhs2, [lhs]))

    
#Adding UNK to token rules
token_rule.extend(temp)
prod.extend(temp)


#Inducing Probabilities and generating grammar


S = Nonterminal('S')
grammar = induce_pcfg(S,prod)

pickle.dump(grammar, open("PCFG", 'wb'))

