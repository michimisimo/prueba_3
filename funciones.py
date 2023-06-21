import random

def menu_1():
    print("\n¿Que sea hacer?\n1. Grabar\n2. Buscar\n3. Imprimir certificados\n4. Salir")


def grabar_auto(lista_multa,autos):
       
        dueño=input("ingrese nombre del dueño: ")
        patente=input("ingrese patente: ")
        tipo=input("ingrese tipo de vehiculo: ")
        
        while True:
            marca=input("ingrese marca: ")
            if len(marca)<2:
                print("la marca debe tener entre 12 y 15 caracteres")
            elif len(marca)>15:
                print("la marca debe tener entre 12 y 15 caracteres")
            else:
                break
        
        precio=0
        while precio<5000000:
            precio=int(input("ingrese precio: "))
            if precio<5000000:
                 print("el precio debe ser mayor a 5.000.000")

        fecha_registro=input("ingrese fecha de registro: ")
        multas=int(input("ingrese cantidad multas: "))

        for m in range(multas):
            print("multa N°",(m+1))
            fecha=input("ingrese fecha de multa: ")
            monto=input("ingrese monto de multa: ")
            
            multa={
                
                "fecha":fecha,
                "monto":monto

            }
            
            lista_multa.append(multa)

        auto={
            
            "dueño":dueño,
            "patente":patente,
            "tipo":tipo,
            "marca":marca,
            "precio":precio,
            "fecha_registro":fecha_registro,
            "multa":lista_multa,

        }
        autos.append(auto)

        print("\n el vehiculo fue ingresado correctamente")


def buscar_auto(autos):
    
    buscar=input("ingrese la patente que dea buscar: ")
     
    auto_encontrado=None

    for  auto in autos:
        if auto["patente"] == buscar:
            auto_encontrado = auto
            break
             
    if auto_encontrado:
        print("\nDatos del auto:")
        print(f"dueño: {auto['dueño']}")
        print(f"patente: {auto['patente']}")
        print(f"tipo: {auto['tipo']}")
        print(f"marca: {auto['marca']}")
        print(f"precio: {auto['precio']}")
        print(f"fecha registro: {auto['fecha_registro']}")
        print(f"multas: {auto['multa']}")
    
    else:
            print("\nla patente no esta vinculada a ningun vehiculo")


def certificados(autos, lista_multa):
    
    buscar=input("ingrese la patente que dea buscar: ")
     
    auto_encontrado=None

    for  auto in autos:
        if auto["patente"] == buscar:
            auto_encontrado = auto
            break
             
    if auto_encontrado:
    
        print("\n¿Que certificado desea?\n1. Emision de contaminantes\n2.Anotaciones vigentes\n3. Multas")
        certificado=int(input())

        if certificado==1:
            print("Certificado de Emision de contaminantes")
            print(f"dueño: {auto['dueño']}")
            print(f"patente: {auto['patente']}")
            print(("precio: $2.300"))
        
        if certificado==2:
            print("Certificado de Anotaciones vigentes")
            print(f"dueño: {auto['dueño']}")
            print(f"patente: {auto['patente']}")
            print(("precio: $3.000"))
        
        if certificado==3:
            print("Certificado de Multas")
            print(f"dueño: {auto['dueño']}")
            print(f"patente: {auto['patente']}")
            print((f"multas: {auto['multa']}"))
    else:
         print("\nla patente no esta vinculada a ningun vehiculo")