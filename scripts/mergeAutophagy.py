#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO MERGE DATABASES AND COLLECT ALL POSSIBLE GENES RELATED TO AUTOPHAGY.
#
#---------------------------------

#HAMdb and The Autophagy Database
count = 0
dict_prot ={}
dict_aut = {}
with open('TBU_proteinbasicHAMdb_clean', 'r') as prot, open('TBU_TheAutophagyDB_clean', 'r') as auto, open('over_HA', 'w') as two:
    lines = auto.readlines()[1:] #remove the header of the file. readlines() generates a list of lines.
    for line in lines:
        line=line.rstrip()
        line=line.split(';')
        uniprotID = line[0]
        dict_aut[uniprotID] = {}
        Symbol = line[1]
        dict_aut[uniprotID]['Symbol'] = Symbol
        synonym = line[2]
        dict_aut[uniprotID]['Synonym'] = synonym
        fullname = line[3]
        dict_aut[uniprotID]['Fullname'] = fullname
    lines = prot.readlines()[1:] # remove file's header
    for line in lines:
        line=line.rstrip()
        line=line.split(';')
        uniprot = line[0]
        dict_prot[uniprot] = {}
        symbol = line[1]
        dict_prot[uniprot]['symbol'] = symbol
        altern = line[2]
        dict_prot[uniprot]['alternative'] = altern
        org = line[3]
        dict_prot[uniprot]['organism'] = org  
    for key in dict_prot:
        if key in dict_aut:
            print(key,dict_prot[key]['symbol'],dict_prot[key]['alternative']+','+dict_aut[key]['Synonym'] , dict_aut[key]['Fullname'],dict_prot[key]['organism'],sep = ';', file = two)      
        else:
            print(key,dict_prot[key]['symbol'],dict_prot[key]['alternative'],'nan', dict_prot[key]['organism'],sep = ';', file = two)
    for key in dict_aut:
        if not key in dict_prot:
            print(key,dict_aut[key]['Symbol'],dict_aut[key]['Synonym'],  dict_aut[key]['Fullname'],'nan',sep = ';', file = two)
# It contains all unique overlapped and non-overlapped lines from both files.

#clean the file above by removing the repeated synonyms/names..etc and keep the unique ones per field.
import re

with open('over_HA', 'r') as test, open('Overlap_HAMdbAuto','w') as over:
    for line in test:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        org = line[4]
        name = line[3]
        alt = line[2]
        #this will split the synonyms and alternatives into lists, each on a line.
        alt = alt.splitlines()
        #loop over the list (alt) of strings to print each list's content on a line. Each list has a string and will be printed.
        for line in alt:
            line=line.strip()
            #split on the multiple delimiters in synonyms. Will be automatically replaced by commas. I need to do this in order to add them all into a set and take unique synonyms for each uniprot ID.
            synonymlist = set(re.split('[;|,]', line))
        #save each set content on a line (NOTICE THAT I STARTED WITH THE JOIN THEN I LOOPED).
        all_synonyms=','.join(str(x) for x in synonymlist)
        print(uniprot,symbol,all_synonyms,name,org, sep = ';', file = over)
#----------------------------

#Overlap_HAMdbAuto and gene ontology/autophagy data

count = 0
goa_auto = {}
dict_over = {}
with open('Overlap_HAMdbAuto', 'r') as over, open('TBU_New_autophagy', 'r') as goa, open('over_HG', 'w') as test:
    lines = goa.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split(';')
        Uniprotgo = line[0]
        goa_auto[Uniprotgo] = {}
        Symbolgo = line[1]
        goa_auto[Uniprotgo]['Symbol'] = Symbolgo
        name = line[2]
        goa_auto[Uniprotgo]['name'] = name
        Synonym = line[3]
        goa_auto[Uniprotgo]['Synonym'] = Synonym  
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
    for key in dict_over:
        if key in goa_auto:
            print(key,goa_auto[key]['Symbol']+','+dict_over[key]['symbol'],dict_over[key]['alternative']+','+goa_auto[key]['Synonym'],goa_auto[key]['name']+'|'+dict_over[key]['fullname'], dict_over[key]['org'], sep = ';', file = test)
        else:
            print(key, dict_over[key]['symbol'], dict_over[key]['alternative'], dict_over[key]['fullname'], dict_over[key]['org'], sep = ';', file = test)
    for key in goa_auto:
        if not key in dict_over:
            print(key, goa_auto[key]['Symbol'], goa_auto[key]['Synonym'],goa_auto[key]['name'], 'nan', sep = ';' , file = test)
 

            
import re

with open('over_HG', 'r') as test, open('Overlap_GoaOver','w') as over:
    for line in test:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        org = line[4]
        name = line[3]
        namelist = set(re.split('[|]', name))
        alt = line[2]
        alt = alt.splitlines()
        for line in alt:
            line=line.strip()
            synonymlist = set(re.split('[|,]', line))
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[|,]', line))         
        #save each set content on a line (NOTICE THAT I STARTED WITH THE JOIN THEN I LOOPED).
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,org, sep = ';', file = over)    
#------------------------------

#Overlap_GoaOver and Human Autophagy database(HADB)

count =0 
dict_over = {}
dict_hadb = {}

with open('Overlap_GoaOver', 'r') as over, open('TBU_New_HADB', 'r') as tbu, open('over_GHA', 'w') as out:
    lines = tbu.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split(';')
        Uniprot = line[1]
        dict_hadb[Uniprot] = {}
        Symbol = line[3]
        dict_hadb[Uniprot]['Symbol'] = Symbol
        name = line[2]
        dict_hadb[Uniprot]['name'] = name
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
    for key in dict_hadb:
        if key in dict_over:
            print(key, dict_hadb[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative'], dict_hadb[key]['name']+'|'+dict_over[key]['fullname'], dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key, dict_hadb[key]['Symbol'], 'nan', dict_hadb[key]['name'],'nan', sep = ';', file = out)
    
    for key in dict_over:
        if not key in dict_hadb:
            print(key, dict_over[key]['symbol'], dict_over[key]['alternative'],dict_over[key]['fullname'], dict_over[key]['org'], sep = ';', file = out)

import re
with open('over_GHA', 'r') as gha, open('Overlap2_hadbOver', 'w') as over:
    for line in gha:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        org = line[4]
        name = line[3]
        name = name.splitlines()
        alt = line[2]
        alt = alt.splitlines()
        for line in alt:
            line=line.strip()
            synonymlist = set(re.split('[|,:]', line))
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[;|,/:]', line))
        for line in name:
            line=line.rstrip()
            namelist = set(re.split('[|]', line))            
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,org, sep = ';', file = over)    
#------------------------------

#Overlap2_hadbOver and gene ontology/Amigo-autophagy search (entries with uniprot IDs).
count =0 
dict_over = {}
dict_amigo = {}

with open('Overlap2_hadbOver', 'r') as over, open('TBU_New_UniprotAmigo_autophagy', 'r') as tbu, open('over_am', 'w') as out:
    lines = tbu.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split(';')
        Uniprot = line[0]
        dict_amigo[Uniprot] = {}
        Symbol = line[1]
        dict_amigo[Uniprot]['Symbol'] = Symbol
        preSynonym = line[2]
        if ':' in preSynonym:
            Synonym = preSynonym.split(':')[1]
        else:
            Synonym = preSynonym
        dict_amigo[Uniprot]['Synonym'] = Synonym
        organism = line[3]
        dict_amigo[Uniprot]['organism'] = organism
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
    for key in dict_amigo:
        if key in dict_over:
            print(key, dict_amigo[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative']+','+dict_amigo[key]['Synonym'], dict_over[key]['fullname'], dict_amigo[key]['organism']+','+dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key, dict_amigo[key]['Symbol'], dict_amigo[key]['Synonym'],'nan',dict_amigo[key]['organism'], sep = ';', file = out)    
    for key in dict_over:
        if not key in dict_amigo:
            print(key, dict_over[key]['symbol'], dict_over[key]['alternative'],dict_over[key]['fullname'], dict_over[key]['org'], sep = ';', file = out)

import re
with open('over_am', 'r') as am, open('Overlap3_amigoOver', 'w') as over:
    for line in am:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        alt = line[2]
        alt = alt.splitlines()
        for line in alt:
            line=line.strip()
            synonymlist = set(re.split('[|,:]', line))
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[;|,/:]', line))
        for line in org:
            line=line.rstrip()
            orglist = set(re.split('[;|,/:]', line)) 
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        print(uniprot,all_symbols,all_synonyms,name,all_org, sep = ';', file = over)    
#-----------------------------------

#Overlap3_amigoOver and gene ontology/Amigo-autophagy search (entries with uniprot IDs from databases other than uniprot)
count =0 
dict_over = {}
dict_amigo = {}

with open('Overlap3_amigoOver', 'r') as over, open('TBU_UniprotSyn_ODB_autophagy', 'r') as tbu, open('over_amUni', 'w') as out:
    lines = tbu.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split(';')
        Uniprot = line[2]
        dict_amigo[Uniprot] = {}
        Symbol = line[1]
        dict_amigo[Uniprot]['Symbol'] = Symbol
        organism = line[3]
        dict_amigo[Uniprot]['organism'] = organism
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
    for key in dict_amigo:
        if key in dict_over:
            print(key, dict_amigo[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative'], dict_over[key]['fullname'], dict_amigo[key]['organism']+','+dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key,dict_amigo[key]['Symbol'],'nan','nan',dict_amigo[key]['organism'],sep = ';', file = out)
            
    for key in dict_over:
        if not key in dict_amigo:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
import re
with open('over_amUni', 'r') as am, open('Overlap4_amigoSynOver', 'w') as over:
    for line in am:
        line=line.rstrip().split(';')
        uniprot = line[0]
        symbol=line[1]
        symbol = symbol.splitlines()
        org = line[4]
        org = org.splitlines()
        name = line[3]
        alt = line[2]
        for line in symbol:
            line=line.rstrip()
            symbollist = set(re.split('[;,/]', line))
        for line in org:
            line=line.rstrip()
            orglist = set(re.split('[;,/]', line)) 
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        print(uniprot,all_symbols,alt,name,all_org,sep = ';', file = over)    
#--------------------------------

#MERGE ENSEMBL and ENTREZ mapped entries 
#Map the ENSEMBL protein IDs for the entries that do not have uniprot IDs yet have the ENSEMBL IDs because these are unique (ENS[species prefix][feature type prefix][a unique eleven digit number]).<br> 
#If the missing uniprot doesn't have ENSEMBL Ids in the symbols but have entrez gene IDs, then map the entrez.

#split the entries to 11 files and prepare for mapping.
with open('mapENStoUni', 'r') as pinfile:
    lines = pinfile.readlines() # create list of lines (ENS IDs)
    count = 0
    for i in range(0,len(lines), 1000): # to print each 1000 lines to a separate file.
        count+=1
        outfileName = 'output_' + str(count)
        try: #try, except are used because the number of lines in the original file is 10492. If I want to print each 1000 lines in a file then the last file will give syntax error because the number of lines are less than 1000.
            with open(outfileName, 'w') as poutfile:
                for line in lines[i:i+1000]:
                    poutfile.write(line)
        except: #if the file doesn't have 1000 lines.
            with open(outfileName, 'w') as poutfile:
                for line in lines[i:]:
                    pooutfile.write(line)
        #Use try,except when there's a time that I want to avoid an error that I expect to happen.    
        
with open('atg_genes_detail.dat') as auto, open('Entrez_maptoUni', 'w') as out:
    lines = auto.readlines()[1:]
    for line in lines:
        line=line.rstrip()
        line=line.split('\t')
        if not 'ENS' in line[2]: #line 2 is the symbols line
            if line[18] == '': #line 18 is the uniprot ID.
                if not '0' in line[6]: #line 6 is the entrez ID
                    #print(line[2],line[6], line[18])
                    print(line[6], file = out) 
                    
 synonym_list =[]
synonym_list2 = []
with open('reviewedEntrez_mappedAuto') as ent,open('Full_reviewed_mappedENS') as ens, open('synonyms_ENS', 'w') as out, open('prefinal_ENT', 'w') as output,open('prefinal_ENS','w') as output2:
    for line in ent:
        if not 'your' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprot = line[1]
            gsym = line[5].split(' ') # the primary name and synonym are separated by space
            symbol = gsym[0]
            synonym = gsym[1]
            protname = line[4].replace(';', ',')
            organism = line[6]
            print(uniprot,symbol,protname,organism,synonym, sep = ';',file = output)
    for line in ens:
        synonym_list = []
        if not 'your' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprot = line[2]
            gsym = line[6].split(' ')
            symbol = gsym[0]
            protname = line[5].replace(';', ',')
            organism = line[7]
            print(uniprot,symbol,protname,organism, sep = ';', file = output2)
            synonym = gsym[1:] # separate synonyms from primary gene name.
            for element in synonym:
                #get each set of synonyms separately
                synonym_list.append(element)
                synonym = ','.join(synonym_list)
            synonym_list2.append(synonym)         
    synonym_list2 = ["nan" if x == [] else x for x in synonym_list2] #remove [] from the list
    for element in synonym_list2:
        print(element, file = out)
            
            
#paste -d ';' prefinal_ENS synonyms_ENS > Ensembl_rev_separated
#cat Ensembl_rev_separated prefinal_ENT > ENSENT_FullReviewedAUTO_nan 


#Overlap4_amigoSynOver and ENSEMBL/ENTREZ merged entries
dict_over = {}
dict_rev= {}
with open('Overlap4_amigoSynOver', 'r') as over, open('ENSENT_FullReviewedAUTO_nan', 'r') as rev, open('over_auto_nan', 'w') as out:
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
    for line in rev:
        line=line.rstrip()
        line=line.split(';')
        Uniprot = line[0]
        dict_rev[Uniprot] = {}
        Symbol = line[1]
        dict_rev[Uniprot]['Symbol'] = Symbol
        name= line[2]
        dict_rev[Uniprot]['name'] = name
        synonym = line[4]
        dict_rev[Uniprot]['Synonym'] = synonym
        org = line[3]
        dict_rev[Uniprot]['organism'] = org
    for key in dict_rev:
        if key in dict_over:
            print(key, dict_rev[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative']+','+dict_rev[key]['Synonym'], dict_over[key]['fullname']+'|'+dict_rev[key]['name'], dict_rev[key]['organism']+','+dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key,dict_rev[key]['Symbol'],dict_rev[key]['Synonym'],dict_rev[key]['name'],dict_rev[key]['organism'],sep = ';', file = out)
            
    for key in dict_over:
        if not key in dict_rev:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)

        
        
import re
with open('over_auto_nan', 'r') as over, open('Overlap5_hgncOver', 'w') as out2:
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
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,all_org, sep = ';', file = out2)      
#-------------------------------    
  
#Merge mapped entries from gene ontology database/ genes belonging to human and yeast that didn't have uniprot IDs.

synhuman_list = []
synhuman_list2 = []
synSac_list = []
synSac_list2 = []

with open('Reviewed_human_AmigoODB') as human, open('Reviewed_Sacch_AmigoODB') as sac,open('synonym_HumanSac', 'w') as out, open('PreFullreviwed_HomoSacch_AmigoODB', 'w') as out2:
    for line in human:
        synhuman_list = []
        if not 'your' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprot = line[1]
            protname = line[4].replace(';', ',')
            organism = line[6]
            gsyn = line[5].split(' ')
            symbol = gsyn[0]
            print(uniprot,symbol,protname,organism, sep = ';',file = out2)
            synonym = gsyn[1:]
            for element in synonym:
                #get each set of synonyms separately
                synhuman_list.append(element)
                synonym = ','.join(synhuman_list)
            synhuman_list2.append(synonym)         
    synhuman_list2 = ["nan" if x == [] else x for x in synhuman_list2] #remove [] from the list
    for element in synhuman_list2:
        print(element, file = out)
    
    for line in sac:
        synSac_list = []
        if not 'your' in line:
            line=line.rstrip()
            line=line.split('\t')
            uniprot = line[1]
            protname = line[4].replace(';', ',')
            organism = line[6]
            print(uniprot,symbol,protname,organism, sep = ';',file = out2)
            gsyn = line[5].split(' ')
            symbol = gsyn[0]
            synonym = gsyn[1:]
            for element in synonym:
                #get each set of synonyms separately
                synSac_list.append(element)
                synonym = ','.join(synSac_list)
            synSac_list2.append(synonym)         
    synSac_list2 = ["nan" if x == [] else x for x in synSac_list2] #remove [] from the list
    for element in synSac_list2:
        print(element, file = out)         
#paste -d ';' PreFullreviwed_HomoSacch_AmigoODB synonym_HumanSac > Fullreviwed_HomoSacch_AmigoODB    
      

#Fullreviwed_HomoSacch_AmigoODB and Overlap5_hgncOver

dict_over = {}
dict_mapp = {}
with open('Overlap5_hgncOver', 'r') as over, open('Fullreviwed_HomoSacch_AmigoODB', 'r') as mapp, open('over_amigoODB', 'w') as out:
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
        if key in dict_over:
            print(key, dict_mapp[key]['Symbol']+','+dict_over[key]['symbol'], dict_over[key]['alternative']+','+dict_mapp[key]['Synonym'], dict_over[key]['fullname']+'|'+dict_mapp[key]['protname'], dict_mapp[key]['organism']+','+dict_over[key]['org'], sep = ';', file = out)
        else:
            print(key,dict_mapp[key]['Symbol'],dict_mapp[key]['Synonym'],dict_mapp[key]['protname'],dict_mapp[key]['organism'],sep = ';', file = out)            
    for key in dict_over:
        if not key in dict_mapp:
            print(key,dict_over[key]['symbol'],dict_over[key]['alternative'],dict_over[key]['fullname'],dict_over[key]['org'], sep = ';', file = out)
    
    
import re
with open('over_amigoODB', 'r') as over, open('Overlap6_ODBOver', 'w') as out2:
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
        all_synonyms=','.join(str(x) for x in synonymlist)
        all_symbols = ','.join(str(x) for x in symbollist)
        all_org = ','.join(str(x) for x in orglist)
        all_names = '|'.join(str(x) for x in namelist)
        print(uniprot,all_symbols,all_synonyms,all_names,all_org, sep = ';', file = out2)       
    #------------------------------
    
#Reviewed entries were considered after mapping the uniprot IDs to uniprot. 
#Fix structure.

with open('Reviewed_Final_AutpphagyMappedData') as rev, open('Final_Clean_Autophagy_Data', 'w') as out:
    print('Auto_Uniprot', 'Auto_Symbol', 'Auto_Synonym', 'Auto_ProteinName', 'Auto_Organism', sep = '\t', file = out)
    for line in rev:
        if not 'your' in line:
            line = line.rstrip()
            line=line.split('\t')
            uniprot = line[0]
            gsyn = line[5]
            symbol = gsyn.split(' ')[0]
            if symbol == '':
                symbol = 'nan'
            else:
                symbol = symbol
            synonym = gsyn.split(' ')[1:]
            synonym = ','.join(synonym)
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym
            protname = line[4]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            org = line[6]
            print(uniprot,symbol,synonym,protname,org, sep = '\t', file = out)
#---------------------------
