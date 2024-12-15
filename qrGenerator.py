import qrcode

def makeQR(qrData,fileName):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(qrData)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(fileName+".png")

def contactDetails():
    firstName=input("enter first name : ")
    secondName=input("enter second name: ")
    mobleNumber=input("enter mobile number: ")
    email=input("enter email address: ")
    contactDetails = "BEGIN:VCARD\nVERSION:3.0\nN:"+secondName+";"+firstName+";"+";\nFN:"+firstName+secondName+"\nORG:Acme Corporation\nTEL;WORK;VOICE:"+mobleNumber+"\nEMAIL;WORK:"+email+"\nEND:VCARD"
    makeQR(contactDetails,firstName+secondName)

def qrURL():
    makeQR(input("enter url: "),input("enter file name: "))


if(  int(input("enter 1 for creating vcard QR: ")) != 1 ):
    qrURL()
    
else:
    contactDetails()

