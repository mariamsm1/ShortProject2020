#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO MERGE DATABASES AND COLLECT ALL POSSIBLE GENES RELATED TO Cell Death.
#
#---------------------------------

#mapped yCellDeath and mapped BCL2 (reviewed entries).
#first fix mapped files.
rev_dict = {}
apop_dict = {}
with open('ReviewedycellDeath_getProtname') as rev, open('TBU_yApoptosis') as apop, open('yApoptosis_final', 'w') as out:
    for line in rev:
        #take ids and protnames
        if not 'your' in line:
            line= line.rstrip()
            line=line.split('\t')
            uniprot = line[0]
            protname = line[4]
            rev_dict[uniprot] = protname
    for line in apop:
        if not 'Gene' in line:
            line = line.rstrip()
            line= line.split(';')
            uniprot = line[1]
            apop_dict[uniprot] = {}
            symbol = line[0]
            apop_dict[uniprot]['symbol'] = symbol
            synonym = line[2]
            apop_dict[uniprot]['synonym'] = synonym
    for key in apop_dict:
        if key in rev_dict:
            print(key,apop_dict[key]['symbol'],apop_dict[key]['synonym'],rev_dict[key], sep = '\t', file = out)
        else:
            print(key, apop_dict[key]['symbol'],apop_dict[key]['synonym'],'nan', sep = '\t', file = out)
  
  
syn_list = []
synonym_list = []
with open('Reviewed_cellDeath') as rev, open('cellDeath_final', 'w') as out:
    lines = rev.readlines()[1:]
    for line in lines:
        syn_list = []
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        protname = line[4]
        gsyn = line[5]
        org = line[6]
        symbol = gsyn.split(' ')[0]
        if symbol == '':
            symbol = 'nan'
        else:
            symbol = symbol
        synonym = gsyn.split(' ')[1:]
        synonym = ','.join(synonym)
        if synonym == '':
            synonym = 'nan'
            print(uniprot, symbol, synonym, protname, org, sep = '\t',file = out)
        else:
            print(uniprot, symbol, synonym, protname, org, sep = '\t',file = out)

#Merge the files above

dict_bcl = {}
dict_apop = {}
count = 0
with open('cellDeath_final') as bcl , open('yApoptosis_final') as apop, open('Overlap1_BclApop', 'w') as out:
    for line in bcl:
        if not 'Gene' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprotID = line[0]
            dict_bcl[uniprotID] = {}
            symbol = line[1]
            dict_bcl[uniprotID]['symbol'] = symbol
            alternative= line[2]
            dict_bcl[uniprotID]['alternative'] = alternative
            fullname = line[3]
            dict_bcl[uniprotID]['fullname'] = fullname
            org = line[4]
            dict_bcl[uniprotID]['org'] = org
    for line in apop:
        if not 'GeneName' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprot = line[0]
            dict_apop[uniprot] = {}
            symbol = line[1]
            dict_apop[uniprot]['symbol'] = symbol
            synonym = line[2].split('|')
            synonym = ','.join(synonym)
            dict_apop[uniprot]['synonym'] = synonym
            protname= line[3]
            dict_apop[uniprot]['protname'] = protname
            dict_apop[uniprot]['organism'] = "Saccharomyces cerevisiae (Baker's yeast)"
    for key in dict_bcl: 
        if key in dict_apop:
            print(key, dict_bcl[key]['symbol']+',' + dict_apop[key]['symbol'], dict_bcl[key]['alternative']+','+ dict_apop[key]['synonym'],dict_bcl[key]['fullname']+'|'+dict_apop[key]['protname'],dict_bcl[key]['org']+','+dict_apop[key]['organism'] ,sep = '\t', file = out)
        else:
            print(key,dict_bcl[key]['symbol'],dict_bcl[key]['alternative'],dict_bcl[key]['fullname'],dict_bcl[key]['org'], sep = '\t', file = out)
    for key in dict_apop:
        if not key in dict_bcl:
            print(key,dict_apop[key]['symbol'], dict_apop[key]['synonym'], dict_apop[key]['protname'], dict_apop[key]['organism'], sep = '\t', file = out)
#--------------------------------

#Merge Overlap1_BclApop and Final_deathbase
        
        
        
            
        
    
    
