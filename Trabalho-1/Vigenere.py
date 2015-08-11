#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program de Criptografia Cifra de Vigenère
#TO-DO fazer a parte de giro de valores acima de 255
nome = raw_input("Digite um valor a ser cryptografado\n")
list_cypt = list(nome)
key = list(raw_input("Digite a Chave de Codificação\n"))
print(key)
key_index = 0
print(key_index)
for x in range(0, len(list_cypt), 1):

  #list_cypt[x] = chr(ord(nome[x]) + ord(key[key_index]))
  #print("Chave é numero: " + str(key_index))
  if (key_index < len(key)):
    val_key = ord(key[key_index])
    #print(ord(nome[x]) + val_key)
    #print(nome[x])
    list_cypt[x] = chr(ord(nome[x]) + val_key)
    key_index = key_index + 1
    #print("somou valor " + str(key_index))
  else:
    key_index = 0
    val_key = ord(key[key_index])
    list_cypt[x] = chr(ord(nome[x]) + val_key)
    #print("Zerou")

print(list_cypt)
print(''.join(list_cypt))

list_plain = list_cypt
key_index = 0
for x in range(0, len(list_cypt), 1):
  if (key_index < len(key)):
    val_key = ord(key[key_index])
    list_plain[x] = chr(ord(list_plain[x]) - val_key)
    key_index = key_index + 1
    #print("somou valor " + str(key_index))
  else:
    key_index = 0
    val_key = ord(key[key_index])
    list_plain[x] = chr(ord(list_plain[x]) - val_key)

print(''.join(list_plain))
