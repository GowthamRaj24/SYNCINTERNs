import random
import string
import sys
import time
import pywhatkit


curr_time = time.strftime('%H:%M:%S')
x = string.ascii_letters
y = string.digits
z = x + y
rand = random.choices(z, k=6)
otp = ''
for i in rand:
    otp += i
print(otp)
mail = input('Enter your Email :- ')
#pywhatkit.send_mail(email_sender='', message=f"Your OTP is : {otp}, Don't Share it with anyone...",password='', subject='OTP VERIFICATION',email_receiver=mail)
print('Mail Sent Successfully...')
c = 1


def verify():
    global c
    global otp
    while c < 3:
        otp_received = input('Enter the OTP received :- ')
        if otp == otp_received:
            print('Verification Successfull...')
            sys.exit()
        else:
            print('Entered otp is Invalid')
            if c <= 3:
                print(f'Attempts left {3-c}')
                c += 1
            elif 3-c == 0:
                print('Try again later.....')
            elif c > 3:
                print('No.of limits Reached')
                return
            verify()
verify()