#MARIAM MIARI
#
#2020-2021
#
#SCRIPT FOR SPLITTING CONTROLS AND SAMPLES TO 3 CONFIDENCE LEVELS(HIGH/MODERATE/LOW).
#
#---------------------------------

#extract the columns needed

import csv
count= 0
ctrl_list = ['01', '02', '23', '24']

with open('control_cumulative_all_data.csv', 'r') as csv_file, open('sublist_screenModified.csv', 'w') as out, open('sublist_screenModified_controls.csv', 'w') as output1, open('sublist_screenModified_samples.csv', 'w') as output2, open('cellcount_rep1_and_rep2_0.85control.csv', 'w') as output3, open('cellcount_rep1_and_rep2_0.75control.csv', 'w') as output4, open('cellcount_rep1_or_rep2_0.75control.csv', 'w') as output5, open('cellcount_rep1_and_rep2_0.85sample.csv', 'w') as output6, open('cellcount_rep1_and_rep2_0.75sample.csv', 'w') as output7, open('cellcount_rep1_or_rep2_0.75sample.csv', 'w') as output8:
    csv_reader = csv.DictReader(csv_file)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = out)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output1)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output2)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output3)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output4)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output5)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output6)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output7)
    print('screen_run', 'plate', 'well', 'entrez_gene_name','entrez_gene_ID', 'REP1_cell_count_normalised_to_OTP', 'REP2_cell_count_normalised_to_OTP', 'average_cell_count_normalised_to_OTP_robust_z_scored', 'average_cell_count_normalised_to_OTP', 'average_cell_count', sep = ',', file = output8)
    for line in csv_reader:
        srun = line['screen.run']
        plate = line['plate']
        well = line['well']
        wellM = well[1:3]
        entname = line['entrez.gene.name']
        entID = line['entrez.gene.ID']
        rep1 = line['REP1.cell.count.normalised.to.OTP']
        rep2 = line['REP2.cell.count.normalised.to.OTP']
        zscore = line['average.cell.count.normalised.to.OTP.robust.z.scored']
        avOTP = line['average.cell.count.normalised.to.OTP']
        ave = line['average.cell.count']
        print(srun,plate,well,entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = out)
        if wellM in ctrl_list: # get control wells
            print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output1)
            if rep1 <= '0.85' and rep2 <='0.85': #get moderate confidence level
                print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output3)
            if rep1 <= '0.75' and rep2 <= '0.75': #get high confidence level
                print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output4)
            if rep1 <= '0.75' or rep2 <= '0.75': #get low confidence level
                print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output5)
        else: #get sample wells
            if not entname == 'empty':
                print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output2)
                if rep1 <= '0.85' and rep2 <='0.85': #get moderate confidence level
                    print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output6)
                if rep1 <= '0.75' and rep2 <= '0.75': #get high confidence level
                    print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output7)
                if rep1 <= '0.75' or rep2 <= '0.75': #get low confidence level
                    print(srun,plate,well, entname,entID,rep1,rep2,zscore,avOTP,ave, sep = ',', file = output8)
#-----------------------------

#Count the wells where replicate1 <=0.75 and replicate2 <= 0.75 (High confidence)

# get all of the counts for all controls (High)

import pandas as pd 
# Creating the dataframe  
df = pd.read_csv('sublist_screenModified_controls.csv')
genes = df.entrez_gene_name.unique() # this represents all the controls from th original file
for j in range(len(genes)):    
    datagene = df.loc[df.entrez_gene_name == genes[j]]  
    target1 = datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.75]
    target2 = target1.loc[target1.REP2_cell_count_normalised_to_OTP<=0.75]
    target2 = len(target2)
    percent2 = target2/len(datagene)*100 
    percent2 = round(percent2,2)
    print(genes[j],target2, percent2)
#------------------------------

#Count the wells where replicate1 <=0.75 or replicate2 <=0.75 (Low confidence)

# get all of the counts for all controls (Low)

import pandas as pd 
# Creating the dataframe  
df = pd.read_csv('sublist_screenModified_controls.csv')
genes = df.entrez_gene_name.unique() # this represents all the controls from th original file
for j in range(len(genes)):    
    datagene = df.loc[df.entrez_gene_name == genes[j]]  
    target1 = len(datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.75])
    target2 = len(datagene.loc[datagene.REP2_cell_count_normalised_to_OTP<=0.75])
    percent1 = target1/len(datagene)*100
    percent1 = round(percent1,2)
    percent2 = target2/len(datagene)*100 
    percent2 = round(percent2,2)
    print(genes[j],target1,percent1, target2, percent2)
#---------------------------------

#Count the wells where replicate1 <= 0.85 and replicate2 <=0.85 (Moderate confidence)

# get all of the counts for all controls (Moderate)

import pandas as pd 
# Creating the dataframe  
df = pd.read_csv('sublist_screenModified_controls.csv')
genes = df.entrez_gene_name.unique() # this represents all the controls from th original file
for j in range(len(genes)):    
    datagene = df.loc[df.entrez_gene_name == genes[j]]  
    target1 = datagene.loc[datagene.REP1_cell_count_normalised_to_OTP<=0.85]
    #because i want <=0.75 AND so use dataframe target 1 to search for target 2
    target2 = target1.loc[target1.REP2_cell_count_normalised_to_OTP<=0.85]
    target2 = len(target2)
    percent2 = target2/len(datagene)*100 
    percent2 = round(percent2,2)
    print(genes[j],target2, percent2)
#----------------------------------
