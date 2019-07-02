import rdflib

g = rdflib.Graph().parse('data-flat.ttl', format='ttl')

all_rdf = []
i = 1
for s, p, o in g:
    rdf = '''
:s{}
    a rdf:Statement ;
    rdf:subject {} ;
    rdf:predicate {} ;
    rdf:object {} ;
    dct:created "2019-07-02"^^xsd:date ;
    loci:hadGenerationMethod :method ;
.'''.format(
        str(i).zfill(3),
        s.replace('https://data.naa.gov.au/def/agift/', 'agift:'),
        p.replace('http://www.w3.org/2004/02/skos/core#', 'skos:'),
        o.replace('http://linked.data.gov.au/def/cofog-a/', 'cofoga:')
    )
    all_rdf.append(rdf)

    i += 1

with open('../data.ttl', 'w') as f:
    f.write('\n'.join(all_rdf))
