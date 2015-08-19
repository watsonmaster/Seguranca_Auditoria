#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq_name = raw_input("Digite arquivo Input\n")
arq_in = open(arq_name, "ab+")
arq_in.write(raw_input("Digite Informação\n"))

arq_in.close()