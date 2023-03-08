from src.container import Container  

def search_emplpoyee (tree: list[Container]):
    
    print('Enter employee SQU ID to find out his\her manager: ')
    emplpoyee_id = input()

    flag = True
    for c in tree:
        for e in c.employees:
            if int(emplpoyee_id)== e.employeeID:
                flag = False
                if e.employeeID == c.manager.employeeID:
                    print('The manager is ',c.parentContainer.manager.name)
                else:
                    print('The manager is ',c.manager.name)

    if flag: print("sorry I couldn't find this ID :(")
    
    print('Press Enter to return to the menu')
    input()
