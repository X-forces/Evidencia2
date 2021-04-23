import datetime
import csv

def leer_csv(articulos):
    try:
        with open("datos.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter = ",")
            registros = 0
            if lector:
                for clave, descripcion, cantidad,precio,total,fechan in lector:
                    if registros == 0:
                        registros = registros + 1
                    else:
                        clave=int(clave)
                        if clave in articulos:
                            articulos[clave].append((clave,descripcion, int(cantidad),float(precio),float(total),fechan))
                        else:
                            articulos[clave]=[(clave,descripcion, int(cantidad),float(precio),float(total),fechan)]            
    except Exception as e:
        print("\n\n\tVerificando Almacenamiento..")
        input("<<ENTER>>")
        print("Memoria sincronizada\n")
    finally:
        archivo.close()
        
    return articulos

def generar(articulos):
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
    return articulos 

articulos={}
if not articulos:
    with open("datos.csv", "a") as archivo:
        archivo.close()

leer_csv(articulos)

while True:
    print("\n\tMenu principal de Cosmeticos")
    print("1-Registrar una venta")
    print("2-Consultar una venta")
    print("3-Obtener un reporte de ventas para una fecha en específico")
    print("X-Salir ")
    opcion = input("Elige una opcion: ")
    if opcion =='1':
        monto_total=0
        print("\n\tRegistrar")
        contador= max(articulos,default=0)+1
        articulos[contador]=[]
        while opcion !='0':
            while True:
                try:
                    descripcion = input(f"Escribe la descripcion de la venta {contador}: ")
                    cantidad = int(input("Escribe la cantidad a comprar del articulo: "))
                    precio= float(input(f"Escribe el precio del articulo: "))
                    fecha=input("Dime la fecha (dd/mm/aaaa): \n")
                    fecha_datetime = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
                    fecha_procesada = fecha_datetime.strftime('%d/%m/%Y')
                    break
                except Exception as e:
                    print(f'Error vuelve a intentarlo\t{e}')    
            compra = (contador,descripcion.upper(),cantidad,precio,cantidad*precio,fecha_procesada)
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
        while True:
            try:
                reporte_f=input("Dime la fecha ha encontrar (dd/mm/aaaa): \n")
                reporte_fecha = datetime.datetime.strptime(reporte_f, "%d/%m/%Y").date()
                print(f"Fecha {reporte_fecha}\n")
                for i in articulos.values():
                    for j in i:
                        if reporte_fecha.strftime('%d/%m/%Y') == j[5]:
                            print(f"\tFolio: {j[0]}\tDescripcion: {j[1]}\tCantidad: {j[2]}\tPrecio: {j[3]}\tTotal:{j[4]}\n")
                break
            except Exception as e:
                print(f"Error Vuelve a intentar\t{e}\n")
                input("<<Enter>>")
    elif opcion =='X':
        generar(articulos)
        print("\n\t\t**---Almacenando cambios del sistema--**\n")
        print("\nSaliendo...\n")
        break
    else:
        print("\n\nError vuelve a intentarlo\n\n")
        input("<<ENTER>>")
