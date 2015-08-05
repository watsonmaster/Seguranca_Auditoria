#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program de Criptografia Cifra de Cesar
nome = raw_input("Digite um valor a ser cryptografado\n")
list_cypt = list(nome)
while True:
  Key  = input("Digite o valor da cifra (chave) 0 - 255 \n")
  if Key in range(0, 256):
    break
  else:
    print("Valor inválido.")
#print(len(nome))
for x in range(0, len(nome)):
  list_cypt[x] = chr(ord(nome[x]) + Key)
val_cypt = ''.join(list_cypt)
print(val_cypt)
list_desc = list_cypt
for x in range(0, len(val_cypt)):
   list_desc[x] = chr(ord(val_cypt[x]) - Key)
val_desc = ''.join(list_desc)
print(val_desc)