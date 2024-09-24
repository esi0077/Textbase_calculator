import operator
# operator system 
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}  

# bruker oprator for funksjonen 
def leggSammen():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    summen = ops["+"](tall1, tall2)  
    print(f'{tall1} + {tall2} = {summen}')

def trekkFra():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    diff = ops["-"](tall1, tall2)  
    print(f'{tall1} - {tall2} = {diff}')

def gange():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    produkt = ops["*"](tall1, tall2)  
    print(f'{tall1} * {tall2} = {produkt}')

def dele():
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    if tall2 == 0:
        print("Kan ikke dele med null!")
    else:
        kvotient = ops["/"](tall1, tall2)  
        print(f'{tall1} / {tall2} = {kvotient}')


