# To install Telepot
sudo pip install telepot

# To create new file 
Sudo nano tele.py

# import all necessary libraries
import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

# defininig and initializing LEDs as output pins and setup GPIOs
green=6
yellow=13
red=19
blue=2

now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(blue,GPIO.OUT)
GPIO.output(blue,0)

GPIO.setup(yellow,GPIO.OUT)
GPIO.output(yellow,0)

GPIO.setup(red,GPIO.OUT)
GPIO.output(red,0)

GPIO.setup(green,GPIO.OUT)
GPIO.output(green,0)




# Whenever the Pi receives a message from the Telegram bot, it will call the action function and this function reads the message and separate the text from it.
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: %s' % command)

# Now, by using the if condition we will toggle the LED by using the keywords used in programming.
    if 'on' in command:       
        message = "on"
        
        if'blue' in command:
            message = message + "blue"
            GPIO.output(blue,1)

        if 'yellow' in command:
            message = message + "yellow"
            GPIO.output(yellow,1)

        if'red' in command:
            message = message + "red"
            GPIO.output(red,1)

        if'green' in command:
            message = message + "green"
            GPIO.output(green,1)

        if 'all' in command:
          message= message+ "all"
          GPIO.output(blue,1)
          GPIO.output(yellow,1)
          GPIO.output(red,1)
          GPIO.output(green,1)
          message=message+ "light(s)"
          telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
         message = "off "
         if 'blue' in command:
            message = message + "blue "
            GPIO.output(blue, 0)

         if 'yellow' in command:
            message = message + "yellow "
         if 'red' in command:
            message = message + "red "
            GPIO.output(red, 0)

         if 'green' in command:
            message = message + "green "
            GPIO.output(green, 0)
         if 'all' in command:
            message= message+ "all"
            GPIO.output(blue,0)
            GPIO.output(yellow,0)
            GPIO.output(red,0)
            GPIO.output(green,0)
            message= message+ "lights(s)"
            telegram_bot.sendMessage (chat_id, message)

#  The “bot.getMe()” will check whether a connection between the Pi and the Telegram bot was made successfully by printing a response, and enter the Token Number

telegram_bot =telepot.Bot('1744905365:AAFBb_vAQhpcG6tkbAS4y1_eR8VHW0FF00A')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
time.sleep(10)
