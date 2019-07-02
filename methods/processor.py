import rdflib


AGIFT = {}
COFOG_A = {}
cleaning_pairs = [
    (' and ', ' '),
    (' of ', ' '),
    (' not ', ' '),
    (' to ', ' '),
    (' in ', ' '),
    (' - ', ' '),
    ("'", ''),
    (',', ''),
    ('(', ''),
    (')', ''),
]


# replaces all the first item in a list of pairs of items with the second, for all occurrences in text
def replace_all(text, pairs):
    for p in pairs:
        text = text.replace(p[0], p[1])
    return text


# loads AGIFT into a Python dict
def load_agift():
    global AGIFT
    g2 = rdflib.Graph().parse('../imports/agift.ttl', format='ttl')

    # get all concepts and prefLabels, in English
    q2 = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            ?c  a skos:Concept ;
                skos:prefLabel ?pl .
            FILTER langMatches( lang(?pl), "en" )
        }
        ORDER BY ?pl
    '''

    # load all Concepts and prefLabels into a dict for comparison
    AGIFT = {}
    for r in g2.query(q2):
        # print('{}, {}'.format(str(r['s']), r['pl']))
        clean_uri = str(r['c']).rstrip('-_2')  # stripping off junk URI trailing chars
        simple_pl = replace_all(str(r['pl']), cleaning_pairs).lower()
        AGIFT[clean_uri] = {
            'pl': str(r['pl']),
            'pl_clean': simple_pl
        }


# loads COFOG-A into a Python dict
def load_cofog_a():
    global COFOG_A
    g2 = rdflib.Graph().parse('../imports/cofog-a.ttl', format='ttl')

    # get all concepts and prefLabels, in English
    q2 = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            ?c  a skos:Concept ;
                skos:prefLabel ?pl .
            FILTER langMatches( lang(?pl), "en" )
        }
        ORDER BY ?pl
    '''

    # load all Concepts and prefLabels into a dict for comparison
    COFOG_A = {}
    for r in g2.query(q2):
        simple_pl = replace_all(str(r['pl']), cleaning_pairs).lower()
        COFOG_A[str(r['c'])] = {
            'pl': str(r['pl']),
            'pl_clean': simple_pl
        }


# just gives a count of the words-per-prefLabel matching
# results in 5,000+ matches, mostly irrelevant
def first_pass_matcher(d1, d2):
    lines = []
    # use the clean pls for matching with but print out the original pls for human matching
    for uri1, v1 in d1.items():
        words1 = v1['pl_clean'].split(' ')
        for uri2, v2 in d2.items():
            words2 = v2['pl_clean'].split(' ')

            match_count = 0
            for w in words1:
                if w in words2:
                    match_count += 1

            if match_count > 0:
                lines.append('{}#{}#{}#{}#{}'.format(uri1, uri2, match_count, v1['pl'], v2['pl']))

    with open('matches.csv', 'w') as f:
        f.write('\n'.join(lines))


# Python code methods
#   all functions from this file
load_agift()
load_cofog_a()

first_pass_matcher(AGIFT, COFOG_A)


# Excel Methods
'''
Place all matches into Excel
Sort by word match count
Manually review all matches
    5,000 matches reduced to ~250
'''