#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
arquivo = open("cod.txt","r")
list_key = numpy.zeros((256), dtype=numpy.int)
for i in range(0, 256):
	list_key[i] = int(arquivo.readline())
arquivo.close()
list_desc = numpy.zeros((256), dtype=numpy.int)
for i in range(0, 256):
	list_desc[list_key[i]] = i

#print(list_key)
#print(list_desc)
nome = raw_input("Digite um valor a ser cryptografado\n")
list_cypt = list(nome)
list_name = numpy.zeros((len(nome)), dtype=numpy.int)
list_pure = numpy.zeros((len(nome)), dtype=numpy.int)

for i in range(0, len(list_cypt)):
	list_name[i] = list_key[ord(list_cypt[i])]
print(list_name)

for i in range(0, len(list_name)):
	list_pure[i] = list_desc[list_name[i]]
print(list_pure)

for i in range(0, len(list_cypt)):
	list_cypt[i] = chr(list_pure[i])
print(''.join(list_cypt))