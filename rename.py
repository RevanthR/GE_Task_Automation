import os

i=1
dir_name=input("Enter: ")
dir_name_list=dir_name.split()
new_name='_'.join(dir_name_list)
for filename in os.listdir(dir_name):
    dst= dir_name + "/" + new_name +"_Report_"+str(i)+".csv"
    src= dir_name+'/'+filename
    os.rename(src,dst)
    i+=1