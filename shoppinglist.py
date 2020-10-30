Shopping=True
list=['youtube']
while Shopping=True:
    toadd=input('What do you want to add to the shopping list?')
    list.append(toadd)
    print('you have', list, 'in your shopping list')
    shoppingstill=input('Do you still want to add to the list?')
    if shoppingstill.lower='yes':
        print('ok')
        Shopping=False
    
