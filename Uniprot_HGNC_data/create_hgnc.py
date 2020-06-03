#hgncSYM_UNIPID, hgnc_uniID_Name, hgnc_uniID_SYNO are the files I generated from hgnc code. They contain the info in their names
#take the uniprot ID as a common field in these files to get symbols, synonyms, and names of the proteins.

count = 0
sym_dict = {}
syn_dict = {}
name_dict = {}
with open('hgncSYM_UniID', 'r') as sym, open('hgnc_uniID_SYNO', 'r') as syno, open('hgnc_uniID_Name', 'r') as name, open('UNISYM_hgncData1', 'w') as out:
    for line in sym:
        line=line.rstrip()
        line=line.split('\t')
        if not '<no value>' in line[0]:
            uniprot = line[0] #20218
            sym_dict[uniprot] = {}
            symbol = line[1] #20218
            sym_dict[uniprot]['symbol'] = symbol
            luge = line[2]
            sym_dict[uniprot]['organism'] = luge
    for line in syno:
        line=line.rstrip()
        line=line.split('\t')
        if not '<no value>' in line[0]:
            uniprot = line[0] #20218
            synonym = line[1] #20218
            syn_dict[uniprot] = synonym
    for line in name:
        line=line.rstrip()
        line=line.split('\t')
        if not '<no value>' in line[0]:
            uniprot = line[0] #20218
            name = line[1] #20218
            name_dict[uniprot] = name
    
    for key in sym_dict:
        if key in syn_dict:
            print(key, sym_dict[key]['symbol'], syn_dict[key], sym_dict[uniprot]['organism'], sep = '\t', file = out)
        else:
            print(key, sym_dict[key]['symbol'], '<no value>', sym_dict[uniprot]['organism'], sep = '\t', file = out)

            
            
#find the overlap/non overlap with name_dict
#names in the output file are ';' delimited
data_dict = {}
with open('UNISYM_hgncData1', 'r') as data, open('HGNC_Data_table', 'w') as output:
    for line in data:
        line=line.rstrip()
        line=line.split('\t')
        uniprot = line[0]
        data_dict[uniprot] = {}
        symbol = line[1]
        data_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        data_dict[uniprot]['synonym'] = synonym
        organism = line[3]
        data_dict[uniprot]['organism'] = organism
    for key in data_dict:
        if key in name_dict:
            print(key,data_dict[key]['symbol'],data_dict[key]['synonym'],name_dict[key], data_dict[key]['organism'], sep = '\t', file = output)
        else:
            print(key, data_dict[key]['symbol'],data_dict[key]['synonym'],'<now value>', data_dict[key]['organism'], sep = '\t', file = output)#20083
            
        
