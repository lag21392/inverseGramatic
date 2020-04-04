# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:22:34 2018

@author: LAG
"""

import mmap
import sys
import numpy
from os import listdir
import os
import shutil
from colorama import Fore, Back, Style 

def configurar():
    path="datos.bin"
    return path

def AbrirReadTXT(path):
#    with open(path, "r+") as f:
        return  open(path, "r+")
def AbrirWriteTXT(path):
    with open(path, "w") as f:
        return f
def cerrarArchivo(fd):
    return   fd.closed
def generarVectorDeCaracteres(path,vectorCaracteres):
    
    archivoTXT=AbrirReadTXT(path)
    while 1:
        caracter = archivoTXT.read(1)
        if not caracter:
            break
        else:
            if caracter not in vectorCaracteres:
                vectorCaracteres.append(caracter)
    cerrarArchivo(archivoTXT)
    return  vectorCaracteres           

def generarRelacionesDeCaracteres(path,vectorCaracteres,vectorRelaciones):
    
    archivoTXT1=AbrirReadTXT(path)
    archivoTXT2=AbrirReadTXT(path)
    archivoTXT2.read(1)
    while 1:
        caracter = archivoTXT1.read(1)
        caracterARelacionar = archivoTXT2.read(1)

        if not caracter or not caracterARelacionar:
            break
        else:
#            if caracter!=' ' and caracterARelacionar!=' ':
                
                if caracter not in vectorCaracteres:
                    vectorCaracteres.append(caracter)
                    i=vectorCaracteres.index(caracter)
                    j=vectorCaracteres.index(caracterARelacionar)
                    vectorRelaciones[i][j]+=1
                else:
                    
                    i=vectorCaracteres.index(caracter)
                    j=vectorCaracteres.index(caracterARelacionar)
                    vectorRelaciones[i][j]+=1
    
    cerrarArchivo(archivoTXT1)
    cerrarArchivo(archivoTXT2)
    return vectorRelaciones

def generarRelacionesDePalabras(path,vectorCaracteres,vectorRelaciones):
    archivoTXT1=AbrirReadTXT(path)
    archivoTXT2=AbrirReadTXT(path)
    
    encontradoPalabraArch1=0
    for i in range(0,len(vectorCaracteres)):
        tamanioPalabra1=len(vectorCaracteres[i])
        palabra1=vectorCaracteres[i]
        palabraArch1=archivoTXT1.read(tamanioPalabra1)
        if palabra1==palabraArch1:
            encontradoPalabraArch1=1
        else:
            archivoTXT1.seek(0)
    
        
    archivoTXT2.seek(tamanioPalabra1)
    encontradoPalabraArch2=0
    for i in range(0,len(vectorCaracteres)):
        tamanioPalabra=len(vectorCaracteres[i])
        palabra2=vectorCaracteres[i]
        
        palabraArch2=archivoTXT2.read(tamanioPalabra)
        if palabra2==palabraArch2:
            encontradoPalabraArch2=1
        else:
            archivoTXT2.seek(tamanioPalabra1)
    
        if encontradoPalabraArch2==1 and encontradoPalabraArch1==1:
            print("Se relaciona:",palabra1," con ",palabra2 )
#    maximoTamanioPalabra=0
#    for i in range(0,len(vectorCaracteres)):
#        if len(vectorCaracteres)>maximoTamanioPalabra:
#            maximoTamanioPalabra=len(vectorCaracteres)
#            
#            
#    archivoTXT1=AbrirReadTXT(path)
#    archivoTXT2=AbrirReadTXT(path)
#   
#    
#    #buscar de palabras mas grandes hasta palabras mas chicas
#    tamanioPalabra=maximoTamanioPalabra
#    encontrado=0
#    while encontrado==0 and maximoTamanioPalabra>=1:
#        palabraLeida= ++
#        print("analizando:",palabraLeida)
#        for i in range(0,len(vectorCaracteres)):
#             if palabraLeida==vectorCaracteres[i]:
#                 print("palabra encontrada Leida:",palabraLeida)
#                 encontrado=1
#                 archivoTXT1.seek(tamanioPalabra*(-1))
#             else:
#                 maximoTamanioPalabra=maximoTamanioPalabra-1
#                 
#    
#            
#    while 1:
#        caracter = archivoTXT1.read(1)
#        caracterARelacionar = archivoTXT2.read(1)
#        if not caracter or not caracterARelacionar:
#            break
#        else:
#               
#                if caracter not in vectorCaracteres:
#                    vectorCaracteres.append(caracter)
#                    i=vectorCaracteres.index(caracter)
#                    j=vectorCaracteres.index(caracterARelacionar)
#                    vectorRelaciones[i][j]+=1
#                else:
#                 
#                    i=vectorCaracteres.index(caracter)
#                    j=vectorCaracteres.index(caracterARelacionar)
#                    vectorRelaciones[i][j]+=1
#    
#    cerrarArchivo(archivoTXT1)
#    cerrarArchivo(archivoTXT2)
#    return vectorRelaciones
    
def mmapArchivoBinario(path,cantArchivos,filas,columnas):
    
    with open(path, "r+b") as f:
        # memory-map the file, size 0 means whole file
        matrix[cantArchivos][filas][columnas] = mmap.mmap(f.fileno(), 0)
    
        mm.close()


def ls(ruta = '.'):
    return listdir(ruta)
def parciar(texto,largo):
    textoA=str(texto)
    while len(textoA)<largo:
        textoA=textoA+" "
    return textoA
def parciarlistas(texto,largo):
    textoA=str(texto)
    while len(textoA)<largo:
        textoA=textoA+" "
    return textoA

def imprimirVectorRelaciones(vectorDeLetras,vectorRelaciones,modo):
    if modo==0:
        for i in range(0,len(vectorDeLetras)):                
            print(vectorRelaciones[i])
    if modo==1:    
        vectorAImprimir=[]
        for i in range(0,len(vectorDeLetras)):  
            vectorAImprimir.append([])
            for j in range(0,len(vectorDeLetras)):
                vectorAImprimir[i].append((vectorDeLetras[j],vectorRelaciones[i][j]))
        for i in range(0,len(vectorDeLetras)):
            vec=[vectorDeLetras[i]]
            if('\t'==vectorDeLetras[i]):
                print(vec,end=" ")
            else:
                print(vec,end="  ")
            print(str(vectorAImprimir[i]))
    if modo==2:              
        print(vectorDeLetras)
        for i in range(0,len(vectorDeLetras)):
            vec=[vectorDeLetras[i]]
            if('\t'==vectorDeLetras[i]):
                print(vec,end="")
            else:
                print(vec,end=" ")
            print(str(vectorRelaciones[i]))
#vectorAImprimir=[]
#for i in range(0,(len(vectorDeLetras)+1)):
#    for j in range(0,(len(vectorDeLetras)+1)):
#        vectorAImprimir.append([])
#        if i==0:
#            if j==0:
#                vectorAImprimir[i].append(0)
#            else:
#                vectorAImprimir[i].append(vectorDeLetras[j-1])
#        else:
#            if j==0:
#                vectorAImprimir[i].append(vectorDeLetras[i-1])
#            else:
##                print("i:",i,"j:",j," ",vectorRelaciones[i-1][j-1])
#                vectorAImprimir[i].append(vectorRelaciones[i-1][j-1])
##    vectorAImprimir[len(vectorAImprimir)-1].append(vectorDeLetras[i-1])
##    vectorAImprimir[len(vectorAImprimir)-1].append(vectorRelaciones[i][j])
#for i in range(0,len(vectorDeLetras)):                
#    print(vectorAImprimir[i])


pathEjecucion=os.getcwd()
print(pathEjecucion)
listaTXTs = ls(pathEjecucion+"/TXTs")

vectorDeLetras=[]
for TXT in listaTXTs:
    vectorDeLetras=generarVectorDeCaracteres(pathEjecucion+"/TXTs/"+TXT,vectorDeLetras)
numpy.sort(vectorDeLetras, axis=-1, kind='quicksort', order=None)


vectorRelaciones=[]
for i in range(0,(len(vectorDeLetras))):
    vectorRelaciones.append([])
    for j in range(0,(len(vectorDeLetras))):
        vectorRelaciones[i].append(0)

for TXT in listaTXTs:
    vectorRelaciones=generarRelacionesDeCaracteres(pathEjecucion+"/TXTs/"+TXT,vectorDeLetras,vectorRelaciones)


imprimirVectorRelaciones(vectorDeLetras,vectorRelaciones,2)
texto=str(AbrirReadTXT(pathEjecucion+"/textoAAnalizar.txt").read())

#saca maximo numero de la relacion 
maximoNum=0
for i in range(0,len(vectorDeLetras)):
    for j in range(0,len(vectorDeLetras)):
        if int(vectorRelaciones[i][j])>maximoNum:
            maximoNum=vectorRelaciones[i][j]
#print("Maximo Numero:",maximoNum) 

#imprime texto analizado con la relacion   
for i in range(0,7):
    color="\x1b[1;"+str(30+i)+"m"
    print(color+str(i),end="")
print(Style.RESET_ALL)
print("")
vectorPalabras=[""]
p=0
numColorAnt=0
primer=1

print("maximoNum",maximoNum)

for i in range(0,len(texto)-1):
    color=0
    if (texto[i] in vectorDeLetras) and (texto[i+1] in vectorDeLetras) :
        numRelacion=vectorRelaciones[vectorDeLetras.index(texto[i])][vectorDeLetras.index(texto[i+1])]
        
        numColor=round((numRelacion*8)/maximoNum)+30
    
    if (numColor==numColorAnt or primer==1) and numColor>30:
        primer=0
        vectorPalabras[p]=str(vectorPalabras[p])+texto[i]  
    else:
        
        if len(vectorPalabras[p])>1:
            p=p+1
            vectorPalabras.append("")
            vectorPalabras[p]=str(vectorPalabras[p])+texto[i]  
        
    numColorAnt=numColor
    color="\x1b[1;"+str(numColor)+"m"
    print(color+texto[i],end="")
    
print(Style.RESET_ALL)
print(set(vectorPalabras))


#
vectorDeLetras=vectorPalabras
for TXT in listaTXTs:
    vectorDeLetras=generarVectorDeCaracteres(pathEjecucion+"/TXTs/"+TXT,vectorDeLetras)
numpy.sort(vectorDeLetras, axis=-1, kind='quicksort', order=None)


vectorRelaciones=[]
for i in range(0,(len(vectorDeLetras))):
    vectorRelaciones.append([])
    for j in range(0,(len(vectorDeLetras))):
        vectorRelaciones[i].append(0)

for TXT in listaTXTs:
    vectorRelaciones=generarRelacionesDePalabras(pathEjecucion+"/TXTs/"+TXT,vectorDeLetras,vectorRelaciones)


imprimirVectorRelaciones(vectorDeLetras,vectorRelaciones,2)
#creamos matriz de palabras

#
