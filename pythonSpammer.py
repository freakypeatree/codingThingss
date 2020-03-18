import subprocess
import pynput.keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

#welcome screen and setup
print("Welcome to my spammer gamer\n\tplease type in the number you want to spam")
number = raw_input()

print("Now type in the message you want to spam")
message = raw_input()

print("Finally put in how many times you would like to spam them")
spam = raw_input()
spam = int(spam)

# opens messages and starts spam
subprocess.call(["/usr/bin/open", "/System/Applications/Messages.app"])
time.sleep(3)
keyboard.press(Key.cmd)
keyboard.press('n')
keyboard.release(Key.cmd)
keyboard.release('n')

time.sleep(3)
keyboard.type(number)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
for x in range(spam):
	keyboard.type(message)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(4)

print("The spam is complete")