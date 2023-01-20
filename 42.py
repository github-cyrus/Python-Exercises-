# whatsapp boomber

# import random
import pyautogui as pg
import time


A = int(input("Enter Your No Of Mess : \n"))


B = str(input("Enter ur Mess\n"))

time.sleep(10)

for i in range(A):
      pg.write(B)
      pg.press("Enter : ")