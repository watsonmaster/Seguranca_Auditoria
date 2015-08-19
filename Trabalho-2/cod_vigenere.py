#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program de Criptografia Cifra de Vigenère

def val_cod(key_val, char_val):
  val_final = (key_val + char_val)
  if (val_final > 255):
    return (val_final%255)
  return val_final

def input_file(nome_arq):
  with open(nome_arq, "rb") as f:
    byte = f.read()
  info = [byte[i:i+1] for i in range(0, len(byte), 1)]
  return info
  
def output_file(out_info, out_name):
	nome_cypt = str(out_name[0:-3]) + "cry"
	arq_out = open(nome_cypt, "wb+")
	arq_out.write(out_info)
	arq_out.close()


nome = raw_input("Digite um arquivo a ser cryptografado\n")
list_clean = input_file(nome)
list_cypt = list_clean
key = list(raw_input("Digite a Chave de Codificação\n"))
#print(key)
key_index = 0
#print(key_index)
for x in range(0, len(list_cypt), 1):

  if (key_index < len(key)):
    val_key = ord(key[key_index])
    list_cypt[x] = chr(val_cod(val_key, ord(list_clean[x])))
    key_index = key_index + 1
  else:
    key_index = 0
    val_key = ord(key[key_index])
    list_cypt[x] = chr(val_cod(val_key, ord(list_clean[x])))

#print(list_cypt)
#print(''.join(list_cypt))
output_file(''.join(list_cypt), (str(nome[:-3]+"cry")))


