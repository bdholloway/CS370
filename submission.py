import qrcode
import sys

def generateqr():
    print("Generating QR")

def getotp():
    print("Getting OTP")

if __name__ == "__main__":
    print("Now running " + sys.argv[0])
    qr = "--generate-qr"
    otp = "--get-otp"
    if len(sys.argv) < 2:
        print("Number of arguments is incorrect")
        exit()
    if(sys.argv[1]) == qr:
        generateqr()
    elif(sys.argv[1]) == otp:
        getotp()
    else:
        print("invalid arguments")