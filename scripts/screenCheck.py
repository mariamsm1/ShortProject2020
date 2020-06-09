#MARIAM MIARI
#
#2020-2021
#
#SCRIPT FOR GENOME-WIDE SCREEN CHECK.
#
#---------------------------------

#create a sublist of the original file

import csv
count= 0
with open('control_cumulative_all_data.csv', 'r') as csv_file, open('sublist_screen.csv', 'w') as out, open('cellcount_rep1_or_rep2_0.8.csv', 'w') as output1, open('cellcount_rep1_and_rep2_0.8.csv', 'w') as output2:
    csv_reader = csv.DictReader(csv_file)
    print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = out)
    print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = output1)
    print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = output2)
    for line in csv_reader:
        srun = line['screen.run']#22269
        plate = line['plate']
        well = line['well']
        entname = line['entrez.gene.name']
        entID = line['entrez.gene.ID']
        rep1 = line['REP1.cell.count.normalised.to.OTP']
        rep2 = line['REP2.cell.count.normalised.to.OTP']
        zscore = line['average.cell.count.normalised.to.OTP.robust.z.scored']
        avOTP = line['average.cell.count.normalised.to.OTP']
        ave = line['average.cell.count']
        print(srun,plate,well,entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = out)
        if rep1 <= '0.8' or rep2 <='0.8': #if any of the two replicates had at least 20% reduction in cell count
            print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output1)
        if rep1 <='0.8' and rep2 <= '0.8': #if both replicates had at least 20% reduction in cell count
            print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output2)
#--------------------------

#list of rows of "OR" not "AND"
count = 0
csv1=set(open(r'cellcount_rep1_or_rep2_0.8.csv'))
csv2 = set(open(r'cellcount_rep1_and_rep2_0.8.csv'))
out = open('cellcount_rep1_orNOTand_rep2_0.8.csv', 'w') 
print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = out)

for line in csv1:
    if not line in csv2: #4234 wells had reduction in cell count
        line = line.rstrip()
        print(line,sep = ',', file = out)
#---------------------------

#split the files above to control and samples

count = 0
ctrl_list = ['01', '02', '23', '24']
for names in ('cellcount_rep1_or_rep2_0.8', 'cellcount_rep1_and_rep2_0.8', 'cellcount_rep1_orNOTand_rep2_0.8'):
    with open(names+'.csv') as csv, open(names+'control.csv', 'w') as out1, open(names+'sample.csv', 'w') as out2:
        print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = out1)
        print('screen.run', 'plate', 'well', 'entrez.gene.name','entrez.gene.ID', 'REP1.cell.count.normalised.to.OTP', 'REP2.cell.count.normalised.to.OTP', 'average.cell.count.normalised.to.OTP.robust.z.scored', 'average.cell.count.normalised.to.OTP', 'average.cell.count', sep = ',', file = out2)
        for line in csv:
            line = line.rstrip()
            line = line.split(',')
            well = line[2][1:]
            if well in ctrl_list:
                line = ','.join(line)
                print(line,file = out1) #1722 controls
            else:
                line = ','.join(line)
                if not 'entrez' in line: #12580 samples
                    print(line,file = out2)
#-----------------------------

#find the number of wells (i.e. the count of controls) through which controls had rep1,rep2 <= 0.8 in a certain plate.
#e.g. plate 1 had 5 times in which KIF11 was <=0.8 in rep1 and 5 times in which it was <=0.8 in rep2. Also plate1 had 0 times in which mock was <=0.8 in rep1 and 1 times in which it was <=0.8 in rep2.

import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("cellcount_rep1_or_rep2_0.8control.csv") 
out = open('cellcount_rep1_or_rep2_0.8controlCounts.csv', 'w')
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
        target1 = len(datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.8])
        target2 = len(datagene.loc[datagene.REP2_cell_count_normalised_to_OTP<=0.8])
        print(plate[i], genes[j], target1,target2, sep = ',', file = out)
    #print the genes that do not have rep1 or rep2 in a certain plate. (important for scatter plot)
    for element in genes_list:
        if not element in genes:
            print(plate[i], element, '0', '0', sep = ',', file = out)
#-----------------------------            
