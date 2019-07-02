# AGIFT / COFOG-A Linkset
This code repository contains a Linkset - a specialised Dataset linking objects in two other Datasets.

This Linkset contains [SKOS mapping properties](https://www.w3.org/TR/skos-reference/#mapping) between Concepts in the [AGIFT](http://data.naa.gov.au/def/agift) and Concepts in the [COFOG-A](http://linked.data.gov.au/def/cofog) vocabularies.

AGIFT, "Australian Governments' Interactive Functions Thesaurus", from the [National Archives of Australia (NAA)](http://www.naa.gov.au), is a "three-level hierarchical thesaurus that describes the business functions carried out across Commonwealth, state and local governments in Australia".

The COFOG-A is an Australian version of the UN's Statistical office's COFOG, "Classification of the Functions of Government", issued by the from the [Australian Bureau of Statistics](http://www.abs.gov.au) in the [Australian System of Government Finance Statistics: Concepts, Sources and Methods](http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/418BDDEBD088A012CA257F230019D433/$File/55140_2015.pdf) which is represented as a SKOS vocabulary online at <http://linked.data.gov.au/def/cofog-a>.


## Linkset relations
This Linkset uses only [SKOS Mapping Properties](https://www.w3.org/TR/skos-reference/#mapping) to map between AGIFT & COFOG-A. Only the following properties are used:

* `skos:closeMatch`
* `skos:exactMatch`
* `skos:broadMatch`
* `skos:narrowMatch`
* `skos:relatedMatch`

See [example-data-unreified.ttl](example-data-unreified.ttl) for 5 simple examples from the Linkset or [example-data.ttl](example-data.ttl) for the same 5 examples presented in *reified* form, that is with per-link metadata, such as time of creation and method used.


## Repository Contents
This repository contains the following files and folders:

* [README.md](README.md) - this file
* [imports/](imports/) - background information: the AGIFT & COFOG-A vocabularies as RDF (turtle) files
* [data.ttl](data.ttl) - this Linkset's links as an RDF (turtle) file
* [header.ttl](header.ttl) - this Linkset’s data.ttl header information, stored separately for ease of access
* [example-data.ttl](example-data.ttl) - 5 Statements from the Linkset for ease of access, in RDF (turtle) format, as per the main data file but none of the whole-of-Linkset information
* [example-data-unreified.ttl](example-data-unreified.ttl) - 5 Statements from the Linkset but flattened, 'unreified', for even easier use
* [methods/](methods/) - a folder containing the notes, scripts (Python) and interim data used to create this Linkset


## Rights & License
The content of this repository is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) all details.

Please note:

The content of AGIFT itself is taken directly from the NAA's delivery of AGIFT at <http://data.naa.gov.au/def/agift>.

The content of COFOG-A itself is derived from the [Australian Bureau of Statistics](http://www.abs.gov.au)' [Australian System of Government Finance Statistics: Concepts, Sources and Methods](http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/418BDDEBD088A012CA257F230019D433/$File/55140_2015.pdf).


## Contacts
*Technical contact:*  
**Nicholas Car**  
CSIRO Land & Water, Environmental Informatics Group  
<nicholas.car@csiro.au>  