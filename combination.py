#THIS IS THE HGNC AND UNIPROT DATA COMBINED
uni_dict = {}
hgnc_dict = {}
count = 0
with open('Uniprot_Data_table', 'r') as uni, open('HGNC_Data_table', 'r') as hgnc, open('preFinal_HGNCUNI_table', 'w') as out:
    for line in uni:
        line=line.rstrip()
        line=line.split('\t')
        uniprot = line[0]
        uni_dict[uniprot] = {}
        symbol = line[1]
        uni_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        uni_dict[uniprot]['synonym'] = synonym
        name = line[3]
        uni_dict[uniprot]['name'] = name
        luge = line[4]
        uni_dict[uniprot]['luge'] = luge
    for line in hgnc:
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        hgnc_dict[uniprot] = {}
        symbol = line[1]
        hgnc_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        hgnc_dict[uniprot]['synonym'] = synonym
        name = line[3]
        hgnc_dict[uniprot]['name'] = name
        luge = line[4]
        hgnc_dict[uniprot]['luge'] = luge
    for key in uni_dict:
        if key in hgnc_dict:
            print(key,uni_dict[key]['symbol']+','+hgnc_dict[key]['symbol'],uni_dict[key]['synonym']+','+ hgnc_dict[key]['synonym'], uni_dict[key]['name']+'|'+ hgnc_dict[key]['name'], hgnc_dict[key]['luge'], sep = '\t', file = out)
        else:
            print(key, uni_dict[key]['symbol'],uni_dict[key]['synonym'],uni_dict[key]['name'], uni_dict[key]['luge'], sep = '\t', file = out)
    for key in hgnc_dict:
        if not key in uni_dict:
            print(key,hgnc_dict[key]['symbol'], hgnc_dict[key]['synonym'], hgnc_dict[key]['name'], hgnc_dict[key]['luge'], sep = '\t', file = out)
            
        
import re
with open('preFinal_HGNCUNI_table', 'r') as pre, open('FULL_HGNCUNI_table', 'w') as full:
    for line in pre:
        line=line.rstrip().split('\t')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        name = line[3]
        name = name.splitlines()
        synonym = line[2]
        synonym = synonym.splitlines()
        luge = line[4]
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[,]', line))
        for line in name:
            line=line.rstrip()
            namelist = set(re.split('[|]', line)) 
        for line in synonym:
            line=line.rstrip()
            synonymlist = set(re.split('[,]', line))
        all_symbols = ','.join(str(x) for x in symbollist)
        all_name = ','.join(str(x) for x in namelist)
        all_synonym = ','.join(str(x) for x in synonymlist)
        print(uniprot,all_symbols,all_synonym,all_name,luge,sep = '\t', file = full)      
    
