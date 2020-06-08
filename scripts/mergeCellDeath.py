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

#Merge Overlap1_BclApop and mapped deathbase 
#first get synonyms and official gene symbols + necessary info from Reviewed_deathbase and save to Final_deathbase.
count = 0
clean_list = []
rev_dict = {}
with open('clean_deathbase') as clean, open('Reviewed_deathbase') as rev, open('Final_deathbase', 'w') as out:
    for line in clean:
        if not 'uniprot_DeathB' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[0].replace(' ', '')
            count+=1
            clean_list.append(uniprot)
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[1]
            rev_dict[uniprot] = {}
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            rev_dict[uniprot]['symbol'] = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            rev_dict[uniprot]['synonym'] = synonym
            org = line[6]
            rev_dict[uniprot]['org'] = org
            protname = line[4]
            rev_dict[uniprot]['protname'] = protname
            
    for key in rev_dict:
        if key in clean_list:
            print(key, rev_dict[key]['symbol'], rev_dict[key]['synonym'], rev_dict[key]['protname'], rev_dict[key]['org'], sep = '\t', file = out)
 
    
dict_over = {}
dict_fin = {}
count = 0
with open('Overlap1_BclApop') as over, open('Final_deathbase') as fin, open('overdeathbase', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in fin:
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_fin[uniprot] = {}
        symbol = line[1]
        dict_fin[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_fin[uniprot]['synonym'] = synonym
        protname = line[3]
        protname = protname.split('(EC ')[0]
        protname = protname.split('[Cleaved ')[0]
        dict_fin[uniprot]['protname'] = protname
        org = line[4]
        dict_fin[uniprot]['org'] = org
    for key in dict_over:
        if key in dict_fin:
            print(key, dict_over[key]['symbol']+','+dict_fin[key]['symbol'], dict_over[key]['synonym']+','+dict_fin[key]['synonym'], dict_over[key]['protname']+'|'+dict_fin[key]['protname'], dict_over[key]['org']+','+dict_fin[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in dict_fin:
        if not key in dict_over:
            print(key, dict_fin[key]['symbol'],dict_fin[key]['synonym'],dict_fin[key]['protname'],dict_fin[key]['org'], sep = '\t', file = out)
        
        
        
import re
with open('overdeathbase', 'r') as over, open('Overlap2_Dbase', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
        print(uniprot,all_symbols,all_alt,all_names,all_org, sep = '\t', file = out2)    #225 all unique No unreviewed. 
#------------------------------------

# Overlap2_Dbase and mapped gene ontology (Amigo search/ entries with uniprot IDs)

count = 0
dict_over = {}
full_dict = {}
with open('Overlap2_Dbase') as over, open('Full_Reviewed_uniprotAmigo') as full, open('overAmigo', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        protname = protname.split('(EC ')[0]
        protname = protname.split('[Cleaved ')[0]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in full:
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        full_dict[uniprot] = {}
        symbol = line[1]
        full_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        full_dict[uniprot]['synonym'] = synonym
        org = line[4]
        full_dict[uniprot]['org'] = org
        protname = line[3]
        full_dict[uniprot]['protname'] = protname
    for key in dict_over:
        if key in full_dict:
            print(key,dict_over[key]['symbol']+','+full_dict[key]['symbol'], dict_over[key]['synonym']+','+full_dict[key]['synonym'], dict_over[key]['protname']+'|'+full_dict[key]['protname'], dict_over[key]['org']+','+full_dict[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in full_dict:
        if not key in dict_over:
            print(key,full_dict[key]['symbol'],full_dict[key]['synonym'],full_dict[key]['protname'],full_dict[key]['org'], sep = '\t', file = out)
            
                
with open('overAmigo', 'r') as over, open('Overlap3_Amigo', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
#--------------------------------

#Overlap3_Amigo and mapped CASBAH to uniprot.

dict_over = {}
count = 0
rev_dict = {}
with open('Overlap3_Amigo') as over, open('Reviewed_CASBAH') as rev, open('overCas', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[1] #line 0 is the entry that I mapped
            rev_dict[uniprot] = {}
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            if symbol == '':
                symbol = 'nan'
            else:
                symbol = symbol
            rev_dict[uniprot]['symbol'] = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            rev_dict[uniprot]['synonym'] = synonym
            protname = line[4]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            rev_dict[uniprot]['protname'] = protname
            org = line[6]
            rev_dict[uniprot]['org'] = org          
    for key in dict_over:
        if key in rev_dict:
            print(key,dict_over[key]['symbol']+','+rev_dict[key]['symbol'], dict_over[key]['synonym']+','+rev_dict[key]['synonym'], dict_over[key]['protname']+'|'+rev_dict[key]['protname'], dict_over[key]['org']+','+rev_dict[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in rev_dict:
        if not key in dict_over:
            print(key,rev_dict[key]['symbol'],rev_dict[key]['synonym'],rev_dict[key]['protname'],rev_dict[key]['org'], sep = '\t', file = out)
            
import re    
with open('overCas', 'r') as over, open('Overlap4_CAS', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
            altlist = set(re.split('[,/]', line))
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
#-----------------------------

#Overlap4_CAS with mapped gene ontology-cell death

dict_over = {}
count = 0
rev_dict = {}
with open('Overlap4_CAS') as over, open('Reviewed_New_cellDeath') as rev, open('overNewCD', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[0] 
            rev_dict[uniprot] = {}
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            if symbol == '':
                symbol = 'nan'
            else:
                symbol = symbol
            rev_dict[uniprot]['symbol'] = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            rev_dict[uniprot]['synonym'] = synonym
            protname = line[4]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            rev_dict[uniprot]['protname'] = protname
            org = line[6]
            rev_dict[uniprot]['org'] = org          
    for key in dict_over:
        if key in rev_dict:
            print(key,dict_over[key]['symbol']+','+rev_dict[key]['symbol'], dict_over[key]['synonym']+','+rev_dict[key]['synonym'], dict_over[key]['protname']+'|'+rev_dict[key]['protname'], dict_over[key]['org']+','+rev_dict[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in rev_dict:
        if not key in dict_over:
            print(key,rev_dict[key]['symbol'],rev_dict[key]['synonym'],rev_dict[key]['protname'],rev_dict[key]['org'], sep = '\t', file = out)
            
with open('overNewCD', 'r') as over, open('Overlap5_newCD', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
#-----------------------------

#Overlap5_newCD and mapped gene ontology's human and yeast entries from other databases without uniprot IDs.
#substitute Reviewed_homo_ODB with Reviewed_Saccharomyces_ODB and run the code.

dict_over = {}
count = 0
rev_dict = {}
with open('Overlap5_newCD') as over, open('Reviewed_homo_ODB') as rev, open('overODB1', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[1] 
            rev_dict[uniprot] = {}
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            if symbol == '':
                symbol = 'nan'
            else:
                symbol = symbol
            rev_dict[uniprot]['symbol'] = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            rev_dict[uniprot]['synonym'] = synonym
            protname = line[4]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            rev_dict[uniprot]['protname'] = protname
            org = line[6]
            rev_dict[uniprot]['org'] = org          
    for key in dict_over:
        if key in rev_dict:
            print(key,dict_over[key]['symbol']+','+rev_dict[key]['symbol'], dict_over[key]['synonym']+','+rev_dict[key]['synonym'], dict_over[key]['protname']+'|'+rev_dict[key]['protname'], dict_over[key]['org']+','+rev_dict[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in rev_dict:
        if not key in dict_over:
            print(key,rev_dict[key]['symbol'],rev_dict[key]['synonym'],rev_dict[key]['protname'],rev_dict[key]['org'], sep = '\t', file = out)
            
with open('overODB1', 'r') as over, open('Overlap6_ODB1', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
#--------------------------------

#mapped gene ontology(entries with uniprot IDs from other databases)  with overlap6_ODB2.
            
dict_over = {}
count = 0
rev_dict = {}
with open('overlap6_ODB2') as over, open('reviewed_SynAmigo_ODB') as rev, open('oversyn', 'w') as out:
    for line in over:
        line= line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        dict_over[uniprot] = {}
        symbol = line[1]
        dict_over[uniprot]['symbol'] = symbol
        synonym = line[2]
        dict_over[uniprot]['synonym'] = synonym
        protname = line[3]
        dict_over[uniprot]['protname'] = protname
        org = line[4]
        dict_over[uniprot]['org'] = org
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[1] 
            rev_dict[uniprot] = {}
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            if symbol == '':
                symbol = 'nan'
            else:
                symbol = symbol
            rev_dict[uniprot]['symbol'] = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            rev_dict[uniprot]['synonym'] = synonym
            protname = line[4]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            rev_dict[uniprot]['protname'] = protname
            org = line[6]
            rev_dict[uniprot]['org'] = org          
    for key in dict_over:
        if key in rev_dict:
            print(key,dict_over[key]['symbol']+','+rev_dict[key]['symbol'], dict_over[key]['synonym']+','+rev_dict[key]['synonym'], dict_over[key]['protname']+'|'+rev_dict[key]['protname'], dict_over[key]['org']+','+rev_dict[key]['org'], sep = '\t', file = out)
        else:
            print(key,dict_over[key]['symbol'],dict_over[key]['synonym'],dict_over[key]['protname'],dict_over[key]['org'], sep = '\t', file = out)
            
    for key in rev_dict:
        if not key in dict_over:
            print(key,rev_dict[key]['symbol'],rev_dict[key]['synonym'],rev_dict[key]['protname'],rev_dict[key]['org'], sep = '\t', file = out)
            
with open('oversyn', 'r') as over, open('Overlap7_syn', 'w') as out2:
    for line in over:
        line=line.rstrip().split('\t')
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
        
        #add headers and call it Final_Clean_CellDeath_Data
 #--------------------------                         
