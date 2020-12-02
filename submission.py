import qrcode
import os
import sys
import time
import random
import hmac
import hashlib
import struct
import base64
import threading
from PIL import Image

#References
#https://github.com/google/google-authenticator/wiki/Key-Uri-Format
#https://www.geeksforgeeks.org/python-pil-image-open-method/
#https://tools.ietf.org/html/rfc6238
#https://kite.com/python/answers/how-to-add-leading-zeros-to-a-number-in-python
#https://www.guru99.com/python-check-if-file-exists.html
#https://docs.python.org/2/library/struct.html
#https://stackoverflow.com/questions/34520928/how-to-generate-a-qr-code-for-google-authenticator-that-correctly-shows-issuer-d
#https://tools.ietf.org/html/rfc4226


def generateqr():
    print("Working on qr")

    otpLabel = str(input("Insert Label (alice): "))
    otpUser = str(input("Insert User (alice@google.com): "))

    #Open/Create keyfile, name it "key"
    keyfile = open("./key", "w")
    #Generate key
    otpKey = ''.join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for u in range (0,16)])
    #Put key in file
    keyfile.write(otpKey)
    #Close file
    keyfile.close()


    #otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example
    #generate URI, match it to above example
    ga_uri = "otpauth://totp/" + otpLabel + ":" + otpUser + "?secret=" + otpKey + "&issuer=" + otpLabel
    #make and save image
    qrcode.make(ga_uri).save("qrcode.png")
    #open qr image
    im = Image.open("./qrcode.png")
    im.show()

    print("Successful qr creation")

    return

def getotp():
    print("Working on otp")
    #30 second timer
    threading.Timer(30.0, getotp).start()

    #Check that keyfile has been created, if it has read file and put into key
    if(os.path.exists("key")):
        keyfile = open("./key", "r")
        key = keyfile.readlines()
        key = key[0].replace("\n", "")
    else:
        print("Key File failed to load, try running --generate-qr first")
        exit()

    otpKey = base64.b32decode(key)

    otpInterval = ((int(time.time())) - 0)//30
    otpInterval = struct.pack(">Q", otpInterval)
    otpHashOut = hmac.new(otpKey, otpInterval, hashlib.sha1).hexdigest()
    otpStartIndex = int(otpHashOut[-1:], 16)
    otpHashSub = otpHashOut[otpStartIndex*2 : (otpStartIndex*2)+8]

    #convert to int
    otpCode = (int("0x" + str(otpHashSub), 16) & 0x7fffffff) % 1000000

    #Padd number with 0's if beginning contains a zero(s)
    if(len(str(otpCode)) < 6):
        oc = str(otpCode)
        UpdatedOTP = oc.zfill(6)
        otpCode = UpdatedOTP


    print(otpCode)

    return

if __name__ == "__main__":
    print("Now running " + sys.argv[1])
    qr = "--generate-qr"
    otp = "--get-otp"
    if len(sys.argv) < 2:
        print("Number of arguments is incorrect")
        exit()
    if(sys.argv[1]) == qr:
        print("generating qr")
        generateqr()
    elif(sys.argv[1]) == otp:
        print("generating otp")
        getotp()
    else:
        print("invalid arguments")

