#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO DOWNLOAD ALL DATA USED IN THIS SHORT PROJECT.
#
#---------------------------------

#get the gene names of the unmapped entrez IDs list. High confidence file
unmap_list = []
count=0
with open('Unmapped_entrez_sampleAND.txt') as unmap, open('cellcount_rep1_and_rep2_0.75sample.csv') as csv, open('Map_geneNames_To_Uni_Sample0.75AND', 'w') as out:
    for line in unmap:
        line = line.rstrip()
        unmap_list.append(line)
    for line in csv:
        if not 'entrez' in line:
            if not 'empty' in line:
                line = line.rstrip()
                line = line.split(',')
                entrez_ID = line[4]
                entrez_name = line[3]
                if entrez_ID in unmap_list:
                    print(entrez_name, file = out)
#---------------------------------        

#Combine the reviewed entries that were got from reviewed gene names and reviewed entrez IDs

with open('MappedReviewed_Entrez_sampleAND_0.75') as ent, open('Reviewed_geneNames_sample_AND0.75') as gene, open('Full_reviewed_0.75AND_sample', 'w') as out:
    print('Uniprot', 'Symbol', 'Synonym', 'Protname', 'Org', sep = '\t', file = out)
    for line in ent:
        if not 'your' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[1]
            symbol = line[5]
            synonym = line[6]
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym.replace(' ', ',')
            protname = line[7]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            org = line[8]
            print(uniprot,symbol,synonym,protname,org, sep = '\t', file = out)
    for line in gene:
        line = line.rstrip()
        if not 'your' in line:
            line = line.split('\t')
            uniprot = line[0]
            symbol = line[4]
            synonym = line[5]
            if synonym == '':
                synonym = 'nan'
            else:
                synonym = synonym.replace(' ', ',')
            
            protname = line[6]
            protname = protname.split('(EC ')[0]
            protname = protname.split('[Cleaved ')[0]
            org = line[7]
            print(uniprot,symbol,synonym,protname,org, sep = '\t', file = out)
#-----------------------------

#Match gene names that didn't map to uniprot to UNIPROT-HGNC data table.

gene_list = []
line_list = []
line_dict = {}
with open(r'FULL_HGNCUNI_table') as table, open('Unmapped_gene_names_sample_AND0.75.txt') as gene, open('Mapped_gene_names_to_Uniprothgnc_AND0.75', 'w') as out:
    for line in gene:
        line = line.rstrip()
        gene_list.append(line)
    for line in table:
        line = line.rstrip()
        line = re.split('[\t,]', line)
        for element in line:
            if element in gene_list:
                line = '\t'.join(line)
                if '9606' in line:
                    line = line.split('\t')
                    print(line[0], element, sep = '\t', file = out)
#-----------------------------

#The same codes were written for moderate and low confidence files, cellcount_rep1_and_rep2_0.85sample.csv and cellcount_rep1_or_rep2_0.75sample.csv respectively.
    
