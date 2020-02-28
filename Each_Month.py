import pandas as pd
import csv
import glob
import os
from itertools import chain

dir_name = input("Enter the folder name : ")
while dir_name.lower() not in list(map(lambda x:x.lower(),os.listdir())):
    dir_name = input("Please Re-enter Folder Name : ")

#Rename all the files in the folder with resect to the folder name
# i = 1
# dir_name_list = dir_name.split()
# new_name='_'.join(dir_name_list)
# for filename in os.listdir(dir_name):
#     dst = dir_name + "/" + new_name +"_Analysis_July_"+str(i)+".csv"
#     src = dir_name+'/'+filename
#     os.rename(src,dst)
#     i+=1 

# Create a new csv file to store the summary
with open( 'Report_Summary.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Dashboard Name","Analysis Name","User Count Year","Query Count Year","Jan_User","Feb_User","Mar_User","Apr_User","May_User","Jun_User","July_User","Aug_User","Sep_User","Oct_User","Nov_User","Dec_User","Jan_Query","Feb_Query","Mar_Query","Apr_Query","May_Query","Jun_Query","July_Query","Aug_Query","Sep_Query","Oct_Query","Nov_Query","Dec_Query","Job_function","User Names"])

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
    dict_month_query_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    dict_month_user={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    user_count_month=[]
    user_count_year=[]
    new_date_mon=[]
    for i in range(len(names_user)):
        for j in range(1,13):
            if(int(date[i][5:7])) == j:
                dict_month_query_count[j]+=query_count[i]
                dict_month_user[j].append(names_user[i])
    for i in range(1,13):
        dict_month_user[i]=list(set(dict_month_user[i]))
    for i in dict_month_user.values():
        user_count_month.append(len(i))
        user_count_year.append(i)

    # calculate user and query count
    user_count_year=list(chain(*user_count_year))
    user_year=list(set(user_count_year))
    user_count_year=len(set(user_count_year))
    month_query_count=list(dict_month_query_count.values())
    year_query_count=sum(month_query_count)
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

    #Get the user
    user_year='/ '.join(user_year)
    # print(dashboard_name,analysis_name, names_user_count,query_count_val, user_count_mon, query_count_mon_val, job_func)

    # Write the list into a csv file

    new_row=[]
    new_row.append(dashboard_name)
    new_row.append(analysis_name)
    new_row.append(user_count_year)
    new_row.append(year_query_count)
    new_row=new_row+user_count_month
    new_row=new_row+(month_query_count)
    new_row.append(job_func)   
    new_row.append(user_year)
    print(new_row)
    with open('Report_Summary.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(new_row)
        
 