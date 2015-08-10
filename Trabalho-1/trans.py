#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
nome = raw_input("Digite um valor a ser cryptografado\n")
list_cypt = list(nome)
while True:
  key  = input("Digite o numero de linhas \n")
  if key in range(2, len(nome)):
    break
  else:
    print("Valor inválido.")
row  = len(nome) / key
if (len(nome) % key) > 0:
  row = row + 1
mat = numpy.zeros((key, row), dtype=numpy.int)
#print(mat)
for i in range(0, row):
  for ii in range (0, key):
    if (len(list_cypt) == 0):
      #print("Zerou")
      break
    mat[ii, i] = ord(list_cypt.pop(0))
#print(mat)
lista_cod = list()
for i in range(0, key):
  for ii in range (0, row):
    lista_cod.append(chr(mat[i, ii]))
print("\nValor Codificado \n")
print(''.join(lista_cod))
print("\nRevertendo \n")
lista_desc = list()
for i in range(0, row):
  for ii in range(0, key):
    if (mat[ii, i] == 0):
      break
    lista_desc.append(chr(mat[ii, i]))
#print(lista_desc)
print(''.join(lista_desc))