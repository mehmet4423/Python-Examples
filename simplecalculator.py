#!/usr/bin/env python
#!-*- coding:utf-8 -*-

from __future__ import division

print "*****              HESAP MAKINESI            *****"
print "Coded By Fatih Erdogan -Cassie23-"
print ""
print ""


admin = "Cassie23"
passwrd = "21180"
ckis = "Cikis"

a=1

while a==1:
	
    giris = str(raw_input("Kullanici Adi ( cikmak icin 'Cikis' yazin ) : "))
    giris2 = str(raw_input("Parola : "))
	
    if giris == admin and giris2 == passwrd:
        print ("Giris Yapildi!")
        print ""
        print ""
        a=2

    elif giris == "Cikis" :
        quit()

    else:
        print ("Yanlis Kullanici Adi veya Parola Girdiniz!!")


a="topla"
b="cikar"
c="carp"
d="bol"
e="us"
f="karekok"
g="mod"
h="cikis"
            
print (a,b,c,d,e,f,g,h)

while True:
    try:

        
        sayi1 = int(input("Islem Yapmak Istediginiz 1.sayiyi Giriniz : "))
        sayi2 = int(input("Islem Yapmak Istediginiz 2.sayiyi Giriniz : "))
        islem = str(raw_input("Yapmak Istediginiz Islemi Giriniz : "))

        if i == a:
            print s1+s2
        elif i == b:
            print s1-s2
        elif i == c:
            print s1*s2
        elif i == d:
            print float(s1)/s2
        elif i == e:
            print s1**s2
        elif i == f:
            print s1**(1.0/float(s2))
        elif i == g:
            print s1%s2
        elif i == h:
            print "tesekkurler"
            print ""
            print ""
            print ""
            print ""
            print ""
            quit()
        else :
            print "yanlis islem komutu girdiniz tekrar deneyin"
            print (a,b,c,d,e,f,g,h)
            
        
    except ValueError:
        print "islem yapmak icin iki SAYİ girdikten sonra islem komutunu YAZİYLA yazin"    
    except ZeroDivisionError:
        print "sayilar 0'a bolunemezler"
    except NameError:
        print "islem yapmak icin iki SAYİ girdikten sonra islem komutunu YAZİYLA yazin"


        



        
