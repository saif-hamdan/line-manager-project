from typing import List
import pandas as pd
from src.container import Container  


def create_tree (df:pd.DataFrame):
    

    tree:List[Container] = []


    for index, row in df.iterrows():

        hierarchyLevel='Section Code'
        containerNameLevel = 'Section'
        flag = True
        flag3 = True
        inx = 0

        
    
        if str(row['Section Code']) == 'nan':
            hierarchyLevel = 'Department Code'
            containerNameLevel = 'Department'
            
        for i,c in enumerate(tree):
            if  c.containerCode == row[hierarchyLevel]:
                flag =False
                inx = i
                break
            elif c.containerCode == row[hierarchyLevel]:
                flag =False
                inx = i
                break
            
            
        if flag ==False and tree[inx].parentContainer is None:
            tree[inx].addContainerName(row[containerNameLevel])
            for c in tree:
                if row['Parent Container'] =='head':
                    
                    break
                
                if row['Parent Container'] == c.containerCode:
                    tree[inx].linkParentContainer(True,c)
                    c.addChildContainers(tree[inx])
                    flag3 =False
                    break
            
            if flag3:
                newParent = tree[inx].linkParentContainer(False,row['Parent Container'])
        
                tree.append(newParent)
            
        if(flag):
            flag2 = True
            con = Container(row[hierarchyLevel],row[containerNameLevel])
            for c in tree:
                if row['Parent Container'] =='head':
                    break
                
                if row['Parent Container'] == c.containerCode:
                    con.linkParentContainer(True,c)
                    c.addChildContainers(con)
                    tree.append(con)
                    flag2 =False
                    break
            
            if flag2:
                newParent = con.linkParentContainer(False,row['Parent Container'])
                
        
                tree.append(newParent)
                
            
                
                tree.append(con)

    return tree
