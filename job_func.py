import pandas as pd
import csv
import glob
import os
from itertools import chain

dir_name = input("Enter the folder name : ")
while dir_name.lower() not in list(map(lambda x:x.lower(),os.listdir())):
    dir_name = input("Please Re-enter Folder Name : ")
with open(dir_name + ' Job_Function_Stats.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Report Name','Job Function','User Count','Query Count(Year)','Query Count(Q1)','Query Count(Q2)','Query Count(Q3)','Query Count(Q4)',"Jan_Query","Feb_Query","Mar_Query","Apr_Query","May_Query","Jun_Query","July_Query","Aug_Query","Sep_Query","Oct_Query","Nov_Query","Dec_Query"])
files = glob.glob(dir_name+'/*.csv')
for file in files:
    df=pd.read_csv(file)
    date=df['Date']
    for i in range(len(date)):
        date[i]=date[i][:10]
    query_count = list(df['Query Count'])
    job_func=list(set(df['JOB Function']))
    Analysis = df['Report/Analysis']
    Analysis = Analysis[0].split('/')
    Analysis_Name = Analysis[-1]
    query_count_dict = {}
    user_count_dict = {}
    user_name = df['Full Name']
    for i in job_func:
        query_count_dict[i] = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        user_count_dict[i] = []
    for i in range(len(date)):
        for j in range(1,13):
            if(int(date[i][5:7])) == j:
                query_count_dict[df['JOB Function'][i]][j]+=df['Query Count'][i]
                user_count_dict[df['JOB Function'][i]].append(user_name[i])
    # print(user_count_dict['Engineering'])
    for i in job_func:
        new_row=[]
        new_row.append(Analysis_Name)
        new_row.append(i)
        new_row.append(len(set(list(user_count_dict[i]))))
        new_row.append(sum(list(query_count_dict[i].values())))
        new_row.append(sum(list(query_count_dict[i].values())[0:3]))
        new_row.append(sum(list(query_count_dict[i].values())[3:6]))        
        new_row.append(sum(list(query_count_dict[i].values())[6:9]))        
        new_row.append(sum(list(query_count_dict[i].values())[9:])) 
        new_row+=list(query_count_dict[i].values())
        print(new_row)
        with open(dir_name + ' Job_Function_Stats.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(new_row)

    # for i in range(len(date)):
    #     query_count_dict[df['JOB Function'][i]]+=df['Query Count'][i]

    
    
