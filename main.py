import pandas as pd
from src.create_tree import create_tree
from src.show_graph import show_graph
from src.insert_employees import insert_employees
from src.search_employee import search_emplpoyee
from src.display_containers import display_containers

df :pd.DataFrame= None

enter_file_name_flag = True
stop_flag = False
while enter_file_name_flag:
    try:
        print('please enter the name of the excel file\nmake sure the file exists in the same main.py folder (◕ᗜ◕)')
        file_name= input()
        df = pd.read_excel(file_name+'.xlsx')
        enter_file_name_flag = False
    except:
        print("I can't find the file ಥ ͜ʖ ͡ಥ\nAre you sure it is in the same folder where main.py exists?\nDo you want to exit (e) or write the name again (w)?")
        flag_except = True
        while flag_except:
            
            res = input()
            if res == 'e':
                enter_file_name_flag = False
                stop_flag = True
                flag_except = False
            elif res == 'w':
                flag_except = False
                
            else:
                print("Excuse my limited understanding (¬_¬”), But I'm expecting the following answers:\ne:exit\nw:write the name again ")
                


if not stop_flag :
    tree = create_tree(df)
    insert_employees(df,tree)
    for i in range(len(tree)):
        tree[i].whoIsManager()


counter = 0
while not stop_flag:
    
    try:
        print('\n\n\nPlease enter a number from the menu below:\n\n')
        print('(1).   Find a line manager for an employee\n')
        print('(2).   Display all of the containers\n')
        print('(3).   Show a graph of the containers\n')
        print('(4).   Exit\n\n')
        
        menu_res= input()

        if menu_res =='1':
            search_emplpoyee(tree)
            counter = 0
        elif menu_res =='2':
            display_containers(tree)
            counter = 0
        elif menu_res == '3':
            show_graph(tree)
            counter = 0
        elif menu_res == '4':
            stop_flag = True
            counter = 0
            print('See you later')
        else:
            print('Sorry but your response should be a number between 1 and 4 (●__● )')
            input()
            if counter >10:
                print('Ok, now you can go to Sisyphus. you two have a lot in common ( ͡◉ ͜ʖ ͡◉)')
                stop_flag = True
            counter = counter+1
            
            
    
    except:
        print('Somthing went wrong (o_O) ?')
        stop_flag = True













# show_graph(tree)

        
# for item in tree:
#     if item.parentContainer is not None:
#         # print('Container: ',item.containerCode,'Its paranet: ',item.parentContainer.containerCode)
        
#         # print('And its childs are:  ')
#         # for child in item.childContainers:
#         #     print(child.containerCode)
            
#         # print('---------------------')
        


# for i in range(len(tree)):
#     print('Container: ',tree[i].containerCode,'Its paranet: ',tree[i].parentContainer.containerCode)
    
#     print('And its childs are:  ')
#     for y in range(len(tree[i].childContainers)):
#         print(tree[i].childContainers[y])
