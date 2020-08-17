#MARIAM MIARI
#
#2020-2021
#
#SCRIPT FOR PLOTTING POSITIVE AND NEGATIVE CONTROLS FROM THE SCREEN DATA.
#
#---------------------------------

import pandas as pd 
  
# The file generated is used in plotting rep1 and rep2.
# Creating the dataframe
df = pd.read_csv("cellcount_rep1_or_rep2_0.75controlmodified.csv") 
out = open('cellcount_rep1_or_rep2_0.75controlCounts.csv', 'w')
print('plate', 'control', 'REP1', 'REP2', sep = ',', file = out)
#save all the unique plates to variable "plate"
plate = df.plate.unique()
#get all unique genes in the file
genes_list = df.entrez_gene_name.unique()
for i in range(len(plate)):
    #print(plate[i])
    #loc locates rows that are under the condition. here it checks which rows have plate same as plates in the loop
    data = df.loc[df.plate == plate[i]]
    #look for genes in that plate
    genes = data.entrez_gene_name.unique()
    for j in range(len(genes)):
        #locate the rows that has entrez gene names the same as the names in the loop for each plate number
        datagene = data.loc[data.entrez_gene_name == genes[j]]          
        #do the count for each condition
        target1 = len(datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.75])
        target2 = len(datagene.loc[datagene.REP2_cell_count_normalised_to_OTP<=0.75])
        print(plate[i], genes[j], target1,target2, sep = ',', file = out)
    #print the genes that do not have rep1 or rep2 in a certain plate. (important for scatter plot)
    for element in genes_list:
        if not element in genes:
            print(plate[i], element, '0', '0', sep = ',', file = out)
            
        
#plot rep1
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_or_rep2_0.75controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP1, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP1, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP1, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP1, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP1, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP1, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'], prop={"size":15},loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep1_OR0.75.png')


#plot rep2
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_or_rep2_0.75controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP2, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP2, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP2, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP2, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP2, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP2, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'], prop={"size":15},loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep2_OR0.75.png')    
#------------------------------------

import pandas as pd 

# The file generated is used in plotting rep1 and rep2.  
# Creating the dataframe  
df = pd.read_csv("cellcount_rep1_and_rep2_0.75control.csv") 
out = open('cellcount_rep1_and_rep2_0.75controlCounts.csv', 'w')
print('plate', 'control', 'REP1', 'REP2', sep = ',', file = out)
#save all the unique plates to variable "plate"
plate = df.plate.unique()
#get all unique genes in the file
genes_list = df.entrez_gene_name.unique()
for i in range(len(plate)):
    #print(plate[i])
    #loc locates rows that are under the condition. here it checks which rows have plate same as plates in the loop
    data = df.loc[df.plate == plate[i]]
    #look for genes in that plate
    genes = data.entrez_gene_name.unique()
    for j in range(len(genes)):
        #locate the rows that has entrez gene names the same as the names in the loop for each plate number
        datagene = data.loc[data.entrez_gene_name == genes[j]]          
        #do the count for each condition
        target1 = len(datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.75])
        target2 = len(datagene.loc[datagene.REP2_cell_count_normalised_to_OTP<=0.75])
        print(plate[i], genes[j], target1,target2, sep = ',', file = out)
    #print the genes that do not have rep1 or rep2 in a certain plate. (important for scatter plot)
    for element in genes_list:
        if not element in genes:
            print(plate[i], element, '0', '0', sep = ',', file = out)
            


#plot rep1
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_and_rep2_0.75controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP1, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP1, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP1, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP1, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP1, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP1, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'], prop={"size":15},loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep1_AND0.75.png')


#plot rep2
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_and_rep2_0.75controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP2, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP2, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP2, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP2, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP2, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP2, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'],prop={"size":15}, loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep2_AND0.75.png')        
#------------------------------------

import pandas as pd 

# The file generated is used in plotting rep1 and rep2. 
# Creating the dataframe  
df = pd.read_csv("cellcount_rep1_and_rep2_0.85control.csv") 
out = open('cellcount_rep1_and_rep2_0.85controlCounts.csv', 'w')
print('plate', 'control', 'REP1', 'REP2', sep = ',', file = out)
#save all the unique plates to variable "plate"
plate = df.plate.unique()
#get all unique genes in the file
genes_list = df.entrez_gene_name.unique()
for i in range(len(plate)):
    #print(plate[i])
    #loc locates rows that are under the condition. here it checks which rows have plate same as plates in the loop
    data = df.loc[df.plate == plate[i]]
    #look for genes in that plate
    genes = data.entrez_gene_name.unique()
    for j in range(len(genes)):
        #locate the rows that has entrez gene names the same as the names in the loop for each plate number
        datagene = data.loc[data.entrez_gene_name == genes[j]]          
        #do the count for each condition
        target1 = len(datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.75])
        target2 = len(datagene.loc[datagene.REP2_cell_count_normalised_to_OTP<=0.75])
        print(plate[i], genes[j], target1,target2, sep = ',', file = out)
    #print the genes that do not have rep1 or rep2 in a certain plate. (important for scatter plot)
    for element in genes_list:
        if not element in genes:
            print(plate[i], element, '0', '0', sep = ',', file = out)
            


#plot rep1
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_and_rep2_0.85controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP1, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP1, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP1, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP1, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP1, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP1, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'],prop={"size":15},loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep1_AND0.85.png')


#plot rep2
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("cellcount_rep1_and_rep2_0.85controlCounts.csv") 
#locate the rows in which each of these genes is present
gene1 = df.loc[df.control == 'siPLK1']
gene2 = df.loc[df.control=='KIF11']
gene3 = df.loc[df.control=='OTP']
gene4 = df.loc[df.control == 'mock']
gene5 = df.loc[df.control == 'untransfected']
gene6 = df.loc[df.control=='LIPA']
plt.scatter(gene1.plate.astype("|S"), gene1.REP2, marker = '^')
plt.scatter(gene2.plate.astype("|S"), gene2.REP2, marker = 'x')
plt.scatter(gene3.plate.astype("|S"), gene3.REP2, marker = 'o')
plt.scatter(gene4.plate.astype("|S"), gene4.REP2, marker = '*')
plt.scatter(gene5.plate.astype("|S"), gene5.REP2, marker = 'v')
plt.scatter(gene6.plate.astype("|S"), gene6.REP2, marker = '+')
plt.legend(['siPLK1','KIF11','OTP','mock','untransfected','LIPA'], prop={"size":15}, loc = 'center left')
plt.xticks(rotation=90)
plt.rcParams["figure.figsize"] = (20,7)
plt.rcParams.update({'font.size': 15})
plt.savefig('Rep2_AND0.85.png')        
#-----------------------------------
