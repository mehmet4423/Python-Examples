#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import time
pygame.init()


genislik = 1000
yukseklik = 600
ekran = pygame.display.set_mode((genislik,yukseklik))
baslik = pygame.display.set_caption("Çakma Windows Ekran Koruyucu =)")

logo = pygame.image.load("windows.png")
arka_plan = pygame.draw.line(ekran,(255,255,255),(0,0),(0, yukseklik),genislik*2)



dongu = 1
k_x = 1
k_y = 300
yukari = 1
ilerle = 1
ekran.blit(logo,(k_x,k_y))
pygame.display.flip()
while dongu == 1:
	for olay in pygame.event.get():
		if olay.type == pygame.QUIT:
			dongu = 0


	if k_x == 0:
		ilerle = 1
		logo = pygame.transform.flip(logo,1,0)
	if k_x == 700:
		ilerle = 0
		logo = pygame.transform.flip(logo,1,0)

	if ilerle == 1:
		k_x = k_x + 1	
	if ilerle == 0:
		k_x = k_x - 1




	if k_y == 250:
		yukari = 1
	if k_y == 300:
		yukari = 0

	if yukari == 1:
		k_y = k_y + 1
	if yukari == 0:
		k_y = k_y - 1


	time.sleep(0.005)
	arka_plan = pygame.draw.line(ekran,(255,255,255),(0,0),(0, yukseklik),genislik*2)
	ekran.blit(logo,(k_x,k_y))
	pygame.display.flip()
