from src.container import Container  

def display_containers(tree: list[Container]):
    for i in range(len(tree)):
        if tree[i].manager is not None:
            x = 0
            print('---------------------------------------------------------------------------------------------')
            print('the manager of container: ', tree[i].containerName,'  is ',tree[i].manager.name )
            for e in tree[i].employees:
                x=1+x
                print(x,'- ',e.name,)
                
            print('---------------------------------------------------------------------------------------------')
    
    print('Press Enter to return to the menu')
    input()
