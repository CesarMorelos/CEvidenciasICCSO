import pandas as pd

x = [1.0, 1.6, 3.4, 4.0, 5.2]
y = [1.2, 2.0, 2.4, 3.5, 3.5]

def lin_reg(a,b):  #Se genera una funcion la cual se realizara cuando sea llama
    xf= pd.array(a) #pasamos la informacion de x a un array de pandas
    yf= pd.array(b)

    def suma(a):  #se genera una funcion 
        sum = 0    #se decl ara una variable
        for i in range(len(a)):  #se realiza un ciclo for, tomando cmo longitud el tamaño de a
            sum = a[i] + sum
        return sum
        
    xy = xf * yf
    x2 = xf*xf
    n = len(xf)

    a = ((n * suma(xy)) - (suma(xf) * suma(yf))) / ((n * suma(x2)) - (suma(xf) * suma(xf)))
    b = ((suma(yf) * suma(x2)) - (suma(xy) * suma(xf))) / ((n * suma(x2)) - (suma(xf) * suma(xf)))

    return a,b

print(lin_reg(x,y))
