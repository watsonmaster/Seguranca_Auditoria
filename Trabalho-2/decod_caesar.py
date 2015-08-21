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
  #arq_out = open("arq_out.kod", "wb+")
  nome_cypt = str(out_name[0:-3]) + "dec"
  arq_out = open(nome_cypt, "wb+")
  arq_out.write(out_info)
  arq_out.close()

def val_cod(key_val, char_val):

  return (char_val + key_val)%255

def val_desc(key_val, char_val):
  if (key_val == 0): return char_val
  return (char_val + (255-key_val))%255


nome_file = raw_input("Digite o Arquivo para Descripografar\n")
val_cypt = list(input_file(nome_file))
#val_cypt = list(input_file("arq_out.kod"))
Key = input("Digite a Key\n")
list_desc = val_cypt

for x in range(0, len(val_cypt)):
   #list_desc[x] = chr(ord(val_cypt[x]) - Key)
   list_desc[x] = chr(val_desc(Key, ord(val_cypt[x])))
val_desc = ''.join(list_desc)
#print(val_desc)

output_file(val_desc, nome_file)