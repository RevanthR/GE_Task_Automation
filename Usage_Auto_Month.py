import pandas as pd
import csv
import glob
import os

month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
month_list_resp=month_list #copy of the list to evaluate input

month_list = list(enumerate(month_list,1))

dir_name = input("Enter the folder name : ")
month_name = input("Enter the month to get the statistics : ") 
while dir_name.lower() not in list(map(lambda x:x.lower(),os.listdir())):
    dir_name = input("Please Re-enter Folder Name : ")
temp=[]

while len(temp) == 0:
    for i in month_list_resp:
        if month_name.lower() in i.lower():
            temp.append(i)
    if len(temp)==1:
        print(temp)
        break
    else:
        month_name = input("Please Re-Enter the month to get the statistics : ") 


month_num = 0
for i in range(len(month_list)):
    if month_name.lower() in month_list[i][1].lower():
        month_num = month_list[i][0] 

#Rename all the files in the folder with resect to the folder name
i = 1
dir_name_list = dir_name.split()
new_name='_'.join(dir_name_list)
for filename in os.listdir(dir_name):
    dst = dir_name + "/" + new_name +"_Analysis_July_"+str(i)+".csv"
    src = dir_name+'/'+filename
    os.rename(src,dst)
    i+=1 

# Create a new csv file to store the summary
month_name=temp[0]
with open(new_name + '_Report_Summary.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Dashboard Name","Analysis Name","User Count","Query Count","User Count("+ month_name +")","Query Count("+ month_name+" 2019)","Job Function"])

# Read Multiple CSV Files in a given folder

files = glob.glob(dir_name+'/*.csv')
for file in files:
    df=pd.read_csv(file)
    date=df['Date']
    for i in range(len(date)):
        date[i]=date[i][0:10]
    query_count= df['Query Count']
    query_count=list(query_count)
    query_count_val=sum(query_count)
    
    query_count_mon=[]
    names_user = list(df['Full Name'])
    names_user_count=len(set(names_user))
    names_user_mon=[]

    new_date_mon=[]
    for i in range(len(names_user)):
        if(int(date[i][5:7])) == int(month_num):
            names_user_mon.append(names_user[i])
            query_count_mon.append(query_count[i])

    names_user_mon=set(names_user_mon)
    user_count_mon=len(names_user_mon)
    query_count_mon_val=sum(query_count_mon)

    # Get the Dashboard Name and the Report Name

    report_name=df['Report/Analysis']
    report_name=list(report_name)
    report_name[0]=report_name[0].split('/')
    analysis_name=report_name[0][-1]

    dashboard=df['Dashboard']
    dashboard=list(dashboard)
    dashboard[0]=str(dashboard[0]).split('/')
    dashboard_name= dashboard[0][-1]
   
    # Get the Job Function
 
    job_func=df['JOB Function']
    job_func=set(list(job_func))
    job_func=list(job_func)
    job_func=', '.join(job_func)
    print(dashboard_name,analysis_name, names_user_count,query_count_val, user_count_mon, query_count_mon_val, job_func)

    # Write the list into a csv file

    new_row=[]
    new_row.append(dashboard_name)
    new_row.append(analysis_name)
    new_row.append(names_user_count)
    new_row.append(query_count_val)
    new_row.append(user_count_mon)
    new_row.append(query_count_mon_val)
    new_row.append(job_func)   

    with open(new_name+'_Report_Summary.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(new_row)
        
