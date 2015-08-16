#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program de Criptografia Cifra de Cesar

#Função de Vefificação de Ciclo em Cifra de Caesar

def val_cod(key_val, char_val):
  val_final = (key_val + char_val)
  if (val_final > 255):
    return (val_final%255)
  return val_final

def val_desc(key_val, char_val):
  if (key_val == 255):
    key_val = 1
  val_final = char_val - (key_val%255)
  if(val_final <= 0):
    return 255 - abs(char_val - (key_val%255))
  return val_final

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
  #list_cypt[x] = chr(ord(nome[x]) + Key)
  list_cypt[x] = chr(val_cod(Key, ord(nome[x])))
val_cypt = ''.join(list_cypt)
print(val_cypt)
list_desc = list_cypt
for x in range(0, len(val_cypt)):
   #list_desc[x] = chr(ord(val_cypt[x]) - Key)
   list_desc[x] = chr(val_desc(Key, ord(val_cypt[x])))
val_desc = ''.join(list_desc)
print(val_desc)