#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO MAP SCREEN HITS TO AUTOPHAGY, CELL DEATH, AND LYSOSOME LISTS.
#
#---------------------------------

# Mapping to Autophagy, reviewed

auto_dict = {}
sample_dict = {}
count= 0
for name in ('_sampleAND0.85', '_sampleAND0.75', '_sampleOR0.75'):
    with open('EntrezID_for_Fullreviewed'+name, 'r') as sample, open('Final_Clean_Autophagy_Data', 'r') as auto, open('MappedSampleToAuto_reviewed'+name, 'w') as out:
        print('Uniprot', 'Entrez ID', 'Symbol', 'Synonym', 'Protein Name', 'Organism', sep = '\t', file = out)
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez
        for line in auto:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                auto_dict[uniprot]= {}
                symbol = line[1]
                auto_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                auto_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                auto_dict[uniprot]['protname'] = protname
                org = line[4]
                auto_dict[uniprot]['organism'] = org
        for key in sample_dict:
            if key in auto_dict:
                print(key,sample_dict[key],auto_dict[key]['symbol'], auto_dict[key]['synonym'], auto_dict[key]['protname'],auto_dict[key]['organism'], sep = '\t', file = out)
#------------------------------

# Mapping to cell death, reviewed

CD_dict = {}
sample_dict = {}
count= 0
for name in ('_sampleAND0.85', '_sampleAND0.75', '_sampleOR0.75'):
    with open('EntrezID_for_Fullreviewed'+name, 'r') as sample, open('Final_Clean_CellDeath_Data', 'r') as CD, open('MappedSampleToCD_reviewed'+name, 'w') as out:
        print('Uniprot', 'Entrez ID', 'Symbol', 'Synonym', 'Protein Name', 'Organism', sep = '\t', file = out)
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez
        for line in CD:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                CD_dict[uniprot]= {}
                symbol = line[1]
                CD_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                CD_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                CD_dict[uniprot]['protname'] = protname
                org = line[4]
                CD_dict[uniprot]['organism'] = org
        for key in sample_dict:
            if key in CD_dict:
                print(key,sample_dict[key],auto_dict[key]['symbol'], CD_dict[key]['synonym'], CD_dict[key]['protname'],CD_dict[key]['organism'], sep = '\t', file = out)
#-------------------------------

#Continue mapping to lysosomes, reviewed

sample_dict = {}
lys_dict = {}
count= 0
for name in ('_sampleAND0.85', '_sampleAND0.75', '_sampleOR0.75'):
    with open('EntrezID_for_Fullreviewed'+name, 'r') as sample, open('Final_Clean_Lysosome_Data') as lys, open('MappedSampleToLys_reviewed'+name, 'w') as out:
        print('Uniprot', 'Entrez ID', 'Symbol', 'Synonym', 'Protein Name', 'Organism', sep = '\t', file = out)
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez
        for line in lys:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                lys_dict[uniprot]= {}
                symbol = line[1]
                lys_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                lys_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                lys_dict[uniprot]['protname'] = protname
                org = line[4]
                lys_dict[uniprot]['organism'] = org           
        for key in sample_dict:
            if key in lys_dict:
                print(key,sample_dict[key],lys_dict[key]['symbol'], lys_dict[key]['synonym'], lys_dict[key]['protname'],lys_dict[key]['organism'], sep = '\t', file = out)
#-------------------------------

Map to Autophagy list, unreviewed 

#use this code for github. change the database name
auto_dict = {}
sample_dict = {}
count= 0
for name in ('_sampleAND0.85', '_sampleAND0.75', '_sampleOR0.75'):
    with open('EntrezID_for_Fullunreviewed'+name, 'r') as sample, open('ALL_Unreviewed_Autophagy', 'r') as auto, open('MappedSampleToAuto_Unreviewed'+name, 'w') as out:
        print('Uniprot', 'Entrez ID', 'Symbol', 'Synonym', 'Protein Name', 'Organism', sep = '\t', file = out)
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez
        for line in auto:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                auto_dict[uniprot]= {}
                symbol = line[1]
                auto_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                auto_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                auto_dict[uniprot]['protname'] = protname
                org = line[4]
                auto_dict[uniprot]['organism'] = org
        for key in sample_dict:
            if key in auto_dict:
                print(key,sample_dict[key],auto_dict[key]['symbol'], auto_dict[key]['synonym'], auto_dict[key]['protname'],auto_dict[key]['organism'], sep = '\t', file = out)
 #-----------------------------
 
 #Map to lysosomes list, unreviewed
            
 sample_dict = {}
lys_dict = {}
count= 0
for name in ('_sampleAND0.85', '_sampleAND0.75', '_sampleOR0.75'):
    with open('EntrezID_for_Fullunreviewed'+name, 'r') as sample, open('ALL_Unreviewed_lysosome') as lys, open('MappedSampleToLys_Unreviewed'+name, 'w') as out:
        print('Uniprot', 'Entrez ID', 'Symbol', 'Synonym', 'Protein Name', 'Organism', sep = '\t', file = out)
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez
        for line in lys:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                lys_dict[uniprot]= {}
                symbol = line[1]
                lys_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                lys_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                lys_dict[uniprot]['protname'] = protname
                org = line[4]
                lys_dict[uniprot]['organism'] = org           
        for key in sample_dict:
            if key in lys_dict:
                print(key,sample_dict[key],lys_dict[key]['symbol'], lys_dict[key]['synonym'], lys_dict[key]['protname'],lys_dict[key]['organism'], sep = '\t', file = out)
#-----------------------------

#Map to cell death list, unreviewed

sample_dict = {}
CD_dict = {}
count= 0
for name in ('_sampleAND0.75', '_sampleOR0.75', '_sampleAND0.85'):
    with open('EntrezID_for_Fullunreviewed'+name, 'r') as sample, open('ALL_Unreviewed_CD') as CD, open('MappedSampleToCD_Unreviewed'+name, 'w') as out:
        for line in sample:
            if not 'From' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                entrez = line[1]
                sample_dict[uniprot] = entrez                
        for line in CD:
            if not 'Uniprot' in line:
                line = line.rstrip()
                line = line.split('\t')
                uniprot = line[0]
                CD_dict[uniprot]= {}
                symbol = line[1]
                CD_dict[uniprot]['symbol'] = symbol
                synonym = line[2]
                CD_dict[uniprot]['synonym'] = synonym
                protname = line[3]
                CD_dict[uniprot]['protname'] = protname
                org = line[4]
                CD_dict[uniprot]['organism'] = org           
        for key in sample_dict:
            if key in CD_dict:
                print(key,sample_dict[key],CD_dict[key]['symbol'], CD_dict[key]['synonym'], CD_dict[key]['protname'],CD_dict[key]['organism'], sep = '\t', file = out)
#----------------------------

#Get the files in the final format, unreviewed

sam1_dict = {}
sam2_dict = {}
sam3_dict = {}
count=0

with open('ALL_Entrez_MappedSampleToAuto_Unreviewed') as sam1, open('ALL_Entrez_MappedSampleToCD_Unreviewed') as sam2, open('ALL_Entrez_MappedSampleToLys_Unreviewed') as sam3, open('Prefinal_MappedSamplesToLists_Unreviewed.csv', 'w') as out:
    print('Gene Symbol',  'Entrez ID', 'Uniprot','REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP', 'Confidence Level', 'Present in Autophagy', 'Present in Lysosome', 'Present in Cell Death', sep = ',', file = out)
    for line in sam1:
        if not 'Uniprot' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[2]
            sam1_dict[uniprot] = {}
            symbol = line[0]
            sam1_dict[uniprot]['symbol'] = symbol
            entrez = line[1]
            sam1_dict[uniprot]['entrez'] = entrez
            rep1 = line[3]
            sam1_dict[uniprot]['rep1'] = rep1
            rep2 = line[4]
            sam1_dict[uniprot]['rep2'] = rep2
            aver = line[5]
            sam1_dict[uniprot]['average'] = aver
            conf = line[6]
            sam1_dict[uniprot]['confidence'] = conf
            pres = line[7]
            sam1_dict[uniprot]['present'] = pres
    for line in sam2:
        if not 'Uniprot' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[2]
            sam2_dict[uniprot] = {}
            symbol = line[0]
            sam2_dict[uniprot]['symbol'] = symbol
            entrez = line[1]
            sam2_dict[uniprot]['entrez'] = entrez
            rep1 = line[3]
            sam2_dict[uniprot]['rep1'] = rep1
            rep2 = line[4]
            sam2_dict[uniprot]['rep2'] = rep2
            aver = line[5]
            sam2_dict[uniprot]['average'] = aver
            conf = line[6]
            sam2_dict[uniprot]['confidence'] = conf
            pres = line[7]
            sam2_dict[uniprot]['present'] = pres
    for line in sam3:
        if not 'Uniprot' in line:
            line = line.rstrip()
            line = line.split('\t')
            uniprot = line[2]
            sam3_dict[uniprot] = {}
            symbol = line[0]
            sam3_dict[uniprot]['symbol'] = symbol
            entrez = line[1]
            sam3_dict[uniprot]['entrez'] = entrez
            rep1 = line[3]
            sam3_dict[uniprot]['rep1'] = rep1
            rep2 = line[4]
            sam3_dict[uniprot]['rep2'] = rep2
            aver = line[5]
            sam3_dict[uniprot]['average'] = aver
            conf = line[6]
            sam3_dict[uniprot]['confidence'] = conf
            pres = line[7]
            sam3_dict[uniprot]['present'] = pres
    for key in sam1_dict: #I make sure after each statement that the files have the same confidence levels for a given entry.
        if key in sam2_dict and key in sam3_dict:
            print(sam1_dict[key]['symbol'],sam1_dict[key]['entrez'],key,sam1_dict[key]['rep1'],sam1_dict[key]['rep2'],sam1_dict[key]['average'],sam1_dict[key]['confidence'], 'yes', 'yes', 'yes', sep = ',', file = out)
        elif key in sam2_dict and not key in sam3_dict:
            print(sam1_dict[key]['symbol'],sam1_dict[key]['entrez'],key,sam1_dict[key]['rep1'],sam1_dict[key]['rep2'],sam1_dict[key]['average'],sam1_dict[key]['confidence'], 'yes', 'No', 'yes', sep = ',', file = out)
        elif key in sam3_dict and not key in sam2_dict:
            print(sam1_dict[key]['symbol'],sam1_dict[key]['entrez'],key,sam1_dict[key]['rep1'],sam1_dict[key]['rep2'],sam1_dict[key]['average'],sam1_dict[key]['confidence'], 'yes', 'yes', 'No', sep = ',', file = out)
        else:
            print(sam1_dict[key]['symbol'],sam1_dict[key]['entrez'],key,sam1_dict[key]['rep1'],sam1_dict[key]['rep2'],sam1_dict[key]['average'],sam1_dict[key]['confidence'], 'yes', 'No', 'No', sep = ',',file = out)
    for key in sam2_dict:
        if key in sam3_dict and not key in sam1_dict:
            print(sam2_dict[key]['symbol'],sam2_dict[key]['entrez'],key,sam2_dict[key]['rep1'],sam2_dict[key]['rep2'],sam2_dict[key]['average'],sam2_dict[key]['confidence'], 'No', 'yes', 'yes', sep = ',', file = out)
        elif not key in sam3_dict and not key in sam1_dict:
            print(sam2_dict[key]['symbol'],sam2_dict[key]['entrez'],key,sam2_dict[key]['rep1'],sam2_dict[key]['rep2'],sam2_dict[key]['average'],sam2_dict[key]['confidence'], 'No', 'No', 'yes', sep = ',', file = out)
    for key in sam3_dict:
        if not key in sam2_dict and not key in sam1_dict:
            print(sam3_dict[key]['symbol'],sam3_dict[key]['entrez'],key,sam3_dict[key]['rep1'],sam3_dict[key]['rep2'],sam3_dict[key]['average'],sam3_dict[key]['confidence'], 'No', 'yes', 'No', sep = ',', file = out)

fin_dict = {}
sub_dict = {}
count = 0
with open('Prefinal_MappedSamplesToLists_Unreviewed.csv') as fin, open('sublist_screenModified.csv') as sub, open('Final_MappedSamplesToLists_Unreviewed.csv', 'w') as out:
    print('screen_run',  'plate', 'well','entrez_gene_name','entrez_gene_ID','Uniprot_ID','REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP', 'Confidence Level', 'Present in Autophagy', 'Present in Lysosome', 'Present in Cell Death', sep = ',', file = out)
    for line in fin:
        if not 'Gene' in line:
            line = line.rstrip()
            line=line.split(',')
            entrez = line[1]
            fin_dict[entrez]={}
            uniprot = line[2]
            fin_dict[entrez]['uniprot'] = uniprot
            symbol = line[0]
            fin_dict[entrez]['symbol'] = symbol
            rep1 = line[3]
            fin_dict[entrez]['rep1'] = rep1
            rep2 = line[4]
            fin_dict[entrez]['rep2'] = rep2
            aver = line[5]
            fin_dict[entrez]['average'] = aver
            conf = line[6]
            fin_dict[entrez]['confidence'] = conf
            auto = line[7]
            fin_dict[entrez]['auto'] = auto
            lys = line[8]
            fin_dict[entrez]['lys'] = lys
            CD = line[9]
            fin_dict[entrez]['CD'] = CD
    for line in sub:
        if not 'entrez' in line:
            line = line.rstrip()
            line = line.split(',')
            entrez = line[4]
            run = line[0]
            plate = line[1]
            well = line[2]
            gname = line[3]
            sub_dict[entrez] = {}
            sub_dict[entrez]['run'] = run
            sub_dict[entrez]['plate'] = plate
            sub_dict[entrez]['well'] = well
            sub_dict[entrez]['gname'] = gname
    for key in fin_dict: #all keys are common
        if key in sub_dict:
            print(sub_dict[key]['run'] ,sub_dict[key]['plate'],sub_dict[key]['well'],sub_dict[key]['gname'], key, fin_dict[key]['uniprot'],fin_dict[key]['rep1'], fin_dict[key]['rep2'],fin_dict[key]['average'],fin_dict[key]['confidence'],fin_dict[key]['auto'], fin_dict[key]['lys'],fin_dict[key]['CD'],sep = ',', file = out)
#-------------------------------

#Get the lists in the final format, reviewed

g_dict = {'TMEM133':'143872','CCR2': '729230', 'CNOT6': 'nan', 'CD24':'100133941','SFTPA2':'729238'}
g_list = ['CHRM5', 'KCNH8','PLXNA4']
sub_dict = {}
g_ent = {} #to hold the new genes and entrez IDs
fin_dict = {} # add the new entrez IDs to the prefinal file
with open('sublist_screenModified.csv') as sub, open('Prefinal_MappedSamplesToLists_reviewed.csv') as fin, open('transient_MappedSamplesToLists_reviewed.csv', 'w') as out:
    print('entrez_gene_name', 'entrez_gene_ID','entrez_gene_ID_Uniprot', 'Uniprot_ID','REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP', 'Confidence Level', 'Present in Autophagy', 'Present in Lysosome', 'Present in Cell Death', sep = ',', file = out)
    for line in sub:
         if not 'entrez' in line:
            line = line.rstrip()
            line = line.split(',')
            entrez = line[4]
            gname = line[3] 
            sub_dict[entrez] = gname
    for key,value in sub_dict.items():
        if value in g_dict:
            gname = value
            entrez = key
            g_ent[gname] = entrez
    for line in fin:
        if not 'Uniprot' in line:
            line = line.rstrip()
            line=line.split(',')
            entrez = line[1]
            fin_dict[entrez]={}
            uniprot = line[2]
            fin_dict[entrez]['uniprot'] = uniprot
            symbol = line[0]
            fin_dict[entrez]['symbol'] = symbol
            rep1 = line[3]
            fin_dict[entrez]['rep1'] = rep1
            rep2 = line[4]
            fin_dict[entrez]['rep2'] = rep2
            aver = line[5]
            fin_dict[entrez]['average'] = aver
            conf = line[6]
            fin_dict[entrez]['confidence'] = conf
            auto = line[7]
            fin_dict[entrez]['auto'] = auto
            lys = line[8]
            fin_dict[entrez]['lys'] = lys
            CD = line[9]
            fin_dict[entrez]['CD'] = CD
    for key, value in fin_dict.items():
        if value['symbol'] in g_ent and value['symbol'] in g_dict:
            if g_dict[value['symbol']] == 'nan':
                g_dict[value['symbol']]=g_dict[value['symbol']].replace('nan', 'empty')
            print(value['symbol'], g_ent[value['symbol']], g_dict[value['symbol']], fin_dict[key]['uniprot'],fin_dict[key]['rep1'], fin_dict[key]['rep2'],fin_dict[key]['average'],fin_dict[key]['confidence'],fin_dict[key]['auto'], fin_dict[key]['lys'],fin_dict[key]['CD'], sep = ',', file = out)
        else:
            print(fin_dict[key]['symbol'],key, key, fin_dict[key]['uniprot'], fin_dict[key]['rep1'], fin_dict[key]['rep2'],fin_dict[key]['average'],fin_dict[key]['confidence'],fin_dict[key]['auto'], fin_dict[key]['lys'],fin_dict[key]['CD'], sep = ',', file = out)
            

fin_dict= {}
sub_dict = {}
count= 0
key_dict = {}

with open('transient_MappedSamplesToLists_reviewed.csv') as fin, open('sublist_screenModified.csv') as sub, open('Final_MappedSamplesToLists_reviewed.csv', 'w') as out:
    print('screen_run', 'plate','well','entrez_gene_name', 'Uniprot_gene_name','entrez_gene_ID','entrez_gene_ID_Uniprot', 'Uniprot_ID','REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP', 'Confidence Level', 'Present in Autophagy', 'Present in Lysosome', 'Present in Cell Death', sep = ',', file = out)
    for line in fin:
        if not 'Uniprot' in line:
            line = line.rstrip()
            line=line.split(',')
            symbol = line[0]
            fin_dict[symbol]={}
            entrez1 = line[1]
            fin_dict[symbol]['entrez1'] = entrez1
            entrez2 = line[2]
            fin_dict[symbol]['entrez2'] = entrez2
            uniprot = line[3]
            fin_dict[symbol]['uniprot'] = uniprot
            rep1 = line[4]
            fin_dict[symbol]['rep1'] = rep1
            rep2 = line[5]
            fin_dict[symbol]['rep2'] = rep2
            aver = line[6]
            fin_dict[symbol]['average'] = aver
            conf = line[7]
            fin_dict[symbol]['confidence'] = conf
            auto = line[8]
            fin_dict[symbol]['auto'] = auto
            lys = line[9]
            fin_dict[symbol]['lys'] = lys
            CD = line[10]
            fin_dict[symbol]['CD'] = CD
    for line in sub:
        if not 'entrez' in line:
            line = line.rstrip()
            line = line.split(',')
            gname = line[3]
            sub_dict[gname] = {}
            entrez = line[4]
            sub_dict[gname]['entrez'] = entrez
            run = line[0]
            sub_dict[gname]['run'] = run
            plate = line[1]
            sub_dict[gname]['plate'] = plate
            well = line[2]
            sub_dict[gname]['well'] = well
    for key in fin_dict:
        if key in sub_dict:
            print(sub_dict[key]['run'],sub_dict[key]['plate'], sub_dict[key]['well'],key,key,fin_dict[key]['entrez1'],fin_dict[key]['entrez2'],fin_dict[key]['uniprot'], fin_dict[key]['rep1'], fin_dict[key]['rep2'],fin_dict[key]['average'],fin_dict[key]['confidence'],fin_dict[key]['auto'], fin_dict[key]['lys'],fin_dict[key]['CD'],sep = ',', file = out)
        else:
            entrez1 = fin_dict[key]['entrez1']
            entrez2 = fin_dict[key]['entrez2']
            uniprot = fin_dict[key]['uniprot']
            rep1 = fin_dict[key]['rep1']
            rep2 = fin_dict[key]['rep2']
            aver = fin_dict[key]['average']
            conf = fin_dict[key]['confidence']
            auto = fin_dict[key]['auto']
            lys =  fin_dict[key]['lys']
            CD = fin_dict[key]['CD']
            key_dict[entrez1] = {}
            key_dict[entrez1]['key'] = key
            key_dict[entrez1]['entrez2'] = entrez2
            key_dict[entrez1]['uniprot'] = uniprot
            key_dict[entrez1]['rep1'] = rep1
            key_dict[entrez1]['rep2'] = rep2
            key_dict[entrez1]['average'] = aver
            key_dict[entrez1]['confidence'] = conf
            key_dict[entrez1]['auto'] = auto
            key_dict[entrez1]['lys'] = lys
            key_dict[entrez1]['CD'] = CD
    for key,value in sub_dict.items(): # key is the entrez unofficial gene name 
        #check if entrez IDs are in key_dict (for the unofficial names)
        if value['entrez'] in key_dict: #key_dict[value['entrez']]['key'] is the gene name from uniprot (i.e. official gene name)
            print(sub_dict[key]['run'],sub_dict[key]['plate'], sub_dict[key]['well'], key, key_dict[value['entrez']]['key'], value['entrez'], key_dict[value['entrez']]['entrez2'],key_dict[value['entrez']]['uniprot'],key_dict[value['entrez']]['rep1'],key_dict[value['entrez']]['rep2'], key_dict[value['entrez']]['average'],key_dict[value['entrez']]['confidence'], key_dict[value['entrez']]['auto'], key_dict[value['entrez']]['lys'], key_dict[value['entrez']]['CD'],sep = ',', file = out )
 #------------------------------ 
