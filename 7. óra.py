'''
def fejlec(cim):
    szelesseg = 30
    csillagok = "*"*szelesseg
    kozepso_csillag = "*"*int((szelesseg-len(cim))/2)

program_neve = "csillagok"
fejlec(program_neve)

teszt = ""
for i in range(2,20):
    teszt+="C"
    fejlec(teszt)
'''
'''
print(0xABBA) #16-os számrendszer

print(0xABBA) #16-os számrendszer
print(0o123) #8-as számrendszer

print(0b11000000) #2-es számrendszer

x=int("345",8) #átváltás 8-as számrednszerbe
print(x)

a = oct(321) #váltás 8-as számrednszerbe
print(a)

b = hex(40096) #váltás 16-os számrednszerbe
print(b)

c = bin(40096) #váltás 2-es számrendszerbe
print (c)

print(1/100000000)  # 1 szorozva 10 a -3.-on (1e-08)

str = 'Anya azt mondta, hogy: \"Érj haza időben!\"'
print(str)
'''
x = 6/4 # 1.5
y = 6//4 # 1 = int(1.5)
z = 6%4 # 2
zs = 2 ** 5 # 32

print(6 // 3)
print(6 // 4) # maradékos osztás
print (6 / 4) # maradék nélküli osztás