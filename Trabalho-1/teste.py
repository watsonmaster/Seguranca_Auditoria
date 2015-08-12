#!/usr/bin/env python
# -*- coding: utf-8 -*-
texto = "1234567890123"
chave = "voces"
modi = len(texto)%len(chave)
mult = len(texto) / len(chave)
lista = list()
for i in range(0, mult):
	lista.append(chave)
lista.append(chave[:modi])
print(lista)
chave_final = ''.join(lista)
print(chave_final)