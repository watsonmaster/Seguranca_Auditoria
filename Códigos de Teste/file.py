#!/usr/bin/env python
# -*- coding: utf-8 -*-

#arq = open("file.bin","wb")
#arq.write("Teste")

#arq.close()

arq = open("file.bin", "ab+")
#arq.seek(0,2)
texto = raw_input("Digite\n")
for x in range(0, 100):
	arq.write(texto)
arq.close()