print('Ez egy állatkert!')
print('Állat hozzáaadása -- (1) Állat törlése -- (2) kilépés -- (0)')


zoo = []
select = None


while select != '0':
    select = input('Mit szeretne tenni? ')
    
    if select == '1':
        animal = {}
        name = input('Az állat neve: ')
        found = False
        
        for i in zoo:
            if name in i:
                found = True
                i[name] += 1
        
        if not found:
            animal[name] = 1
            zoo.append(animal)

    elif select == '2':
        remove = input('A eltávolítandó állat neve: ')
        
        for i in zoo:
            if remove in i and i[remove] > 1:
                i[remove] -= 1
            
            else:
                del animal[remove]
            
            
print(zoo)
