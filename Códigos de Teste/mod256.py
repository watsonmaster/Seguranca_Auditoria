#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Função de Vefificação de Ciclo em Cifra de Caesar

def val_cod(key_val, char_val):

  return (char_val + key_val)%255

def val_desc(key_val, char_val):
  if (key_val == 0): return char_val
  return (char_val + (255-key_val))%255



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