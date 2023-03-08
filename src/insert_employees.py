from typing import List
import pandas as pd
from src.container import Container  
from src.employee import Employee



def insert_employees(df: pd.DataFrame,tree: List[Container]):
    #print(df[['Emp Name','Emp Id','Department','Section','Designation','is job add task','is job supervisory']][(df['Section Code']==122703) | (df['Title A']=='الفاضل' )])
    
    flag =False
    for i in range(len(tree)):
        emps:pd.DataFrame = df[['Emp Name','Emp Id','Department','Section','Designation','is job add task','is job supervisory','has add task']][(df['Section Code']==tree[i].containerCode) | (df['Department Code']==tree[i].containerCode )]
        for ind, emp in emps.iterrows():
      
            
            flag = False
            if emp['has add task'] == True and not emp['is job add task'] :
                checkEmpData:pd.DataFrame = df[['Department Code','Section Code','is job add task',]][(df['Emp Id']==emp['Emp Id'])]
               
                for ind, data in checkEmpData.iterrows():

                    if (data['is job add task']) and ( data['Department Code'] != tree[i].containerCode or  data['Section Code'] != tree[i].containerCode):
                        flag = True
                       
                       
                    
                    
            if flag: continue
            # print(emp['Emp Id'])
            e = Employee(emp['Emp Id'],emp['Emp Name'],emp['Designation'],tree[i].containerCode,emp['is job supervisory'],emp['is job add task'])
            tree[i].addEmployee(e)
        


    
    