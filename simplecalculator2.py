#!/usr/bin/env python
# -*- coding: utf-8 -*-

#giris paneli
print "HESAP MAKINASi"
print "Coded By Cassie"
admin = "fecassie"
sifre = "12345"
cks = "cikis"

a=1


while a==1:

        giris = str(raw_input("Kullanici adi(cikmak icin 'cikis' yazin):"))
        giriss = str(raw_input("sifre:"))

        if giris == admin and giriss == sifre:
            print("giris yapildi")
            a=2
        elif giris == "cikis":
            quit()
        else:
            print("yanlis kullanici adi veya sifre!")
#hesap makinası için:


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
        
        s1 = int(input("islem yapmak istediginiz sayiyi giriniz:"))
        s2 = int(input("islem yapmak istediginiz diger sayiyi giriniz:"))
        i = str(raw_input("yapmak istediğiniz işlemi giriniz:"))

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
