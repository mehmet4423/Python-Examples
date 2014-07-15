#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
print "Şu an bulunduğun dizin ----> %s" %os.getcwd()
dehayde = raw_input("Gitmek istedigin dizini gir ----> ")
os.chdir(dehayde)
if dehayde == os.getcwd():
	print "%s dizinine başarıyla geçiş yapıldı!" %os.getcwd()
else:
	print "Üzgünüm tekrar dene.."
