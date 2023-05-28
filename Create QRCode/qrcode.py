import qrcode  #import qrcode (the libraries pillow and qrcode must be downloaded)
my_qrcode = qrcode.make('Put the link here') #it will generate a qrcode to the link you put 
my_qrcode.save('qrcode.png') #you can save the qrcode as you want. I saved as 'qrcode'
my_qrcode.show() #it will show the qrcode 
