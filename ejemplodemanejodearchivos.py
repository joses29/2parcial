def leer():
    with open ('nombres.txt','r',encoding='UTF-8') as f:
        nombre = [line[:-1] for line in f]
        print(nombre)

def escribir():
    nombres = ['Josue','Andres','Luis','Erick','Maria','Diana']

    with open('nombres.txt','w',encoding='UTF-8') as f:
        for nombre in nombres:
            f.write(nombre)
            f.write('\n')
def run():
    escribir()
    leer()

if __name__ == '__main__':
    run()