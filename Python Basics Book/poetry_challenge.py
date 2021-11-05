from random import choice
nouns = ["fossil","horse","aardvark","judge","chef","mango","extrovert","gorilla"]
verbs = ["kicks","jingles","bounces","slurps","meows","explodes","curdles"]
adjectives = ["furry","balding","incredulous","fragrant","exuberant","glistening"]
prepositions = ["against","after","into","beneath","upon","for","in","like","over","within"]
adverbs = ["curiously","extravagantly","tantalizingly","furiously","sensuously"]


poem_format = ['A/An', 'adj1', 'noun1',
'A/An', 'adj1', 'noun1', 'verb1', 'prep1', 'the', 'adj2', 'noun2',
'adverb1', 'the', 'noun1', 'verb2',
'the', 'noun2', 'verb3', 'prep2', 'a', 'adj3', 'noun3']

def make_poem():
    # loop over the poem format list and if it matches any of the randoms that need to be
    # choosen then choose and replace the old value.
    for i in range(len(poem_format)):
    #print(poem_format[i].find('verb'))
        if poem_format[i] == 'A/An':
            poem_format[i] = choice(['A','An'])
        if poem_format[i].find('noun') == 0:
            poem_format[i] = choice(nouns)
        if poem_format[i].find('verb') == 0:
            poem_format[i] = choice(verbs)
        if poem_format[i].find('adj') == 0:
            poem_format[i] = choice(adjectives)
        if poem_format[i].find('prep') == 0:
            poem_format[i] = choice(prepositions)
        if poem_format[i].find('adv') == 0:
            poem_format[i] = choice(adverbs)


    return (f' {" ".join(poem_format[0:3])} \n\n {" ".join(poem_format[3:12])} \n {" ".join(poem_format[12:17])} \n {" ".join(poem_format[17:25])}')

poem = make_poem()
print(poem)


