#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program de Criptografia Cifra de Vigenère

def val_desc(key_val, char_val):
  if (key_val == 255):
    key_val = 1
  val_final = char_val - (key_val%255)
  if(val_final <= 0):
    return 255 - abs(char_val - (key_val%255))
  return val_final
  
def input_file(nome_arq):
  with open(nome_arq, "rb") as f:
    byte = f.read()
  info = [byte[i:i+1] for i in range(0, len(byte), 1)]
  return info

def output_file(out_info, out_name):
  #arq_out = raw_input("Digite arquivo Output\n")
  #arq_out = open("arq_out.kod", "ab+")
  nome_cypt = str(out_name[0:-3]) + "dec"
  arq_out = open(nome_cypt, "wb+")
  arq_out.write(out_info)
  arq_out.close()


nome = raw_input("Digite um arquivo a ser cryptografado\n")
list_cypt = input_file(nome)
key = list(raw_input("Digite a Chave de Codificação\n"))

list_plain = list_cypt
key_index = 0
print(len(list_cypt))
for x in range(0, len(list_cypt), 1):
  if (key_index < len(key)):
    val_key = ord(key[key_index])
    list_plain[x] = chr(val_desc(val_key, ord(list_plain[x])))
    #list_plain[x] = chr(ord(list_plain[x]) - val_key)
    key_index = key_index + 1
    #print("somou valor " + str(key_index))
  else:
    key_index = 0
    val_key = ord(key[key_index])
    list_plain[x] = chr((val_desc(val_key, ord(list_plain[x]))))
    
#print(''.join(list_plain))
output_file(''.join(list_plain), nome)