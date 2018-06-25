#coding=utf-8
from SPARQLWrapper import SPARQLWrapper, JSON

imdb_sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
dbpedia_sparql = SPARQLWrapper("http://dbpedia.org/sparql/")

def sparql_runner(sparql=dbpedia_sparql, query=''):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def show_result_processing(results):
    finished_product = {}
    for item in results['head']['vars']:
        a = set()
        for row in results['results']['bindings']:
            a.add(row[item]['value'])
        finished_product[item] = a
    return finished_product


def recommand_result_processing(results):

    result_processed = {}
    for result in results["results"]["bindings"]:
        result_processed[result['name']['value']] = result['abstract']['value']
    print(result_processed)
    return result_processed


def movie_recommand_result_processing(results):
    result_processed = {}
    for result in results["results"]["bindings"]:
        result_processed[result['filmTitle']['value']] = result['page']['value']
    print(result_processed)
    return result_processed



def result_to_dict(results={}):
    finished_product = {}
    for item in results['head']['vars']:
        a = []
        for row in results['results']['bindings']:
            a.append(row[item]['value'])
        finished_product[item] = a
    return finished_product