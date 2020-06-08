#MARIAM MIARI
#
#2020-2021
#
#SCRIPT TO PARSE HTMLS.
#
#BeautifulSoup SHOULD BE IMPORTED
#
#---------------------------------

#Dealing with BCL2 database
#Import BeautifulSoup for this set of scripts.


import bs4
from bs4 import BeautifulSoup
with open('BCL2DBCellular') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
    #the class attribute is always represented with '_' because "class" is a reserved word in python
    table = soup.find_all('table', class_="tnomenclature")
    
list_head = []
list_rows= []

#Create a csv
with open ('BCL2_table'+ ".csv", 'w') as out:
    for row in table[0].find_all('tr'):
        for head in row.find_all('th'):
            #append the headers to a list and join with commas (easier to parse)
            list_head.append(head.text)
            header = ",".join(list_head)
            #append the cells in each row to a list
        for cell in row.find_all('td'):
            #since the synonyms are seperated by commas, replace the commas with "|" because if I specify the delimiter later on as a comma it will be problematic.
            list_rows.append(cell.text.replace(',', '|'))
    print(header, file = out)
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples = list(zip(*[iter(list_rows)]*6))
    
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        print(','.join(tup), file = out)


#Printing table BAX
list_head = []
list_rows= []

#Create a csv
with open ('BAX_table'+ ".csv", 'w') as out:
    for row in table[1].find_all('tr'):
        for head in row.find_all('th'):
            #append the headers to a list and join with commas (easier to parse)
            list_head.append(head.text)
            header = ",".join(list_head)
            #append the cells in each row to a list
        for cell in row.find_all('td'):
            #since the synonyms are seperated by commas, replace the commas with "|" because if I specify the delimiter later on as a comma it will be problematic.
            list_rows.append(cell.text.replace(',', '|'))
    print(header, file = out)
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples = list(zip(*[iter(list_rows)]*6))
    
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        print(','.join(tup), file = out)
        
        
#Printing table BID-like
list_head = []
list_rows= []

#Create a csv
with open ('BID_table'+ ".csv", 'w') as out:
    for row in table[2].find_all('tr'):
        for head in row.find_all('th'):
            #append the headers to a list and join with commas (easier to parse)
            list_head.append(head.text)
            header = ",".join(list_head)
            #append the cells in each row to a list
        for cell in row.find_all('td'):
            #since the synonyms are seperated by commas, replace the commas with "|" because if I specify the delimiter later on as a comma it will be problematic.
            list_rows.append(cell.text.replace(',', '|'))
    print(header, file = out)
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples = list(zip(*[iter(list_rows)]*6))
    
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        print(','.join(tup), file = out)


#Printing other cellular homologs table

list_head = []
list_rows= []

#Create a csv
with open ('otherCellularHomologs_table'+ ".csv", 'w') as out:
    for row in table[3].find_all('tr'):
        for head in row.find_all('th'):
            #append the headers to a list and join with commas (easier to parse)
            list_head.append(head.text)
            header = ",".join(list_head)
            #append the cells in each row to a list
        for cell in row.find_all('td'):
            #since the synonyms are seperated by commas, replace the commas with "|" because if I specify the delimiter later on as a comma it will be problematic.
            list_rows.append(cell.text.replace(',', '|'))
    print(header, file = out)
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples = list(zip(*[iter(list_rows)]*6))
    
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        print(','.join(tup), file = out)
        

# Printing BH3 motif containing proteins

list_head = []
list_rows= []
with open('BCL2DBBH3only') as html_file, open('TBU_BH3_classical.csv', 'w') as out:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table', class_="tnomenclature")
    #to check how many tables are there in the site
    #len(table) #1
    #table[0] 
    for row in table[0].find_all('tr'):
        for head in row.find_all('th'):
            list_head.append(head.text)
        for cell in row.find_all('td'):
            list_rows.append(cell.text.replace(',', '|'))
    #remove 'primary function'
    list_head.pop(3)
    #remove references
    list_head = list_head[:-1]
    header = ",".join(list_head)
    print(header, file = out)
    tuples = list(zip(*[iter(list_rows)]*6)) 
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        #this will remove last element of the tuple (i.e. references)
        tup = tup[:-1]
        #this will print the first 3 element of the tuple and the last element (i.e. accession number)
        print(','.join(tup[:3]+tup[-1:]), file = out)
        
        

list_rows = []
list_head = []
with open('BCL2DBOtherBH3') as html_file, open('TBU_BH3_other.csv', 'w') as out:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table', class_="tnomenclature")
    #len(table) #1
    #table[0]
    for row in table[0].find_all('tr'):
        for head in row.find_all('th'):
            list_head.append(head.text)
        for cell in row.find_all('td'):
            list_rows.append(cell.text.replace(',', '|'))
    #remove 'primary function'
    list_head.pop(3)
    #remove references
    list_head = list_head[:-1]
    header = ",".join(list_head)
    print(header, file = out)
    tuples = list(zip(*[iter(list_rows)]*6)) 
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup[:3]+tup[-1:]), file = out)
# ---------------------------------

#Dealing with CASBAH database

with open('The_CASBAH.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table')
len(table) #18 SO CHECK THE INDEX OF EACH TABLE OF INTEREST

list_head = []
list_rows= []

#Create a csv
with open ('CASBAH_table'+ ".csv", 'w') as out:
    for row in table[1].find_all('tr'):
        for head in row.find_all('th'):
            #This step was done because some lines before the headers started with "#" and they were hard to get rid of.
            if head.text.startswith('Name') or head.text.startswith('Uni Prot') or head.text.startswith('Synonyms') or head.text.startswith('Consequences') or head.text.startswith('PubMed') or head.text.startswith('Site(s)'):#print(head.text) 
            #append the headers to a list and join with commas (easier to parse)
                list_head.append(head.text)#print(list_head)
    header = ",".join(list_head)
    #append the cells in the table to a list
    for cell in table[1].find_all('td'):
        #I don't want the first cell which is a number
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    #print(list_rows)
    print(header, file = out)
    
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples = list(zip(*[iter(list_rows)]*7))
    #print(tuples)
    #iterate over the tuple list in order to join the cells with commas (easier to parse)
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
#Start with table2

list_rows= []
list_head = []

#Create a csv
with open ('CASBAH_table2'+ ".csv", 'w') as out:
    for row in table[2].find_all('tr'):
        for cell in table[2].find_all('td'):
            if not cell.text.isdigit():
                list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown'))
    
    #This code will create a list of tuples whereby each tuple has 6 cells (i.e. 1 row)
    tuples1 = list(zip(*[iter(list_rows)]*7))
    # I took the first 13 tuples because there's problem in this table.
    first13_tuples = tuples1[:13]
    for tup in first13_tuples:
        #remove the last "unknown" which I used to replace '\xa0'
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
    #get the middle elements in the list and create another tuple: I counted the index of each element in list_rows and wrote the index accordingly.
    tuples2 = list(zip(*[iter(list_rows[91:283])]*12))
    for tup in tuples2:
        #remove the last 6 unknowns (this part of the table had more unknowns than the other tables)
        tup = tup[:-6]
        print(','.join(tup), file = out)
        
    #create another tuple that contain that last 147 element of the list_rows.
    tuples3 = list(zip(*[iter(list_rows[-147:])]*7)) 
    for tup in tuples3:
        tup = tup[:-1]
        print(','. join(tup), file = out)
        
 
 #Start with table3
 list_rows= []

#Create a csv
with open ('CASBAH_table3'+ ".csv", 'w') as out:
    for cell in table[3].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    #print(list_rows)
    
    tuples = list(zip(*[iter(list_rows)]*7))
    #print(tuples)
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
  #Continue with other tables
  list_rows= []

with open ('CASBAH_table4'+ ".csv", 'w') as out:
    for cell in table[4].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)

        
with open ('CASBAH_table5'+ ".csv", 'w') as out:
    for cell in table[5].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)

        
with open ('CASBAH_table6'+ ".csv", 'w') as out:
    for cell in table[6].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table7'+ ".csv", 'w') as out:
    for cell in table[7].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table8'+ ".csv", 'w') as out:
    for cell in table[8].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    #print(tuples)
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table9'+ ".csv", 'w') as out:
    for cell in table[9].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table10'+ ".csv", 'w') as out:
    for cell in table[10].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table11'+ ".csv", 'w') as out:
    for cell in table[11].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table12'+ ".csv", 'w') as out:
    for cell in table[12].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table13'+ ".csv", 'w') as out:
    for cell in table[13].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table14'+ ".csv", 'w') as out:
    for cell in table[14].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    tuples = list(zip(*[iter(list_rows)]*7))
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table15'+ ".csv", 'w') as out:
    for cell in table[15].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    #print(list_rows)
    tuples = list(zip(*[iter(list_rows)]*7))
    #print(tuples)
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)
        
        
with open ('CASBAH_table16'+ ".csv", 'w') as out:
    for cell in table[16].find_all('td'):
        #print(cell.text)
        if not cell.text.isdigit():#print(cell.text)
            list_rows.append(cell.text.replace(',', '|').replace('\xa0','unknown').replace('&nbsp;', 'x')) 
            #to remove empty strings from a list
            list_rows = list(filter(None,list_rows))
    #print(list_rows)
    tuples = list(zip(*[iter(list_rows)]*7))
    #print(tuples)
    for tup in tuples:
        tup = tup[:-1]
        print(','.join(tup), file = out)    #cat all 
        
#Parsing CASBAH:

#Print each organism's name at the end of its line. 
with open('CASBAH_Fulltable.csv', 'r') as full, open('TBU_CASBAH', 'w') as out:
    print('Name_CASBAH', 'Uniprot_CASBAH', 'Synonyms_CASBAH', 'Organism_CASBAH', sep = ';', file = out)
    for line in full:
        if not 'Uni Prot' in line:
            if 'HUMAN' in line or 'human' in line:
                line = line.rstrip()
                line = line.split(',')
                name = line[0]
                uniprot = line[1].split(')')[0]
                synonym = line[2].replace(';', ',')
                print(name,uniprot,synonym, 'HUMAN', sep = ';', file = out )
            elif 'MOUSE' in line:
                line = line.rstrip()
                line=line.split(',')
                name_m = line[0]
                uniprot_m = line[1].split(')')[0]
                synonym_m = line[2].replace(';', ',')
                print(name_m,uniprot_m,synonym_m,'MOUSE', sep = ';',file = out)
            elif 'RAT' in line:
                line = line.rstrip()
                line=line.split(',')
                name_r = line[0]
                uniprot_r = line[1].split(')')[0]
                synonym_r = line[2].replace(';', ',')
                print(name_r,uniprot_r,synonym_r,'RAT', sep = ';', file = out)
            else:
                line = line.rstrip()
                line=line.split(',')
                name_o = line[0]
                uniprot_o = line[1].split(')')[0]
                synonym_o = line[2].replace(';', ',')
                print(name_o,uniprot_o,synonym_o,'OTHER', sep = ';',file = out)
#-----------------------------

#Dealing with Human Autophagy Database (HADB)

mylist = [] # that is going to be a list of lists
myelement = []

#No need to write this with open statment each time I run the code here. just the first time. But write it in Atom
with open('HumanAutophagydatabase.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    #check the index of all tables
    table = soup.find_all('table')
#len(table)
#index table[6]

#the file is named to be cleaned because I will remove the escape characters from it.
with open('tobecleaned', 'w') as tobecleaned:
    for row in table[6].find_all('tr'):
        print(row.text, file = tobecleaned)  

#row.text contains a lot of spaces and tabs. The file is a mess.
with open('tobecleaned','r') as tobecleaned, open('cleanTable6', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        #I split at the new lines and that gave empty lists instead of the new lines.
        line_list = line.split('\n')
        mylist.append(line_list)
        #I need to remove the empty lists from the list.
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            #append all the contents of the sub-lists to another list (this will make it easier to parse)
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples:
        #The delimiter now is a ';'. That's better than',' because some words within same field are separated by ','.
        print(';'.join(tup), file = output) 
        
 #REMOVE HEADERS
with open('HumanAutophagydatabase.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table')

with open('tobecleaned8', 'w') as tobecleaned:
    for row in table[8].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned8','r') as tobecleaned, open('cleanTable8', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    #I don't want to include the header in the rest of the tuples because it's already present from the first table. (i will concate all)
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
  
#REMOVE HEADERS
with open('HumanAutophagydatabase.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table')


with open('tobecleaned8', 'w') as tobecleaned:
    for row in table[8].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned8','r') as tobecleaned, open('cleanTable8', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    #I don't want to include the header in the rest of the tuples because it's already present from the first table. (i will concate all)
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)

#FROM TABLE 10 TILL TABLE 56, CHANGE THE INDEX.
with open('tobecleaned10', 'w') as tobecleaned:
    for row in table[10].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned10','r') as tobecleaned, open('cleanTable10', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        

with open('tobecleaned12', 'w') as tobecleaned:
    for row in table[12].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned12','r') as tobecleaned, open('cleanTable12', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned14', 'w') as tobecleaned:
    for row in table[14].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned14','r') as tobecleaned, open('cleanTable14', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        

with open('tobecleaned16', 'w') as tobecleaned:
    for row in table[16].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned16','r') as tobecleaned, open('cleanTable16', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        

with open('tobecleaned18', 'w') as tobecleaned:
    for row in table[18].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned18','r') as tobecleaned, open('cleanTable18', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned20', 'w') as tobecleaned:
    for row in table[20].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned20','r') as tobecleaned, open('cleanTable20', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned22', 'w') as tobecleaned:
    for row in table[22].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned22','r') as tobecleaned, open('cleanTable22', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        

        
with open('tobecleaned24', 'w') as tobecleaned:
    for row in table[24].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned24','r') as tobecleaned, open('cleanTable24', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
   
with open('tobecleaned26', 'w') as tobecleaned:
    for row in table[26].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned26','r') as tobecleaned, open('cleanTable26', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
with open('tobecleaned28', 'w') as tobecleaned:
    for row in table[28].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned28','r') as tobecleaned, open('cleanTable28', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
with open('tobecleaned30', 'w') as tobecleaned:
    for row in table[30].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned30','r') as tobecleaned, open('cleanTable30', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
with open('tobecleaned32', 'w') as tobecleaned:
    for row in table[32].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned32','r') as tobecleaned, open('cleanTable32', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
#TABLE34 IS EMPTY       
with open('tobecleaned36', 'w') as tobecleaned:
    for row in table[36].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned36','r') as tobecleaned, open('cleanTable36', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
#TABLE 38 is empty      
with open('tobecleaned40', 'w') as tobecleaned:
    for row in table[40].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned40','r') as tobecleaned, open('cleanTable40', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned42', 'w') as tobecleaned:
    for row in table[42].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned42','r') as tobecleaned, open('cleanTable42', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        

with open('tobecleaned44', 'w') as tobecleaned:
    for row in table[44].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned44','r') as tobecleaned, open('cleanTable44', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned46', 'w') as tobecleaned:
    for row in table[46].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned46','r') as tobecleaned, open('cleanTable46', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned48', 'w') as tobecleaned:
    for row in table[48].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned48','r') as tobecleaned, open('cleanTable48', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
with open('tobecleaned50', 'w') as tobecleaned:
    for row in table[50].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned50','r') as tobecleaned, open('cleanTable50', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)
        
        
        
#Tables 52,54 were empty
with open('tobecleaned56', 'w') as tobecleaned:
    for row in table[56].find_all('tr'):
        print(row.text, file = tobecleaned)

mylist = []
myelement = []
with open('tobecleaned56','r') as tobecleaned, open('cleanTable56', 'w') as output:
    for line in tobecleaned:
        line=line.strip()
        line_list = line.split('\n')
        mylist.append(line_list)
        mylist = [x for x in mylist if x != ['']]
    for lists in mylist:
        for element in lists:
            myelement.append(element)
            ','. join(myelement)
            tuples = list(zip(*[iter(myelement)]*3))
    for tup in tuples[1:]:
        print(';'.join(tup), file = output)

#cat all files and save to TBU_HumanAutophagy_DB

#Parsing Human Autophagy database
entrez_uniprot = {} # will hold the entrezID from the mapped entries.
myDict = {} #this will be the big dictionary that will hold entGeneIDs, name , uniprotID, symbol from the original file.
with open('TBU_HumanAutophagy_DB', 'r') as tbu, open('mapped_uniprot_HADB','r') as mapped, open('TBU_New_HADB', 'w') as out:
    print('GeneId_HADB', 'Uniprot_HADB','Name_HADB','Symbol_HADB', sep = ';', file = out)
    for line in mapped:
        if not 'yourlist' in line:
            line=line.rstrip()
            line=line.split('\t')
            entrezID= line[0]
            uniprot = line[1]
            entrez_uniprot[uniprot] = entrezID
    for line in tbu:
        if not 'GeneId' in line:
            line=line.rstrip()
            line=line.split(';')
            entGeneID = line[0]
            myDict[entGeneID] = {}
            name = line[1]
            myDict[entGeneID]['name'] = name
            symbol=line[2]
            myDict[entGeneID]['symbol'] = symbol
    for uniprot,entrezID in entrez_uniprot.items():
        if entrezID in myDict:
            print(entrezID, uniprot,myDict[entrezID]['name'], myDict[entrezID]['symbol'], sep = ';', file = out)
#-------------------------------

#Dealing with Human Lysosome Gene database

with open('TheHumanLysosomeGene.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    table = soup.find_all('table')
#len(table)

list_head = []
list_rows= []

with open ('HumanLysosomeGene_table', 'w') as out:
    for row in table[1].find_all('tr'):
        for head in row.find_all('th'):
            #append the headers to a list and join with commas (easier to parse)
            list_head.append(head.text)
            list_head = list(filter(None,list_head))
            header = ";".join(list_head)
            #append the cells in each row to a list
        for cell in row.find_all('td'):
            list_rows.append(cell.text)
            list_rows = list(filter(None,list_rows))
    print(header, file = out)
    tuples = list(zip(*[iter(list_rows)]*3))
    
    for tup in tuples: #keep in mind that the delimiter is a ';'
        print(';'.join(tup), file = out)
        
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
cat header TBU_HumanLysosomeGene_DB> TBU_TheHumanLysosomeGene            
#-----------------------------
  
