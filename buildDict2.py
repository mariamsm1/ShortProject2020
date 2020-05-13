#!/usr/bin/env python3

import pickle
import regex as re
from protein2 import Protein


# Creates a unique ID for all proteins based on which species it is found in
def createID(prot, counter):
    species = 0
    if prot.species_id is not None:
        species = int(prot.species_id)
    return "LUGE" + "{:08d}".format(species) + "{:08d}".format(counter)


# Combines the proteins from the 2 dictionaries and removes any overlap
def combineDicts(combined, dataDict):
    for prot in dataDict:
        match = None
        IDs = []

        for ID in prot.uniprot_id:
            IDs.append(ID)
            if ID in combined:
                match = combined[ID]

        for ID in prot.hgnc_id:
            IDs.append(ID)
            if ID in combined:
                match = combined[ID]

        if match is not None:
            match.update(prot)

        for ID in IDs:
            if ID not in combined:
                combined[ID] = prot

def commaSeparate(strings):
    if not strings:
        return "<no value>"

    commaSeparated = ""
    for s in strings:
        commaSeparated += s + ","
    return commaSeparated[:-1]

def main():
    combinedNoID = {}

    uniprot = pickle.load(open("uniprot.out", "rb"))
    combineDicts(combinedNoID, uniprot)

    hgnc = pickle.load(open("hgnc.out", "rb"))
    combineDicts(combinedNoID, hgnc)

    counter = 0
    combined = {}
    for prot in combinedNoID.values():
        if prot.id is None:
            prot.id = createID(prot, counter)
            combined[prot.id] = prot
            counter += 1

    index = open("out/index.txt", "w+")
    for key,entry in combined.items():
        index.write(commaSeparate(entry.symbol) + "\t" + commaSeparate(entry.uniprot_id) + "\t" + commaSeparate(entry.names)+"\t"+commaSeparate(entry.genenames)+'\t'+key+ "\n")

if __name__ == "__main__":
    main()
