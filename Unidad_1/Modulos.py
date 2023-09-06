#Hay modulos por defecto en Python 
import csv
import random

numRandom=random.randint(0,100)

while True:
    numero=int(input("Cual sera el numero entre 0 y 100:"))
    if numero==numRandom:
        break
    if numero>numRandom:
        print("El numero capturado es mayor")
    else:
        print("El numero capturado es menor")
    print(f"El numero era {numRandom}")

#Tema nulos
    
def split(inputFile,outPutName,lines):
    with open(inputFile,'r') as file:
        header = file.readline().strip()
        outPutFile=None
        linecount=0
        for line in file:
            if linecount % lines == 0:
                if outPutFile is not None:
                    outPutFile.close()
                outPutFile=open(f"{outPutName}_{linecount//lines}.csv",'w')
                outPutFile.write(header+'\n')
            outPutFile.write(line)
            linecount+=1
    if outPutFile is not None:
        outPutFile.close()

if __name__=="__main__":
    split("usuarios.csv","Ou")