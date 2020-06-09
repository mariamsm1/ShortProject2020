#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO CHECK FOR THE OVERLAP BETWEEN ALL DATABASES.
#
#---------------------------------

#Autophagy and cell death

auto_dict = {}
cd_dict = {}
count =0
with open('Final_Clean_Autophagy_Data') as auto, open('Final_Clean_CellDeath_Data') as cd, open('OverlapAutoCD', 'w') as out:
    print('AutoCD_Uniprot', 'AutoCD_Symbol', 'AutoCD_Synonym', 'AutoCD_Protname', 'AutoCD_Organism', sep = '\t', file = out)
    lines = auto.readlines()[1:]
    for line in lines:
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
    lines = cd.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        cd_dict[uniprot]= {}
        symbol = line[1]
        cd_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        cd_dict[uniprot]['synonym'] = synonym
        protname = line[3]
        cd_dict[uniprot]['protname'] = protname
        org = line[4]
        cd_dict[uniprot]['organism'] = org
    for key in auto_dict:
        if key in cd_dict: 
            count+=1
            print(key,auto_dict[key]['symbol'],auto_dict[key]['synonym'],auto_dict[key]['protname'], auto_dict[key]['organism'], sep = '\t', file = out)
    
#Same script is used for autophagy and lysosome, replace "Final_Clean_CellDeath_Data" with "Final_Clean_Lysosome_Data".
#Same script is used for lysosome and cell death. Use "Final_Clean_CellDeath_Data" and "Final_Clean_Lysosome_Data".
#-------------------------------------

#Check for overlap between the three categories.

cd_dict = {}
lys_dict = {}
auto_dict = {}
count =0
with open('Final_Clean_CellDeath_Data') as cd, open('Final_Clean_Lysosome_Data') as lys, open('Final_Clean_Autophagy_Data') as auto, open('OverlapCDLysAuto', 'w') as out:
    print('CDLysAuto_Uniprot', 'CDLysAuto_Symbol', 'CDLysAuto_Synonym', 'CDLysAuto_Protname', 'CDLysAuto_Organism', sep = '\t', file = out)
    lines = cd.readlines()[1:]
    for line in lines:
        line = line.rstrip()
        line = line.split('\t')
        uniprot = line[0]
        cd_dict[uniprot]= {}
        symbol = line[1]
        cd_dict[uniprot]['symbol'] = symbol
        synonym = line[2]
        cd_dict[uniprot]['synonym'] = synonym
        protname = line[3]
        cd_dict[uniprot]['protname'] = protname
        org = line[4]
        cd_dict[uniprot]['organism'] = org
    lines = lys.readlines()[1:]
    for line in lines:
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
    lines = auto.readlines()[1:]
    for line in lines:
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
    for key in auto_dict:
        if key in lys_dict and key in cd_dict: #126 genes in common
            print(key,auto_dict[key]['symbol'],auto_dict[key]['synonym'],auto_dict[key]['protname'], auto_dict[key]['organism'], sep = '\t', file = out)
 #------------------------------
    
