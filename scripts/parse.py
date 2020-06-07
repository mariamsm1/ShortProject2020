#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO PARSE DATABASES THAT WERE AVAILABLE FOR DOWNLOAD.
#
#---------------------------------

#Parsing Human Autophagy Modulator Database (HAMdb)

mylist=[]
uniprot_list = []
#junk list contains all the not-needed cells that were embedded in the alternative names (they were not alternative names)
junk_list= ['metastatic prostate cancer; primary prostate cancer', '1GAG;1I44;1IR3;1IRK;1P14;1RQQ;2AUH;2B4S;2HR7;2MFR;2Z8C;3BU3;3BU5;3BU6;3EKK;3EKN;3ETA;3W11;3W12;3W13;3W14;4IBM;4OGA;4XLV;4XSS;4XST;4ZXB;5E1S;5HHW;5J3H',
'2YS1', '1B8M;1BND', 'Ins1; LY294002; PI3K (complex); wortmannin; IGF1; PDPK1; Insulin; PTEN; INS; EGF; AKT1; Pdgf (complex); TNF; hydrogen peroxide; ILK', 'D-glucose; dexamethasone; REN; beta-estradiol; IL6; losartan potassium; AGT; candesartan; SB203580; Ins1; ACE; lipopolysaccharide; STAT3; Insulin; phorbol myristate acetate',
'advanced glycation end-products; HMGB1; TNF; advanced glycation endproducts-bovine serum albumin; APP; exenatide; GLP-1-(7-34)-amide; GCG; D-glucose; CRP; NFkB (complex); IL1B; PSEN1; AGER; S100B', '221040736;1034671294;46394126;56788407;158261143;553634;221045686;56788401;56788405;13129138;767958268;383875656;48762798;119608037;56788403;119608038;1034671292;46391586;56788399;48762794;46391582;52545786;15214282;48762796;383875657',
'hypertension']
#alter_list will be used to append all the alternative names (including alternative name #736 which will be removed from te list)
alter_list = []

#each file ('w') is used to include one field (ex Symbol, uniprot_ID, organism) these fields will be all pasted in bash.
with open('protein-basic.csv', 'r', encoding = 'latin1') as protein, open('TBU_Symbol', 'w') as output, open('TBU_uniprot', 'w') as out, open('TBU_homo', 'w') as out2:
    for line in protein:
        #The following line will be used to extract homo_sapiens from the splitted list
        line_homo = line.split(',')
        for element in line_homo:
            if element == 'Organism' or element == 'Homo sapiens (Human)':
                print(element, file= out2)
        #here I need to take the Symbol (index 0), but since some of them start with " , i need to remove it.
        Symb = line.split(',')[0]
        if not Symb.startswith('"'):
            print(Symb, file=output)
            Uniprot = line.split(',')[2]
            #it's appended to a list to replace the empty strings with 'nan'
            uniprot_list.append(Uniprot)
            uniprot_list = ["nan" if x == '' else x for x in uniprot_list]
    for element in uniprot_list:
        print(element, file = out)

#specify the delimiter in the output file
df = pd.read_csv('protein-basic.csv', encoding = 'latin1')
outfile = 'protein_output'
df.to_csv(outfile,index=False, sep = '|')

with open('protein_output', 'r') as protein, open('alternative_output', 'w') as alt:
    for line in protein:
        line = line.split('|')
        if not line[5] in junk_list:
            print(line[5], file = alt)
with open('alternative_output','r') as tbu, open('TBU_alternative', 'w') as out:
    for line in tbu:
        line = line.rstrip()
        alter_list.append(line)
        alter_list = ["nan" if x == '' else x for x in alter_list]
    #remove element #736 which is a nan
    alter_list.pop(736)
    for element in alter_list:
        print(element, file = out)
#paste -d '|' TBU_Symbol TBU_uniprot TBU_alternative TBU_homo > TBU_protein-basic
#----------------------------------

#Parsing Hela Spatial Proteome(HSP)

#LFQdeep
gnames_list = []
protnames_list = []
df = pd.read_csv('LFQDeep.csv')
outfile = 'geneNames_output'
df.to_csv(outfile,index=False, sep = '|')
with open('geneNames_output', 'r') as gene, open('prot_Ids', 'w') as prot, open('protnames', 'w') as pnames, open('gnames', 'w') as gname:
    for line in gene:
        line= line.rstrip()
        line = line.split('|')
        gnames_list.append(line[3])
        gnames_list = ["nan" if x == '' else x for x in gnames_list]
        prot_Ids = line[0]
        print(prot_Ids, file = prot)
        prot_names = line[2]
        protnames_list.append(line[2])
        protnames_list = ["nan" if x == '' else x for x in protnames_list]
    for element in gnames_list:
        print(element, file = gname )
    for cell in protnames_list:
        print(cell, file = pnames)
        
paste -d '|' prot_Ids protnames gnames > TBU_LFQdeep    


#LFQFast
count = 0
df = pd.read_csv('LFQ_Fast.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open('transitionfile.csv', 'r') as lfq, open('TBU_LFQ_Fast', 'w') as out:
    for line in lfq:
        line= line.rstrip()
        line = line.split('|')
        prot_Ids = line[0]
        prot_names = line[2]
        gnames = line[3]
        print(prot_Ids, prot_names,gnames, sep='|', file=out)

#TMTDeep
count = 0
df = pd.read_csv('TMTDeep.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open ('transitionfile.csv', 'r') as tmt, open('TBU_TMTdeep', 'w') as out:
    for line in tmt:
        line = line.rstrip()
        prot_Ids = line.split('|')[0]
        protnames = line.split('|')[2]
        gname = line.split('|')[3]
        #count+=1
        print(prot_Ids, protnames,gname, sep='|', file=out)
        
#TMTFast
df = pd.read_csv('TMT_Fast.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open ('transitionfile.csv', 'r') as tmt, open('TBU_TMTfast', 'w') as out:
    for line in tmt:
        line = line.rstrip()
        prot_Ids = line.split('|')[0]
        protnames = line.split('|')[2]
        gname = line.split('|')[3]
        print(prot_Ids, protnames,gname, sep='|', file=out)

#DynamicSilac_deep
count= 0
df = pd.read_csv('DynamicSilac_deep.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open('transitionfile.csv', 'r') as dyn , open('TBU_DYNdeep', 'w') as out:
    for line in dyn:
        line = line.rstrip()
        prot_Ids = line.split('|')[0]
        protnames = line.split('|')[2]
        gname = line.split('|')[3]
        #count+=1
        print(prot_Ids, protnames,gname, sep = '|', file = out)
        
 
#Simulated_deep
count= 0
df = pd.read_csv('SimulatedDynamics_LFQdeep.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open('transitionfile.csv', 'r') as sim , open('TBU_SimulatedDyn_LFQdeep', 'w') as out:
    for line in sim:
        line = line.rstrip()
        prot_Ids = line.split('|')[0]
        protnames = line.split('|')[2]
        gname = line.split('|')[3]
        #count+=1
        print(prot_Ids, protnames,gname, sep = '|', file = out)
        

#Simulated_fast
df = pd.read_csv('SimulatedDynamics_LFQFast.csv')
outfile = 'transitionfile.csv'
df.to_csv(outfile,index=False, sep = '|')
with open('transitionfile.csv', 'r') as sim , open('TBU_SimulatedDyn_LFQFast', 'w') as out:
    for line in sim:
        line = line.rstrip()
        prot_Ids = line.split('|')[0]
        protnames = line.split('|')[2]
        gname = line.split('|')[3]
        print(prot_Ids, protnames,gname, sep = '|', file = out)
        
        
#Organellar markers
# count = 0
df = pd.read_csv('Organellar_markers.csv')
outfile = 'transitionfile'
df.to_csv(outfile,index=False, sep = '|')
with open('transitionfile', 'r') as org, open('TBU_organellar_markers','w') as out:
    #take the first line of the file. h stands for header
    first_line = org.readline()
    #print(first_line)
    hgene_name= first_line.split('|')[0]
    hprotein_name = first_line.split('|')[1]
    hprotein_ID = first_line.split('|')[2]
    hcompartmnet = first_line.split('|')[4]
    print(hgene_name,hprotein_ID,hprotein_name,hcompartmnet, sep = '|', file = out)
    for line in org:
        #I will only print to a the output file the lines that are related to lysosomes.
        #"lyososomes" and "Lysosomes" are not present in file
        if 'lysosome' in line or 'Lysosome' in line: 
            lysosome_line = line.rstrip()
            gene_lysosome = lysosome_line.split('|')[0]
            protname_lysosome = lysosome_line.split('|')[1]
            protId_lysosome = lysosome_line.split('|')[2]
            comp_lysosome = lysosome_line.split('|')[4]
            print(gene_lysosome,protId_lysosome,protname_lysosome,comp_lysosome, sep = '|', file = out)
            

#Compact HSP with prediction confidence
comp_list=[]
conf_list = []
df = pd.read_csv('Compact_Hela_proteome.csv')
outfile = 'transitionfile'
df.to_csv(outfile,index=False, sep = '|') 
with open('transitionfile', 'r') as org, open('TBU_compact_HSP','w') as out, open('first_cols', 'w') as out2, open('compfile', 'w') as output, open('conffile', 'w') as output2:
    first_line = org.readline()
    hgene_name= first_line.split('|')[0]
    hprotein_ID = first_line.split('|')[1]
    hprotein_name = first_line.split('|')[2]
    hcompartmnet = first_line.split('|')[7]
    hconfidence = first_line.split('|')[8]
    print(hgene_name,hprotein_ID,hprotein_name,hcompartmnet,hconfidence, sep = '|', file = out)

    for line in org:
        if 'lysosome' in line or 'Lysosome' in line: 
            lysosome_line = line.rstrip()
            gene_lysosome = lysosome_line.split('|')[0]
            protId_lysosome = lysosome_line.split('|')[1]
            protname_lysosome = lysosome_line.split('|')[2]
            print(gene_lysosome, protId_lysosome, protname_lysosome, sep = '|', file = out2)
            comp_lysosome = lysosome_line.split('|')[7]
            conf_lysosome = lysosome_line.split('|')[8]
            comp_list.append(comp_lysosome)
            comp_list = ["nan" if x == '' else x for x in comp_list]
            conf_list.append(conf_lysosome)
            conf_list = ['nan' if x == '' else x for x in conf_list]
    for element in comp_list:
        print(element, file = output)
    for element in conf_list:
        print(element, file = output2)
            
#paste -d '|' first_cols compfile conffile >datafile
#cat TBU_compact_HSP datafile > TBU_compact-HSP        
#---------------------------------

#Parsing Yeast Cell Death database (yCellDeath)

count =0
alias_list = []
with open('yApoptosis.csv', 'r', encoding = 'latin1') as csv_file, open('TBU_yApop.csv', 'w') as out:
    first_line = csv_file.readline()
    #list the header
    first_line = first_line.rstrip().split(',')
    #print specific elements
    print(first_line[1], first_line[4], first_line[2], sep = ',', file = out)
    with open('yApoptosis.csv', 'r', encoding = 'latin1') as csv_new, open('geneuniprot','w') as gp,open('alias', 'w') as alias:
        csv_reader = csv.DictReader(csv_new)
        for line in csv_reader:
            gene_name = line['gene_name']
            uniprot = line['uniprot']
            print(gene_name,uniprot, sep = ',', file = gp)
            gene_alias = line['gene_alias']
            alias_list.append(gene_alias.replace('\xa0',''))
            alias_list = ['nan' if x == '' else x for x in alias_list]
        for element in alias_list:
            print(element, file = alias)
            
#paste -d ',' geneuniprot alias > gp_alias.csv
#cat TBU_yApop.csv gp_alias.csv > TBU_yApoptosis.csv
#-------------------------------

#Parsing Protein Atlas(all lysosome data)

count = 0
myDict = {} # will hold gene name and synonyms
mylist = [] # will hold synonyms
myDict2 = {} #will hold gene name and uniprot IDs
mylist2 = [] #will hold uniprot Ids
with open('proteinAtlasLysosome.xml', 'r') as xml, open('gene_syn','w') as out, open('gene_uni', 'w') as output:
    for line in xml:
        line = line.rstrip()
        if '<name>' in line:
            line = line.split('<')[1]
            #get the gene_name
            gene_name = line.split('>')[1]
            #empty the list from the previous synonym to append a new one.
            mylist=[]
            mylist2=[]
            #some gene names do not have synonyms so I replace the synonym space with 'nan'. If I don't write this line, the gene names that do not have synonyms won't be added to myDict.
            myDict[gene_name] = 'nan'
            #same for uniprot IDs
            myDict2[gene_name] = 'nan'
        elif '<synonym>' in line:
            line = line.split('<')[1]
            pre_syn = line.split('>')[1]
            synonym= pre_syn.split('<')[0]
            #mylist is where I will store synonyms 
            mylist.append(synonym)
            #since one gene_name can have multiple synonyms so I have to join mylist for each synonyms set
            synonyms = ','.join(mylist)
            #store the synonyms for each gene_name
            myDict[gene_name] = synonyms        
        elif 'Uniprot' in line:
            pre_uni = line.split(' ')[1]
            uniprot = line.split('"')[1]
            #some gene names have more that 1 uniprot ID
            mylist2.append(uniprot)
            uniprot_IDs = ','.join(mylist2)
            myDict2[gene_name] = uniprot_IDs
    for key,value in myDict2.items(): # I could have said print(value) since I only want the uniprot. But that's for sanity check.
        print(key,value,sep = ';', file = output)
    #print them in this from:SNAPIN;BLOC1S7,BORCS3,SNAPAP
    for key,value in myDict.items():
        print(key,value,sep = ';', file = out)

####continue the rest of the code on bash####:
# echo 'gene_name' 'synonym' 'Uniprot' | tr ' ' ';' > headers
# cat gene_uni | cut -d ';' -f2 > uniIds
# paste -d ';' gene_syn uniIds > proteinAtlasFile
# cat headers proteinAtlasFile > proteinAtlasLysosome1


count = 0
syn_list = []
syn_list2 = []
syn_list3 = []
with open('proteinAtlasLysosomeS.tsv') as lyso, open('proteinAtlasLysosomAl.tsv') as lyso2, open('proteinAtlasLysosomeVesicle.tsv') as ves,open('prefinalProteinAtlas', 'w') as out:
    for line in lyso:
        line=line.rstrip()
        line=line.split('\t')
        if not 'Gene' in line:
            syn_list = []
            gname = line[0]
            synonyms = line[1]
            syn_list.append(synonyms)
            synonyms = ['nan' if x == '' else x for x in syn_list]
            for element in synonyms:
                element = element.split('"')
                element = list(filter(None,element))
            synonyms = ','.join(element)
            uniprot = line[4]
            uniprot = uniprot.split('"')
            uniprot = list(filter(None,uniprot))
            uniprot = ','.join(uniprot)
            print(gname,synonyms,uniprot, sep = ';', file = out)
    for line in lyso2:
        line=line.rstrip()
        line=line.split('\t')
        if not 'Gene' in line:
            syn_list2 = []
            gname = line[0]
            synonyms = line[1]
            syn_list2.append(synonyms)
            synonyms = ['nan' if x == '' else x for x in syn_list2]
            for element in synonyms:
                element = element.split('"')
                element = list(filter(None,element))
            synonyms = ','.join(element)
            uniprot = line[4]
            uniprot = uniprot.split('"')
            uniprot = list(filter(None,uniprot))
            uniprot = ','.join(uniprot)
            print(gname,synonyms,uniprot,sep = ';', file = out)
    for line in ves:
        line=line.rstrip()
        if not 'Gene' in line:
            if 'Lysosomes' in line or 'lysosomes' in line or 'lysosome' in line or 'Lysosome' in line or 'lysosomal' in line or 'Lysosomal' in line:
                line=line.split('\t')
                syn_list3 = []
                gname = line[0]
                synonyms = line[1]
                syn_list3.append(synonyms)
                synonyms = ['nan' if x == '' else x for x in syn_list3]
                for element in synonyms:
                    element = element.split('"')
                    element = list(filter(None,element))
                synonyms = ','.join(element)
                uniprot = line[4]
                uniprot = uniprot.split('"')
                uniprot = list(filter(None,uniprot))
                uniprot = ','.join(uniprot)
                print(gname,synonyms,uniprot,sep = ';', file = out)

            
  #cat proteinAtlasLysosome1 prefinalProteinAtlas > TBU_proteinAtlasLysosome         
#------------------------------------

#Parsing Human Lysosome Gene database

count = 0
symbol_list =[]
with open('HumanLysosomeGene_table', 'r') as table, open ('symbol', 'w') as symb, open('name','w' ) as nam:
    for line in table:
        line=line.rstrip()
        line=line.split(';')
        symbol = line[0]
        name = line[1]
        print(name, file = nam)
        symbol_list.append(symbol)
        #some references are printed with the name creating an empty line in the list of symbols. 
        #replace the empty line with nan (this will be eliminated at later steps)
        symbol_list = ['nan' if x == '' else x for x in symbol_list]
    for element in symbol_list:
            print(element, file = symb)
with open('prefinal_HLG', 'r') as pre, open ('TBU_HumanLysosomeGene_DB', 'w') as tbu:
    for line in pre:
        line= line.rstrip()
        if not line.startswith('nan'):
            print(line,file = tbu)
#-----------------------------------

#Parsing goa_uniprot_all.gaf

#This code takes a long time to finish
list_autophagy = ['autophagy', 'Autophagy', 'autophagosome', 'Autophagosome',"autophagocytosis",'Autophagocytosis']
list_lysosomes = ['lysosome', 'Lysosome', 'Lysosomes', 'Lysosome', 'lysosomal', 'Lysosomal']
list_cellDeath = ['cell death', 'Cell Death','apoptosis', 'Apoptosis', 'programmed', 'Programmed']

with open('goa_uniprot_all.gaf', 'r') as goa, open('autophagy_lines','w') as auto,open('lysosome_lines','w') as lys, open('cellD_lines','w') as cell:
    for line in goa:
        line=line.rstrip()
    for element in list_autophagy:
        if element in line:
            print(line, file = auto)
    for keyword in list_lysosomes:
        if keyword in line:
            print(line, file = lys)
    for vocab in list_cellDeath:
        if vocab in line:
            print(line,file=cell)
            
 
#Continuation on the output files.

#start with autophagy_lines
set1 = set()
with open('autophagy_lines','r') as auto, open('TBU_autophagy','w') as out:
    for line in auto:
        line=line.rstrip()
        uniprot_ID=line.split('\t')[1]
        symbol = line.split('\t')[2]
        gene_OR_geneproduct_name = line.split('\t')[9]
        synonym = line.split('\t')[10]
        #this can be also done using nested dictionaries (it will take unique key-value pairs)
        #create a frozenset inside the big set
        if frozenset({uniprot_ID,symbol,gene_OR_geneproduct_name,synonym}) in set1:
            #If the line is in the set continue to the next line, if not then print it
            continue
        else:
            #this is to print the first line of the file
            print(uniprot_ID, symbol,gene_OR_geneproduct_name,synonym,sep =";", file = out)
            #add it to frozenset to avoid duplicates
            set1.add(frozenset({uniprot_ID, symbol,gene_OR_geneproduct_name,synonym}))

#echo 'Uniprot_ID' 'Symbol' 'DB_Object_name' 'Synonym' | tr ' ' ';' > headers
#cat headers TBU-autophagy > TBU_autophagy


#Continue with lysosome_lines and cellD_lines

#remove empty synonyms
mylist = []
with open('TBU-lysosome') as tbu, open('prefinal_lysosome', 'w') as pre, open('synonyms_lysosome', 'w') as output:
    for line in tbu:
        line=line.rstrip()
        line = line.split(';')
        uniprot = line[0]
        symbol = line[1]
        name = line[2]
        print(uniprot,symbol,name, sep = ';', file = pre)
        synonym = line[3]
        mylist.append(synonym)
        mylist = ['nan' if x == '' else x for x in mylist]
    for element in mylist:
        print(element, file = output)
    
#paste -d ';' prefinal_lysosome synonyms_lysosome > lysosome
#cat headers lysosome > TBU_lysosome


set3 = set()
with open('cellD_lines','r') as cell, open('TBU-cellDeath','w') as out:
    for line in cell:
        line=line.rstrip()
        uniprot_ID=line.split('\t')[1]
        symbol = line.split('\t')[2]
        gene_OR_geneproduct_name = line.split('\t')[9]
        synonym = line.split('\t')[10]
        if frozenset({uniprot_ID,symbol,gene_OR_geneproduct_name,synonym}) in set3:
            continue
        else:
            print(uniprot_ID, symbol,gene_OR_geneproduct_name,synonym,sep =";", file = out)
            set3.add(frozenset({uniprot_ID, symbol,gene_OR_geneproduct_name,synonym}))
            
#cat headers TBU-cellDeath | grep -v '^URS'> TBU_cellDeath
#---------------------------------


