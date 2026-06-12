# Lista para guardar los voluntarios en memoria
voluntarios = []

def reg_voluntario():
    print("REGISTRO DE VOLUNTARIOS")

    mat = input("Matrícula: ")
    nom = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")
    tel = input("Teléfono: ")

    voluntario = {
        "matricula": mat,
        "nombre": nom,
        "edad": edad,
        "correo": correo,
        "telefono": tel
    }
    voluntarios.append(voluntario)

    # Guardar en archivo de texto
    archivo = open("voluntarios.txt", "a")
    archivo.write(f"{mat},{nom},{edad},{correo},{tel}\n")
    archivo.close()

    print("Voluntario registrado correctamente.")

def most_vol():
    print("\n=== VOLUNTARIOS REGISTRADOS ===")

    archivo = open("voluntarios.txt", "r")

    for linea in archivo:
        datos = linea.strip().split(",")

        print("Matrícula:", datos[0])
        print("Nombre:", datos[1])
        print("Edad:", datos[2])
        print("Correo:", datos[3])
        print("Teléfono:", datos[4])
        print("-" * 20)

    archivo.close()

# Programa principal
reg_voluntario()
most_vol()
