def cargarContactos():
    info_contactos = leerArchivo()
    contactos = []
    for linea in info_contactos:
        linea = linea.replace("\n", "")
        c = linea.split(",")
        contactos.append(c)
    print(contactos)

    return contactos

def leerArchivo():
    try:
        n_archivo = "contactos" + ".txt"
        archivo = open("Archivos/" + n_archivo)
        contenido = archivo.readlines()
        return contenido
    except Exception as error:
        print(error)