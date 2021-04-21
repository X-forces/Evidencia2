import datetime
import csv

def generar(articulos):
    contador=0
    datos = list()

    with open("datos.csv", "r") as archivo:
        lector = csv.reader(archivo, delimiter = ",")
        registros = 0
        
        for clave, descripcion, cantidad,precio,total,fechan in lector:
            if registros == 0:
                columnas = (clave,descripcion, cantidad,precio,total,fechan)
                registros = registros + 1
            else:
                contador=0
                clave = int(clave)
                print(clave,descripcion, cantidad,precio,total,fechan)
                if clave in articulos:
                    articulos[clave].append((clave, descripcion, cantidad,precio,total,fechan))
                else:
                    articulos[clave]=[(clave,descripcion, cantidad,precio,total,fechan)]
                    datos.append((clave, descripcion, cantidad,precio,total,fechan))
        print(articulos)
    return articulos

articulos={}
generar(articulos)
print(articulos)
input("-----")

while True:
    print("\n\tMain menu")
    print("1-Registrar una venta")
    print("2-Consultar una venta")
    print("X-Salir ")
    opcion = input("Elige una opcion")
    if opcion =='1':
        monto_total=0
        print("Registrar")
        contador= max(articulos,default=0)+1
        articulos[contador]=[]
        while opcion !='0':
            while True:
                try:
                    descripcion = input(f"Escribe la descripcion de la venta {contador}: ")
                    cantidad = int(input("Escribe la cantidad a comprar del articulo: "))
                    precio= float(input(f"Escribe el precio del articulo: "))
                    fecha=input("Dime una fecha (dd/mm/aaaa): \n")
                    fecha_procesada = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
                    break
                except Exception as e:
                    print(e)    
            compra = (contador,descripcion.upper(),cantidad,precio,cantidad*precio,fecha)
            monto_total=monto_total+cantidad*precio
            articulos[contador].append(compra)
            opcion=input("Escribe si deseas continuar (1-Continuar registrando/0-Dejar de registar: ")
        print(f"N° {contador}")
        for i in articulos[contador]:
            print(f"Descripcion: {i[1]}\t {i[2]}X ${i[3]}\tMonto Total: {i[4]}\n")
        print("\nMonto total a pagar: ",monto_total)
        input("<<ENTER>>")
    elif opcion =='2':
        total=0
        print("\n\tConsulta tus ventas\n")
        buscar=int(input("Introduce el numero de venta a buscar: "))
        if buscar in articulos:
            for consulta in articulos[buscar]:
                print(f"Descripcion: {consulta[1]}\t {consulta[2]}X ${consulta[3]}\tMonto Total: {consulta[4]}\n")
                total=total+consulta[4]
            print(f"Precio a pagar {total}")
        else:
            print("\n\tNo se ha encontrado dicho numero de venta")
        input("<<ENTER>>")


    elif opcion =='3':
        print("\tObtener un reporte de ventas para una fecha en específico\n")
        print(articulos)
        try:
            with open("datos.csv", "w", newline="") as archivo:
                registrador = csv.writer(archivo)
                registrador.writerow(("Clave","Descripcion","Cantidad","Precio","Total","Fecha de Venta"))
                for i in articulos.keys():
                    registrador.writerows(articulos[i])
        except Exception as e:
            print(f"Ocurrio un Error {e}\nVuelve a intentarlo\n")
        finally:
            archivo.close()






    elif opcion =='X':
        print("\nSaliendo...\n")
        break
    else:
        print("\n\nError vuelve a intentarlo\n\n")
        input("<<ENTER>>")
