import qrcode

#taking upi id as a layout

upi_id= input("enter your upi id = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=currency&tn=message

# defining the payment url details on the upi id and the payment app

# you can modify these urls based on your payment app you want to support


phone_url=f"upi://pay?pa={upi_id}&pn=Your Name&am=100&cu=INR&tn=Payment for services"
payment_url=f"upi://pay?pa={upi_id}&pn=Your Name&am=100&cu=INR&tn=Payment for services"
google_pay_url=f"upi://pay?pa={upi_id}&pn=Your Name&am=100&cu=INR&tn=Payment for services"

# create or codes for each payment app

phone_qr=qrcode.make(phone_url)
payment_qr=qrcode.make(payment_url)
google_pay_qr=qrcode.make(google_pay_url)

#save the qr  codes to image file options
phone_qr.save('phone_qr.png')
payment_qr.save('payment_qr.png')
google_pay_qr.save('google_pay_qr.png')

#  display the qr codes 
phone_qr.show()
payment_qr.show()
google_pay_qr.show()