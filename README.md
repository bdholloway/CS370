**Works on IOS Google Authenticator App that was shown in instructions. Did not get to try it on other platforms.
**This was run on VSCode terminal
**used pip install for following
    1. Pillow            7.1.2
    2. qrcode            6.1

How To Run Program
    1. Runs on Python 3.7.7
    2. Must run: pip install qrcode[pil]
        NOTE: Did this step on VSCode Terminal, was having trouble on flip servers. I suspect that the python version is not right on the flip servers.
    3. Must Run --generate-qr command first to generate key file and URI in a qrcode.
        *Run using: python submission.py --generate-qr
    4. Then Run --get-otp
    *Run using: python submission.py --get-otp

NOTE: --get-otp will update every 30 seconds. Runs forever 

Steps to Authentication
    1. open the qrcode.png that was created
    2. scan using authenticator app
    3. run --get-otp to get code
    4. can verify code against code given by google authenticator app

Full Process:
    1. python submission.py --generate-qr
        Label: Bob
        User: Bob@google.com
    2. python submission.py --get-otp 
    3. Scan code with authenticator app
    4. compare codes