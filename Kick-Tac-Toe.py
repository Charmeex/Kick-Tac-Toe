from PIL import Image, ImageEnhance
import numpy as np
import functools as ft
import pygame
import pygame.camera
import mouse
import keyboard

def threshold(imageArray):
    global VarAr
    VarAr = []
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = ft.reduce(lambda x, y: int(x) + int(y), eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = ft.reduce(lambda x, y: int(x) + int(y), balanceAr)/len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if ft.reduce(lambda x, y: int(x) + int(y), eachPix[:3])/len(eachPix[:3]) > 240:
                eachPix = 255
                VarAr.append(eachPix)
            else:
                eachPix = 0
                VarAr.append(eachPix)
    return(newAr)

Tr = 0
Tc = 0
Tl = 0
Cr = 0
C = 0
Cl = 0
Br = 0
Bc = 0
Bl = 0
i = 1

pygame.camera.init()
cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()
while(True):
 if(i == 1):
     print("It's player 1's turn!")
 else:
     print("It's player 2's turn!")
 while(keyboard.is_pressed("ctrl") == False):
  if(keyboard.is_pressed("alt") == True):
      if(mouse.get_position() != (366, 1364)):
          mouse.move(376, 527, absolute = True, duration = 0)
          mouse.click("left")
          mouse.move(366, 1364, absolute = True, duration = 0)
          Tr = 0
          Tc = 0
          Tl = 0
          Cr = 0
          C = 0
          Cl = 0
          Br = 0
          Bc = 0
          Bl = 0
 i = webcam.get_image()
 pygame.image.save(i, "Img.png")
 i = Image.open("Img.png")
 i = i.resize((16,16), Image.ANTIALIAS)
 i_brightness_obj = ImageEnhance.Brightness(i)
 i = i_brightness_obj.enhance(2.8)
 i.save("Img.png")
 i = Image.open("Img2.png")
 iar = np.array(i)
 threshold(iar)
 if((0 in VarAr[74:76] or  0 in VarAr[90:92] or 0 in VarAr[106:108]) and Tr == 0):
     print("Top right")
     mouse.move(636, 264, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Tr = 1
 elif((0 in VarAr[72:73] or  0 in VarAr[88:89] or 0 in VarAr[104:105]) and Tc == 0):
     print("Top center")
     mouse.move(384, 266, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Tc = 1
 elif((0 in VarAr[69:71] or 0 in VarAr[85:87] or 0 in VarAr[101:103]) and Tl == 0):
     print("Top left")
     mouse.move(117, 260, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Tl = 1
 elif((0 in VarAr[122:124] or 0 in VarAr[138:140] or 0 in VarAr[154:156]) and Cr == 0):
     print("Center right")
     mouse.move(636, 526, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Cr = 1
 elif((0 in VarAr[120:121] or 0 in VarAr[136:137] or 0 in VarAr[152:153]) and C == 0):
     print("Center")
     mouse.move(376, 527, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     C = 1
 elif((0 in VarAr[117:119] or 0 in VarAr[133:135] or 0 in VarAr[149:151]) and Cl == 0):
     print("Center left")
     mouse.move(118, 523, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Cl = 1
 elif((0 in VarAr[170:172] or 0 in VarAr[186:188] or 0 in VarAr[202:204]) and Br == 0):
     print("Bottom right")
     mouse.move(637, 782, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Br = 1
 elif((0 in VarAr[168:169] or 0 in VarAr[184:185] or 0 in VarAr[200:201]) and Bc == 0):
     print("Bottom center")
     mouse.move(381, 780, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Bc = 1
 elif((0 in VarAr[165:167] or 0 in VarAr[181:183] or 0 in VarAr[197:199]) and Bl == 0):
     print("Bottom left")
     mouse.move(124, 778, absolute = True, duration = 0)
     mouse.click("left")
     mouse.move(366, 1365, absolute = True, duration = 0)
     Bl = 1
 else:
     print("Try again!")
 if(i == 1):
  i = 2
 else:
  i = 1
