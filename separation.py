gsyn_list = [] # this will hold genes and synonyms that were moxed together in column #4
genelist = [] # this will hold the gene names in the first column of the file.
syn_list = [] # this will hold the separated synonyms 
with open('PreUniprot_Data_table') as pre, open('synonyms_HU', 'w') as out:
    for line in pre:
        line=line.rstrip()
        line=line.split('\t')
        gene_name = line[0]
        genelist.append(gene_name)
        uniprot = line[1]
        name = line[2]
        gsyn = line[3]
        gsyn_list.append(gsyn)
    for element in gsyn_list:
        syn_list = [] # always empty the list if I need to get joined entries.
        if ',' in element:
            gslist = element.split(',')#55965
            for syn in gslist:
                if not syn in genelist:
                    syn_list.append(syn)
                    ','.join(syn_list)
        print(syn_list, file = out)

#cat synonyms_HU | tr -d "[]'" > clean_synonym_HU
#cat PreUniprot_Data_table | cut -f1 > HU_genename
#cat PreUniprot_Data_table | cut -f2 > HU_protID
#cat PreUniprot_Data_table | cut -f3 > HU_protname
#cat PreUniprot_Data_table | cut -f5 > HU_Luge
#paste -d '\t' HU_protID HU_genename clean_synonym_HU HU_protname HU_Luge > Uniprot_Data_table
       
        
