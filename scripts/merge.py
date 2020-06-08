#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO MERGE DATABASES AND COLLECT ALL POSSIBLE GENES RELATED TO AUTOPHAGY,CELL DEATH, AND LYSOSOMES.
#
#---------------------------------

#START WITH *AUTOPHAGY DATA*


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
#cat Ensembl_rev_separated prefinal_ENT > ENSENT_FullReviewedAUTO_nan ##save to mapENSENT_files
    
    
                                   
