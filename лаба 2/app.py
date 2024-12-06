
def greet(name:str):
    if isinstance(name,str)!=True:
        return ('Ошибка')
    else:
        return (f'Приветствую {name}!')
print(greet('ars'))



def square(number:int):
    if number.isdigit()==False:
        return('Ошибка')
    return(int(number)**2)
print(square('33'))




def max_of_two(x:int, y:int):
    if x.isdigit()==False or y.isdigit()==False:
       return('Ошибка')
    return(max(int(x),int(y)))
print(max_of_two('33','65'))


def describe_person(name:str, age:int=30):
    return(f'Моё имя {name}, мой возраст {age}')
print(describe_person('Arseniy',31))



def is_prime(number:int):
    if int(number)/float(number)!=1.0:
        return False
    divider=2
    while number % divider != 0:
        divider+=1
    return divider==number
print(is_prime(5))
