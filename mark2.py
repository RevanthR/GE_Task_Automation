import pandas as pd
import csv
import glob

with open('new1.csv','a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Dashboard Name","Analysis Name","User Count","Query Count","User Count(Jan)","Query Count(Jan)","Job Function"])

files= glob.glob('Data/*.csv')

# Read Multiple CSV Files in a given folder

for file in files:
    df=pd.read_csv(file)
    date=df['Date']
    for i in range(len(date)):
        date[i]=date[i][0:10]
    query_count= df['Query Count']
    i=0
    new_date_jan=[]
    while(int(date[i][5:7])) == 1:
        new_date_jan.append(date[i])
        i=i+1

    query_count=list(query_count)
    query_count_val=sum(query_count)

    # Count the number of users in Total

    names_user= df['Full Name']
    names_user=list(names_user)
    names_user_count=len(set(names_user))

    # Count the number of user in the month of Jan

    names_user_jan=names_user[:len(new_date_jan)]
    names_user_jan=list(names_user_jan)
    names_user_jan=set(names_user_jan)

    user_count_jan=len(names_user_jan)
    query_count_jan=sum(query_count[:len(new_date_jan)])

    # Get the dashboard Name and the Report Name

    report_name=df['Report/Analysis']
    report_name=list(report_name)
    report_name[0]=report_name[0].split('/')

    dashboard_name=report_name[0][-2]
    analysis_name=report_name[0][-1]

    # Get the Job Function

    job_func=df['JOB Function']
    job_func=set(list(job_func))
    job_func=list(job_func)
    job_func=', '.join(job_func)

    print(dashboard_name,analysis_name, names_user_count,query_count_val, user_count_jan, query_count_jan, job_func)

    # Write the list into a csv file

    new_row=[]
    new_row.append(dashboard_name)
    new_row.append(analysis_name)
    new_row.append(names_user_count)
    new_row.append(query_count_val)
    new_row.append(user_count_jan)
    new_row.append(query_count_jan)
    new_row.append(job_func)   
    with open('new1.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(new_row)