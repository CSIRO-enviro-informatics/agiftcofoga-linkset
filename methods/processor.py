import rdflib
import Levenshtein

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


# loads COFOG-A into a Python dict
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


load_agift()
load_cofog_a()

first_pass_matcher(AGIFT, COFOG_A)

# FOR TESTING
# COFOG_A = {
#     'http://linked.data.gov.au/def/cofog-a/01': {'pl': 'General Public Services'},
# }

# loop through AGIFT
#   for each Concept's prefLabel
#       remove a set of useless words and characters ['and', ' - ', ',']
#       compute the L distance to each Concept in COFOG's prefLabel, useless stuff removed too
#       store each URI of COFOG-A concepts in an ordered array (Python list), smallest to largest distance

# for c, v in COFOG_A.items():
#     distances = []  # to store the distance from this COFOG-A item to each COFOG item
#     pl_clean = replace_all(v['pl'], cleaning_pairs).lower()
#
#     for c2, v2 in COFOG.items():
#         pl2_clean = replace_all(v2['pl'], cleaning_pairs).lower()
#         d = Levenshtein.distance(pl_clean, pl2_clean)
#         distances.append((c2, d, v2['pl']))
#
#     # order the distances, smallest to largest
#     distances.sort(key=lambda tup: tup[1])
#
#     COFOG_A[c]['distances'] = distances
#
# # get matches of a certain distance
# with open('matches.csv', 'w') as f:
#     for c, v in COFOG_A.items():
#         for d in v['distances']:
#             if d[1] < 5:
#                 # use hash to separate files as there are commas in text
#                 f.write('{}#{}#{}#{}#{}\n'.format(c, v['pl'], d[0], d[2], d[1]))



# Excel Methods
'''
Place all matches into Excel
Sort by L distance
Considering all 0-length latches:
    Remove only cross level duplicates (e.g. 01 == 010 if also 01 == 01)
    
Considering all 1+ length matches:
    Manually removed obvious errors (there weren't too many)
'''