#!/usr/bin/python
 
# TFT Status monitor
#
# v1.0
#
# Based on script by mharizanov
#

import pygame
import sys
import time
from time import strftime
import os
import httplib
import urllib
import json
 
time_stamp_prev=0
 
#Set the framebuffer device to be the TFT
os.environ["SDL_FBDEV"] = "/dev/fb1"
 
#Get emoncms feed latest data
def getFeedVal(feedId):
    conn = httplib.HTTPConnection("###########SITE#########")
    conn.request("GET", "/emoncms/feed/value.json?apikey=########apikey##########&id=" + feedId)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    data = data.replace("\"", "")
    return data[:4]

def displayTime():
    screen.fill((0, 0, 255))

    font = pygame.font.Font(None, 45)
    power_grid = "Time" 
    textPowerGrid = font.render(power_grid, 0, (255,255,255))
    textRotatedPowerGrid = pygame.transform.rotate(textPowerGrid, 0)
    textpos = textRotatedPowerGrid.get_rect()
    screen.blit(textRotatedPowerGrid,(92,3))

    pygame.draw.line(screen, (255,255,255), (90,0) , (90,160),2)

    font = pygame.font.Font(None, 28)
    now=time.localtime()
    for setting in [("%H:%M:%S",60),("%d  %b",10)] :
         timeformat,dim=setting
         currentTimeLine = strftime(timeformat, now)
         text = font.render(currentTimeLine, 0, (255,255,255))
         Surf = pygame.transform.rotate(text, -90)
         screen.blit(Surf,(dim,20))
 
def displayPowerScreen():

    screen.fill((0, 0, 255))

    font = pygame.font.Font(None, 32)
    power_grid = "Daily Use" 
    textPowerGrid = font.render(power_grid, 0, (255,255,255))
    textRotatedPowerGrid = pygame.transform.rotate(textPowerGrid, 0)
    textpos = textRotatedPowerGrid.get_rect()
    screen.blit(textRotatedPowerGrid,(3,1))

    pygame.draw.line(screen, (255,255,255), (0,30) , (128,30),3)

    font = pygame.font.Font(None, 23)
    power_grid = "Grid: " + getFeedVal("2") + " kWh"
    textPowerGrid = font.render(power_grid, 0, (255,255,255))
    textRotatedPowerGrid = pygame.transform.rotate(textPowerGrid, 0)
    textpos = textRotatedPowerGrid.get_rect()
    screen.blit(textRotatedPowerGrid,(3,35))

    power_house = "Use: " + getFeedVal("4") + " kWh"
    textPowerHouse = font.render(power_house, 0, (255,255,255))
    textRotatedPowerHouse  = pygame.transform.rotate(textPowerHouse, 0)
    textpos = textRotatedPowerHouse.get_rect()
    screen.blit(textRotatedPowerHouse,(3,55))

    power_solar = "Solar: " + getFeedVal("7") + " kWh"
    textPowerSolar = font.render(power_solar, 0, (255,255,255))
    textRotatedPowerSolar = pygame.transform.rotate(textPowerSolar, 0)
    textpos = textRotatedPowerSolar.get_rect()
    screen.blit(textRotatedPowerSolar, (3,75))

    power_solar = "Gas: " + getFeedVal("33") + " m3"
    textPowerSolar = font.render(power_solar, 0, (255,255,255))
    textRotatedPowerSolar = pygame.transform.rotate(textPowerSolar, 0)
    textpos = textRotatedPowerSolar.get_rect()
    screen.blit(textRotatedPowerSolar, (3,95))

    pygame.draw.line(screen, (255,255,255), (0,117) , (128,117),1)

    power_grid = "T_out: " + getFeedVal("38") + " C"
    textPowerGrid = font.render(power_grid, 0, (255,255,255))
    textRotatedPowerGrid = pygame.transform.rotate(textPowerGrid, 0)
    textpos = textRotatedPowerGrid.get_rect()
    screen.blit(textRotatedPowerGrid,(3,120))

    power_house = "T_in: " + getFeedVal("37") + " C"
    textPowerHouse = font.render(power_house, 0, (255,255,255))
    textRotatedPowerHouse  = pygame.transform.rotate(textPowerHouse, 0)
    textpos = textRotatedPowerHouse.get_rect()
    screen.blit(textRotatedPowerHouse,(3,140))


def main():
    pygame.init()
    global screen

    size = width, height = 128, 160
    black = 0, 0, 0
    white = 255, 255, 255
 
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode(size)

    while True: 
      	displayPowerScreen()
        pygame.display.flip()
	time.sleep(600)


if __name__ == '__main__':
    main()
