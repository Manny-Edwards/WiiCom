import cwiid, time

button_delay = 0.1
print ('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)

def getTranslation():
 try:
   wii=cwiid.Wiimote()
 except RuntimeError:
   print ("Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!")
   quit()

 print ('Wiimote connection established!\n')
 print ('Go ahead and press some buttons\n')
 print ('Press PLUS and MINUS together to disconnect and quit.\n')

 time.sleep(3)

 wii.rpt_mode = cwiid.RPT_BTN
 running = True
 translations=[]
 letter = []
 while running:
  buttons = wii.state['buttons']
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
   print ('\nClosing connection ...')
   wii.rumble = 1
   time.sleep(.5)
   wii.rumble = 0
   time.sleep(4)
   running = False
  if (buttons & cwiid.BTN_DOWN):
   if (len(letter)<=4):
     translations.append(letter)
     print("letter saved.")
   else:
     print("Your letter should be 4 or less characters. Please try again.")
   letter=[]
   time.sleep(button_delay)
   if (buttons & cwiid.BTN_A):
       print('Rumbling Now')
       wii.rumble = 1
       time.sleep(1)
       wii.rumble = 0
       letter.append('dash')
       time.sleep(button_delay)

   if (buttons & cwiid.BTN_B):
       print ('Button B pressed')
       letter.append('dot')
       time.sleep(button_delay)
   return translations

def receive_translations(list):
 print('Connect Wiimote to recieve messages:')
 print ('Please press buttons 1 + 2 on your Wiimote now ...')
 time.sleep(1)
 try:
  wii=wii=cwiid.Wiimote()
 except RuntimeError:
   print ("Cannot connect to your Wiimote.Please try again!")
   quit()
 letter=[]
 word=[]
 for letters in list:
  for chr in letters:
   if (chr==("dash")):
    wii.rumble=1
    time.sleep(1)
    wii.rumble=0
    time.sleep(1)
    letter.append('-')
   if (chr==("dot")):
    time.sleep(2)
    letter.append('0')
  print("",letter)
  letter=[]
  wii.led = 15
  time.sleep(1)
  wii.led = 0
