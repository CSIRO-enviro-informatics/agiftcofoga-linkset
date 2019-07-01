import rdflib

g = rdflib.Graph().parse('data-flat.ttl', format='ttl')

LS = rdflib.Namespace('http://linked.data.gov.au/dataset/cofogcofoga/')
g.bind('ls', LS)
COFOGA = rdflib.Namespace('http://linked.data.gov.au/def/cofog/')
g.bind('cofoga', COFOGA)
COFOG = rdflib.Namespace('http://linked.data.gov.au/def/cofog-a/')
g.bind('cofog', COFOG)

all_rdf = []
i = 1
for s, p, o in g:
    rdf = '''
:s{}
    a rdf:Statement ;
    rdf:subject {} ;
    rdf:predicate {} ;
    rdf:object {} ;
    dct:created "2019-07-01"^^xsd:date ;
    loci:hadGenerationMethod ls_method: ;
.'''.format(
        str(i).zfill(3),
        s.replace('http://linked.data.gov.au/def/cofog-a/', 'cofoga:'),
        p.replace('http://www.w3.org/2004/02/skos/core#', 'skos:'),
        o.replace('http://linked.data.gov.au/def/cofog/', 'cofog:')
    )
    all_rdf.append(rdf)

    i += 1

with open('data.ttl', 'w') as f:
    f.write('\n'.join(all_rdf))
