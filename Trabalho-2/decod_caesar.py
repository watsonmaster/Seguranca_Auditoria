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


#val_cypt = list(input_file(raw_input("Digite o Arquivo para Descripografar\n")))
val_cypt = list(input_file("arq_out.kod"))
Key = input("Digite a Key\n")
list_desc = val_cypt

for x in range(0, len(val_cypt)):
   #list_desc[x] = chr(ord(val_cypt[x]) - Key)
   list_desc[x] = chr(val_desc(Key, ord(val_cypt[x])))
val_desc = ''.join(list_desc)
print(val_desc)