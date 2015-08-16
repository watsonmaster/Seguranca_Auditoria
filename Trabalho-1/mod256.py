#!/usr/bin/env python
# -*- coding: utf-8 -*-

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



val = input()
key = input()
#if (val > 255):
  #print("OK")
  ##print("Mod 255 " + str(val%255) + " DIV 255 " + str(val/255))
#else:
  ##print(str(val % 255))
  #print("Abaixo")
  
print("teste funcao Criptografia " + str(val_cod(key, val)))
val = val_cod(key, val)
print("teste funcao Descriptografia " + str(val_desc(key, val)))