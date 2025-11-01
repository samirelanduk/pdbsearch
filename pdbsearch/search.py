import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type):
    query = {
        "return_type": return_type,
    }
    response = requests.post(SEARCH_URL, json=query)
    return response.json()


def entries():
    return search("entry")


def polymer_entities():
    return search("polymer_entity")


def non_polymer_entities():
    return search("non_polymer_entity")


def polymer_instances():
    return search("polymer_instance")


def assemblies():
    return search("assembly")


def mol_definitions():
    return search("mol_definition")