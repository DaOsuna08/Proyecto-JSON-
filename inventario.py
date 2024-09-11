import json

#Las siguientes dos funciones unicamente evaluan si el valor que el usuario vaya a ingresar en los apartados de precio y cantidad sean validos, cayendo en un bucle hasta que se ingrese un valor valido
#Y después de evaluar se transforma en un tipo numérico y en el caso del precio se divide entre 100, así en cada punto en el que se use cualquiera de las 2 funciones definidas
def comp_pr (pr):
    intentos = 1
    while intentos <= 5:
        if intentos == 5:
            print ("Operación cancelada debido a exceso de intentos fallidos")
            todo_bien == False
            break
        elif not pr.isnumeric():
            print("El valor ingresado como 'precio' no es válido, por favor intente nuevamente")
            pr = input("Ingrese el precio de venta del artículo como número entero, si es valido se aplicarán dos (2) cifras decimales.\nPor ejemplo: '299', que luego pasa a ser 2.99\n")
            intentos += 1
        else:
            if float (pr) < 0:
                print ("El valor ingresado debe ser positivo")
                intentos += 1
                pr = input("Ingrese el precio de venta del artículo como número entero, si es valido se aplicarán dos (2) cifras decimales.\nPor ejemplo: '299', pasa a ser 2.99\n")
            else:
                break

def comp_ct (ct):
    intentos = 1
    while intentos <= 5:
        if intentos == 5:
            print ("Operación cancelada debido a exceso de intentos fallidos")
            todo_bien == False
            break
        elif not ct.isnumeric():
            print("El valor ingresado como 'cantidad' no es válido, por favor intente nuevamente")
            ct = input("Ingrese la cantidad de unidades del artículo (debe ser un número entero).\nPor ejemplo: '15'\n")
            intentos += 1
        else:
            if int (ct) < 0:
                print ("El valor ingresado debe ser positivo")
                intentos += 1
                ct = input("Ingrese la cantidad de unidades del artículo (debe ser un número entero).\nPor ejemplo: '15'\n")
            else:
                break

while True:
    with open ("inventario.json","r") as all:
        #guardo el inventario en una variable para usarlo luego
        arts = json.load(all)
    #menu del programa
    print("Se recomienda mostrar los archivos antes de hacer cualquier acción")
    orden = input("--Gestión de Inventario--\n 1) Crear Artículo\n 2) Mostrar todos los Artículos\n 3) Mostrar información de un Artículo\n 4) Actualizar información de un Artículo\n 5) Eliminar un Artículo\n 6) Salir\nEscoja una opción escribiendo su número: ")
#Crear    
    if orden == "1":
        clasif = input("Escriba  el tipo de artículo que va a ingresar.\nPor ejemplo: 'Azucar'\n").capitalize()
        name = input("Escriba  el nombre del artículo.\nPor ejemplo: 'A. Moltalban'\n").capitalize()
        price = input("Ingrese el precio de venta del artículo como número entero, si es valido se aplicarán dos (2) decimales.\nPor ejemplo: '299', que luego pasa a ser 2.99\n")
        cant = input("Ingrese la cantidad de unidades del artículo (debe ser un número entero).\nPor ejemplo: '15'\n")

        new_art = arts
        todo_bien = True

        #esta variable sera usada para asegurarse de que el usuario desea agregar el nuevo articulo
        if clasif in new_art:
            #si ya existe un articulo con el nombre dado por el usuario
            if name in new_art[clasif]:
                print("El artículo aludido ya está registrado, se le recomienda escojer la opción nro 4")
                todo_bien = False
            #si el articulo no existe en el registro
            else:
                comp_pr (price)
                price = float (price) / 100
                comp_ct (cant)
                cant = int (cant)
                art = {name:{"precio":price,"cant":cant}}
                new_art[clasif].update(art)
        #si la clasificacion no existe es creada automaticamente
        else:
            comp_pr (price)
            price = float (price) / 100
            comp_ct (cant)
            cant = int (cant)
            art = {clasif:{name:{"Precio":price,"Cant":cant}}}
            new_art.update(art)

        intentos_1 = 1
        while todo_bien:    
            print(art)
            sure = input("¿Está seguro de que desea registrar esos datos? (Escriba 'si' para registrarlos y 'no' para cancelar esta tarea).\n").lower()
            
            if intentos_1 == 3:
                print("Operación cancelada por exceso de intentos")
                break

            elif sure == "si":
                with open ("inventario.json","w") as new:
                    json.dump(new_art,new,indent=4)
                break
            
            elif sure == "no":
                break

            else:
                print("Debe escribir 'si' o 'no'\n")
                intentos_1 += 1
#Lectura:
    #General
    elif orden == "2":
        for k in arts:
            print (k,":")
            #muestra las clasificaciones de los articulos
            for v in arts[k]:
                print ("    -",v)
                #muestra los nombres de los articulos
    #Específica
    elif orden == "3":
        clas_art = input("Escriba el tipo de artículo:\n").capitalize()
        art = input("Escriba el nombre del artículo:\n").capitalize()

        while not clas_art in arts:
            print("Ese tipo de artículo no existe, vuelva a intentarlo")
            clas_art = input("Escriba el tipo de artículo:\n").capitalize()

        if not art in arts[clas_art]:
            print("Ese artículo no existe")
        else:
            print ("Nombre :",art)
            for i in arts[clas_art][art]:
                print(i,":",arts[clas_art][art][i])
                #muestra la informacion del articulo
#Modificacion
    elif orden == "4":
        clasif = input("Ingrese el tipo del artículo que desea modificar:\n").capitalize()
        #en esta parte el programa se asegura de que la clasificacion del articulo exista

        todo_bien = True
        #Esta variable será usada de la misma forma que en el apatado de creacion (bloque 1)

        while not clasif in arts:
            print("Ese tipo de artículo no existe. Por favor vuelva a intentarlo.")
            clasif = input("Ingrese el tipo del artículo que desea modificar:\n").capitalize()
        #hecho esto ya se escoje que modificar o si no se desea cambiar nada cancelar la orden
        mod = input("Escriba el dato que desea modificar ('tipo','nombre', 'precio' o 'cantidad') o 'cancelar' si desea abandonar el proceso:\n").lower()
        #aca el programa se asegura de recibir una de las opciones dadas
        intentos_1 = 1
        while mod != "tipo" and mod != "nombre" and mod != "precio" and mod != "cantidad" and mod != "cancelar" :
            if intentos_1 >= 3:
                print("Excedido el número de intentos")
                mod == "cancelar"
            else:
                mod = input("La entrada ingresada no es válida.\nEscriba el dato que desea modificar ('nombre', 'precio' o 'cantidad') o 'cancelar' si desea abandonar el proceso:\n").lower()
                intentos_1 += 1

        if mod == "cancelar":
            print("Modificación cancelada")

        
        elif mod == "tipo":
            #esta variable es el nuevo nombre de la clasificacion
            k_clasif = input("Ingrese el nuevo nombre del tipo de artículo:\n").capitalize()
            #mientras esta es la que se agregará a arts, donde se copia todo el contenido de la clasificacion que se va a cambiar
            n_clasif = {k_clasif:arts[clasif]}
            #se borra la clasificacion con el nombre anterior
            del arts[clasif]
            #se agrega la clasificacion con el nuevo nombre
            arts.update(n_clasif)
            with open ("inventario.json","w") as modif:
                json.dump(arts,modif,indent=4)
        
        else:
            name = input("Ingrese el nombre del artículo que desea modificar:\n").capitalize()
            #aca se asegura de que el articulo exista
            while not name in arts[clasif]:
                print("Ese artículo no existe. Por favor vuelva a intentarlo.")
                name = input("Ingrese el nombre del artículo que desea modificar:\n").capitalize()
            if mod == "nombre":
                k_name = input("Ingrese el nuevo nombre :\n").capitalize()
                #se crea un nuevo diccionario con los datos del articulo pero con el nuevo nombre
                n_name = {k_name:arts[clasif][name]} 
                del arts[clasif][name]
                #se elimina el articulo con el nombre anterior y se agrega el diccionario con el nombre actualizado
                arts[clasif].update(n_name)

            elif mod == "precio":
                n_price = input("Ingrese el nuevo precio. Recuerde que debe escribirlo como si fuera entero y que la unidad y la decena serán los valores decimales:\n")
                comp_pr (n_price)
                n_price = float (n_price) / 100
                #aqui solo se reemplaza el precio anterior por el nuevo
                arts[clasif][name]["precio"] = n_price

            elif mod == "cantidad":
                n_cant = input("Ingrese la cantidad actual de unidades (debe ser un número entero):\n")
                comp_ct (n_cant)
                n_cant = int (n_cant)
                #y aca solo se cambia la cantidad
                arts[clasif][name]["cant"] = n_cant
            
            intentos_2 = 1
            while todo_bien: 
                sure = input("¿Está seguro de que desea registrar esos nuevos datos? (Escriba 'si' para registrarlos y 'no' para cancelar esta tarea).\n").lower()
                
                if intentos_2 == 3:
                    print ("Operacion cancelada")
                    break

                elif sure == "si":
                    with open ("inventario.json","w") as new:
                        json.dump(arts,new,indent=4)
                    break
                
                elif sure == "no":
                    break

                else:
                    print("Debe escribir 'si' o 'no'\n")
                    intentos_2 += 1


#Eliminar    
    elif orden == "5":
        elim = input ("¿Desea eliminar solo un artículo (art) o una clasificación (clas) completa?\n")
        while elim != "art" and elim != "clas":
            print("Debe elegir una opción. Por favor vuelva a intentarlo.")
            elim = input ("¿Desea eliminar solo un artículo (art) o una clasificación (clas) completa?\n")
        if elim == "art":
            clasif = input("Ingrese el tipo del artículo que desea eliminar:\n").capitalize()
            name = input("Ingrese el nombre del artículo que desea eliminar:\n").capitalize()
            #esta variable sera usada de la misma forma que en el apartado 1
            todo_bien = True
            intentos_1 = 1
            while not clasif in arts:
                if intentos_1 == 3:
                    print("Operación cancelada por exceso de intentos")
                    todo_bien = False
                    break
                else:
                    print("Ese tipo de artículo no existe. Por favor vuelva a intentarlo.")
                    clasif = input("Ingrese el tipo del artículo que desea eliminar:\n").capitalize()
                    intentos_1 += 1
            if not name in arts[clasif]:
                print("Ese artículo no existe. Por lo tanto se omitirá la tarea actual.")
                todo_bien = False
            
            intentos_2 = 1
            while todo_bien:
                print(name,arts[clasif][name])
                sure = input("¿Está seguro de querer eliminar este artículo? Escriba 'si' o 'no'\n").lower()

                if intentos_2 == 3:
                    print("Operación cancelada por exceso de intentos")
                    break
                elif sure == "si":
                    #en este caso se borra el articulo de la variable arts y esta se agrega al inventario
                    del arts[clasif][name]
                    with open ("inventario.json","w") as bor:
                        json.dump(arts,bor,indent=4)
                    break

                elif sure == "no":
                    break
                
                else:
                    print("Debe escribir 'si' o 'no'\n")
                    intentos_2 += 1

        elif elim == "clas":
            clasif = input("Ingrese el tipo de artículo que desea eliminar:\n").capitalize()
            todo_bien = True
            intentos_3 = 1
            while not clasif in arts:
                if intentos_3 == 3:
                    print("Operación cancelada por exceso de intentos")
                    todo_bien = False
                    break
                else:
                    print("Ese tipo de artículo no existe. Por favor vuelva a intentarlo.")
                    clasif = input("Ingrese el tipo del artículo que desea eliminar:\n").capitalize()
                    intentos_3 += 1
            intentos_4 = 1
            while todo_bien:
                print(arts[clasif])
                sure = input("¿Está seguro de querer eliminar este tipo de artículo? Escriba 'si' o 'no'\n").lower()

                if intentos_4 == 3:
                    print("Operación cancelada por exceso de intentos")
                    break
                elif sure == "si":
                    del arts[clasif]
                    with open ("inventario.json","w") as bor:
                        json.dump(arts,bor,indent=4)
                    break

                elif sure == "no":
                    break
                
                else:
                    print("Debe escribir 'si' o 'no'\n")
                    intentos_4 += 1
#Fin de programa
    elif orden == "6":
        print ("Adios\n:D")
        break
#Otros casos
    else:
        print("\n\nDebe ingresar una opción válida")

#Se separa la siguiente vuelta del programa con 2 lineas vacias
    print("\n\n")