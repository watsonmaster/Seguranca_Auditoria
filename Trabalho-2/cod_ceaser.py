#!/usr/bin/env python
# -*- coding: utf-8 -*-

def input_file(nome_arq):
  with open(nome_arq, "rb") as f:
    byte = f.read()
    #print(len(byte))
    #print(byte)
  info = [byte[i:i+1] for i in range(0, len(byte), 1)]
  #print(info)
  return info

def output_file(out_info, out_name):
  #arq_out = raw_input("Digite arquivo Output\n")
  #arq_out = open("arq_out.kod", "ab+")
  nome_cypt = str(out_name[0:-3]) + "cry"
  arq_out = open(nome_cypt, "wb+")
  arq_out.write(out_info)
  arq_out.close()


def val_cod(key_val, char_val):

  return (char_val + key_val)%255

def val_desc(key_val, char_val):
  if (key_val == 0): return char_val
  return (char_val + (255-key_val))%255

##Inicio PROGRAMA

nome_file = raw_input("Digite o arquivo a ser criptografado\n")
nome = input_file(nome_file)
list_cypt = nome
#print(list_cypt)
while True:
  Key  = input("Digite o valor da cifra (chave) 0 - 255 \n")
  if Key in range(0, 256):
    break
  else:
    print("Valor inválido.")
#print(len(nome))
for x in range(0, len(nome)):
  #list_cypt[x] = chr(ord(nome[x]) + Key)
  if (chr(val_cod(Key, ord(nome[x]))) > 255): 
	print("Fodeu")
  list_cypt[x] = chr(val_cod(Key, ord(nome[x])))
val_cypt = ''.join(list_cypt)
output_file(val_cypt, nome_file)

##Fim Criptografia