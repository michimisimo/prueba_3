
import funciones as func

x=1

autos=[]
lista_multa=[]

while True:

    func.menu_1()
    opc=input()

    if opc=="1":
        
        func.grabar_auto(lista_multa,autos)

    elif opc=="2":

        func.buscar_auto(autos)
    
    elif opc=="3":

        func.certificados(autos,lista_multa)
        
    elif opc=="4":
        print("\ngracias por utilizar el programa\n\n Felipe Urbina       Version:3.5\n")
        break

            


        
