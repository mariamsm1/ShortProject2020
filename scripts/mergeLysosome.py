#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO MERGE DATABASES AND COLLECT ALL POSSIBLE GENES RELATED TO Lysosome.
#
#---------------------------------

# Uniprot/subcellular-Lysosome and mapped to uniprot Human Lysosome Gene database(HLGdb)
#first fix structure of mapped HLGdb

syn_list = []
synonym_list = []
count = 0
with open('mappedToUni_HLGB.tab', 'r') as mapp, open('synonyms_HLGB', 'w') as out, open('prefinal_HLGB', 'w') as pre:
    lines = mapp.readlines()[1:]
    for line in lines:
        syn_list = []
        line = line.rstrip()
        line=line.split('\t')
        uniprot = line[1]
        protname= line[4].replace(';', ',')
        org = line[6]
        gsyn = line[5].replace(' ', ',').split(',')
        symbol = gsyn[0]
        print(uniprot, symbol, protname, org, sep = ';', file = pre)
        synonym = gsyn[1:]
        for element in synonym:
            syn_list.append(element)
            synonym = ','.join(syn_list)
        synonym_list.append(synonym)         
    synonym_list = ["nan" if x == [] else x for x in synonym_list] #remove [] from the list
    for element in synonym_list:
        print(element, file = out)
        
#paste -d ';' prefinal_HLGB synonyms_HLGB > mappedToUni_HumanLGDB       


tbu_dict = {}
dict_mapp = {}
count = 0
with open('TBU_Lysosome_Uniprot') as tbu, open('mappedToUni_HumanLGDB') as mapp, open('over_lysUni_mapp', 'w') as out:
    for line in tbu:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        tbu_dict[uniprotID] = {}
        symbol = line[1]
        tbu_dict[uniprotID]['symbol'] = symbol
        alternative= line[4]
        tbu_dict[uniprotID]['alternative'] = alternative
        org = line[3]
        tbu_dict[uniprotID]['org'] = org
        fullname = line[2]
        tbu_dict[uniprotID]['fullname'] = fullname
    for line in mapp:
        line=line.rstrip()
        line=line.split(';')
        Uniprot = line[0]
        dict_mapp[Uniprot] = {}
        Symbol = line[1]
        dict_mapp[Uniprot]['Symbol'] = Symbol
        synonym= line[4]
        dict_mapp[Uniprot]['Synonym'] = synonym
        protname = line[2]
        dict_mapp[Uniprot]['protname'] = protname
        org_ID = line[3]
        dict_mapp[Uniprot]['organism'] = org_ID 
    for key in dict_mapp:
        if key in tbu_dict:
            print(key, dict_mapp[key]['Symbol']+','+tbu_dict[key]['symbol'], tbu_dict[key]['alternative']+','+dict_mapp[key]['Synonym'], tbu_dict[key]['fullname']+'|'+dict_mapp[key]['protname'], dict_mapp[key]['organism']+','+tbu_dict[key]['org'],sep = ';', file = out)
        else:
            print(key,dict_mapp[key]['Symbol'],dict_mapp[key]['Synonym'],dict_mapp[key]['protname'],dict_mapp[key]['organism'],sep = ';', file = out)            
    for key in tbu_dict:
        if not key in dict_mapp:
            print(key,tbu_dict[key]['symbol'],tbu_dict[key]['alternative'],tbu_dict[key]['fullname'],tbu_dict[key]['org'], sep = ';', file = out)
    
        
import re
with open('over_lysUni_mapp', 'r') as over, open('Overlap1_lysUni', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        name = name.splitlines()
        for line in alt:
            line=line.strip()
            synonymlist = set(re.split('[,]', line))
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[,]', line))
        for line in org:
            line=line.rstrip()
            orglist = set(re.split('[,]', line)) 
        for line in name:
            line=line.rstrip()
            namelist = set(re.split('[|]', line)) 
            #I could have put x without str as well.
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,all_org, sep = ';', file = out2)       
#--------------------------

#Mapped Protein Atlas to uniprot and Overlap1_lysUni
#first fix structure of mapped Protein Atlas to uniprot
synonym_list = []
syn_list = []
count=0
with open('Reviewed_proteinAtlasFull') as rev, open('prefinalProtein_Atlas', 'w') as out, open('synonyms_proteinAtlas', 'w') as out2:
    for line in rev:
        syn_list = []
        if not 'your' in line:
            line = line.rstrip()
            line=line.split('\t')
            uniprot = line[1]
            protname= line[4].replace(';', ',')
            org = line[6]
            gsyn = line[5].replace(' ', ',').split(',')
            symbol = gsyn[0]
            print(uniprot, symbol, protname, org, sep = ';', file = out)
            synonym = gsyn[1:]
            for element in synonym:
                syn_list.append(element)
                synonym = ','.join(syn_list)
            synonym_list.append(synonym)   
        synonym_list = ["nan" if x == [] else x for x in synonym_list] #remove [] from the list
    for element in synonym_list:
        print(element, file = out2)
        
 #paste -d ';' prefinalProtein_Atlas synonyms_proteinAtlas > ProteinAtlasForMerge    
  
        
dict_over = {}
dict_mer = {}
count = 0
with open('Overlap1_lysUni') as over, open('ProteinAtlasForMerge') as mer, open('overHLG', 'w') as out:
    for line in over:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_over[uniprotID] = {}
        symbol = line[1]
        dict_over[uniprotID]['symbol'] = symbol
        alternative= line[2]
        dict_over[uniprotID]['alternative'] = alternative
        org = line[4]
        dict_over[uniprotID]['org'] = org
        fullname = line[3]
        dict_over[uniprotID]['fullname'] = fullname
    for line in mer:
        line=line.rstrip()
        line=line.split(';')
        Uniprot = line[0]
        dict_mer[Uniprot] = {}
        Symbol = line[1]
        dict_mer[Uniprot]['Symbol'] = Symbol
        synonym= line[4]
        dict_mer[Uniprot]['Synonym'] = synonym
        protname = line[2]
        dict_mer[Uniprot]['protname'] = protname
        org_ID = line[3]
        dict_mer[Uniprot]['organism'] = org_ID 
    for key in dict_mer:
        if key in dict_over:
            print(key, dict_mer[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative']+','+dict_mer[key]['Synonym'], dict_over[key]['fullname']+'|'+dict_mer[key]['protname'], dict_mer[key]['organism']+','+dict_over[key]['org'],sep = ';', file = out)
        else:
            print(key,dict_mer[key]['Symbol'],dict_mer[key]['Synonym'],dict_mer[key]['protname'],dict_mer[key]['organism'],sep = ';', file = out)            
    for key in dict_over:
        if not key in dict_mer:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    
    
with open('overHLG', 'r') as over, open('Overlap2_atlas', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        name = name.splitlines()
        for line in alt:
            line=line.strip()
            synonymlist = set(line.split(','))
        for line in symbol:
            line=line.rstrip()
            symbollist = set(line.split(','))
        for line in org:
            line=line.rstrip()
            orglist = set(line.split(',')) 
        for line in name:
            line=line.rstrip()
            namelist = set(line.split('|')) 
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,all_org, sep = ';', file = out2)       
#--------------------------

# Overlap2_atlas and HeLa Spatial Proteome

dict_over = {}
dict_tbu = {}
count = 0
with open('TBU_ALL_HSP') as tbu, open('Overlap2_atlas') as over, open('overHSP','w') as out:
    for line in over:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_over[uniprotID] = {}
        symbol = line[1]
        dict_over[uniprotID]['symbol'] = symbol
        alternative= line[2]
        dict_over[uniprotID]['alternative'] = alternative
        org = line[4]
        dict_over[uniprotID]['org'] = org
        fullname = line[3]
        dict_over[uniprotID]['fullname'] = fullname
    for line in tbu:
        if not 'ProteinName' in line:
            line=line.rstrip()
            line=line.split(';')
            uniprot = line[0]
            dict_tbu[uniprot] = {}
            symbol = line[2]
            dict_tbu[uniprot]['symbol'] = symbol
            protname= line[1]
            dict_tbu[uniprot]['protname'] = protname
    for key in dict_over:
        if key in dict_tbu:
            print(key, dict_over[key]['symbol']+',' + dict_tbu[key]['symbol'], dict_over[key]['alternative'],dict_over[key]['fullname']+'|'+dict_tbu[key]['protname'],dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    for key in dict_tbu:
        if not key in dict_over:
            print(key,dict_tbu[key]['symbol'], 'nan', dict_tbu[key]['protname'], 'Homo sapiens (Human)', sep = ';', file = out)
            
            
with open('overHSP', 'r') as over, open('Overlap3_hsp', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        org = line[4]
        name = line[3]
        name = name.splitlines()
        for line in symbol:
            line=line.rstrip()
            symbollist = set(line.split(','))
        for line in name:
            line=line.rstrip()
            namelist = set(line.split('|')) 
        all_symbols = ','.join(str(x) for x in symbollist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,alt,all_names,org, sep = ';', file = out2)       
#-------------------------------

#Overlap3_hsp and mapped gene ontology/Lysosome

dict_over = {}
dict_clean = {}
count = 0
with open('clean_TBU_New_lysosome') as clean, open('Overlap3_hsp') as over, open('overclean','w') as out:
    for line in over:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_over[uniprotID] = {}
        symbol = line[1]
        dict_over[uniprotID]['symbol'] = symbol
        alternative= line[2]
        dict_over[uniprotID]['alternative'] = alternative
        org = line[4]
        dict_over[uniprotID]['org'] = org
        fullname = line[3]
        dict_over[uniprotID]['fullname'] = fullname
    for line in clean:
        line=line.rstrip()
        line=line.split(';')
        uniprot = line[0]
        dict_clean[uniprot] = {}
        symbol = line[1]
        dict_clean[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_clean[uniprot]['synonym'] = synonym
        protname= line[3]
        dict_clean[uniprot]['protname'] = protname
        organism = line[4]
        dict_clean[uniprot]['organism'] = organism
    for key in dict_over:
        if key in dict_clean:
            print(key, dict_over[key]['symbol']+',' + dict_clean[key]['symbol'], dict_over[key]['alternative']+','+ dict_clean[key]['synonym'],dict_over[key]['fullname']+'|'+dict_clean[key]['protname'],dict_over[key]['org']+','+dict_clean[key]['organism'], sep = ';', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    for key in dict_clean:
        if not key in dict_over:
            print(key,dict_clean[key]['symbol'], dict_clean[key]['synonym'], dict_clean[key]['protname'], dict_clean[key]['organism'], sep = ';', file = out)

import re
with open('overclean', 'r') as over, open('Overlap4_clean', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        name = name.splitlines()
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[|,]', line))
        for line in alt:
            line=line.rstrip()
            altlist = set(re.split('[|,]', line))
        for line in name:
            line=line.rstrip()
            namelist = set(line.split('|')) 
        for line in org:
            line = line.rstrip()
            orglist = set(line.split(',')) 
        all_symbols = ','.join(str(x) for x in symbollist)
        all_alt = ','.join(str(x) for x in altlist)
        all_names = '|'.join(str(x) for x in namelist)
        all_org = ','.join(str(x) for x in orglist)
        print(uniprot,all_symbols,all_alt,all_names,all_org, sep = ';', file = out2)       
#----------------------------

#merge mapped gene ontology/lysosome (Amigo search of entries with uniprot IDs) and Overlap4_clean

dict_over = {}
dict_clean = {}
with open('Overlap4_clean') as over , open('Clean_UniprotAmigo_Lysosome') as clean, open('overAmigo', 'w') as out:
    for line in over:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_over[uniprotID] = {}
        symbol = line[1]
        dict_over[uniprotID]['symbol'] = symbol
        alternative= line[2]
        dict_over[uniprotID]['alternative'] = alternative
        org = line[4]
        dict_over[uniprotID]['org'] = org
        fullname = line[3]
        dict_over[uniprotID]['fullname'] = fullname
    for line in clean:
        line=line.rstrip()
        line=line.split(';')
        uniprot = line[0]
        dict_clean[uniprot] = {}
        symbol = line[1]
        dict_clean[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_clean[uniprot]['synonym'] = synonym
        protname= line[3]
        dict_clean[uniprot]['protname'] = protname
        organism = line[4]
        dict_clean[uniprot]['organism'] = organism
    for key in dict_over:
        if key in dict_clean:
            print(key, dict_over[key]['symbol']+',' + dict_clean[key]['symbol'], dict_over[key]['alternative']+','+ dict_clean[key]['synonym'],dict_over[key]['fullname']+'|'+dict_clean[key]['protname'],dict_over[key]['org']+','+dict_clean[key]['organism'], sep = ';', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    for key in dict_clean:
        if not key in dict_over:
            print(key,dict_clean[key]['symbol'], dict_clean[key]['synonym'], dict_clean[key]['protname'], dict_clean[key]['organism'], sep = ';', file = out)

import re
with open('overAmigo', 'r') as over, open('Overlap5_clean', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        name = name.splitlines()
        for line in symbol:
            line=line.rstrip()
            symbollist = set(line.split(','))
        for line in alt:
            line=line.rstrip()
            altlist = set(line.split(','))
        for line in name:
            line=line.rstrip()
            namelist = set(line.split('|')) 
        for line in org:
            line = line.rstrip()
            orglist = set(line.split(','))
        all_symbols = ','.join(str(x) for x in symbollist)
        all_alt = ','.join(str(x) for x in altlist)
        all_names = '|'.join(str(x) for x in namelist)
        all_org = ','.join(str(x) for x in orglist)
        if ',' in all_org:
            all_org = all_org.split(',')[0]
            print(uniprot,all_symbols,all_alt,all_names,all_org, sep = ';', file = out2)     
        else:
            all_org = all_org
            print(uniprot,all_symbols,all_alt,all_names,all_org, sep = ';', file = out2)
#----------------------------

#Overlap5_clean and mapped gene ontology-Lysosome(Amigo search of human and yeast entries without uniprot IDs)

dict_over = {}
dict_clean = {}
with open('Overlap5_clean') as over , open('Amigo_ODB_Lys_HomoSacch') as clean, open('overODB', 'w') as out:
    for line in over:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_over[uniprotID] = {}
        symbol = line[1]
        dict_over[uniprotID]['symbol'] = symbol
        alternative= line[2]
        dict_over[uniprotID]['alternative'] = alternative
        org = line[4]
        dict_over[uniprotID]['org'] = org
        fullname = line[3]
        dict_over[uniprotID]['fullname'] = fullname
    for line in clean:
        line=line.rstrip()
        line=line.split('\t')
        uniprot = line[0]
        dict_clean[uniprot] = {}
        symbol = line[1]
        dict_clean[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_clean[uniprot]['synonym'] = synonym
        protname= line[3]
        dict_clean[uniprot]['protname'] = protname
        organism = line[4]
        dict_clean[uniprot]['organism'] = organism
    for key in dict_over:
        if key in dict_clean:
            print(key, dict_over[key]['symbol']+',' + dict_clean[key]['symbol'], dict_over[key]['alternative']+','+ dict_clean[key]['synonym'],dict_over[key]['fullname']+'|'+dict_clean[key]['protname'],dict_over[key]['org']+','+dict_clean[key]['organism'], sep = ';', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    for key in dict_clean:
        if not key in dict_over:
            print(key,dict_clean[key]['symbol'], dict_clean[key]['synonym'], dict_clean[key]['protname'], dict_clean[key]['organism'], sep = ';', file = out)

import re
with open('overODB', 'r') as over, open('Overlap6_ODB', 'w') as out2:
    for line in over:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        name = name.splitlines()
        for line in symbol:
            line=line.rstrip()
            symbollist = set(line.split(','))
        for line in alt:
            line=line.rstrip()
            altlist = set(line.split(','))
        for line in name:
            line=line.rstrip()
            namelist = set(line.split('|')) 
        for line in org:
            line = line.rstrip()
            orglist = set(line.split(','))
        all_symbols = ','.join(str(x) for x in symbollist)
        all_alt = ','.join(str(x) for x in altlist)
        all_names = '|'.join(str(x) for x in namelist)
        all_org = ','.join(str(x) for x in orglist)
        print(uniprot,all_symbols,all_alt,all_names,all_org, sep = '\t', file = out2)    
#---------------------------
#clean end file

#remove nan from synonyms 

#Remove 'nan' in names and organisms

syn_list = []
with open('Overlap6_ODB') as over, open('Final_Lysosome_Data', 'w') as out:
    print('uniprot_lys', 'Symbol_lys', 'Synonym_lys', 'ProtName_lys', 'Organism_lys', sep = '\t', file = out)
    for line in over:
        line=line.rstrip()
        line=line.split('\t')
        uniprot = line[0]
        gname = line[1]
        name= line[3]
        org = line[4]
        synonym = line[2]
        if ',' in synonym:
            syn_list = []
            synonym = synonym.split(',')
            synonym = ['' if x == 'nan' else x for x in synonym]
            synonym = list(filter(None, synonym))
            synonym = ','.join(synonym)
            print(uniprot, gname, synonym, name, org, sep = '\t', file = out)
        else:
            print(uniprot, gname, synonym, name, org, sep = '\t', file = out)
#------------------------------    
    
     
           
    
        
     
