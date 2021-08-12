class life():
    import cv2
    from pyzbar import pyzbar
    def read_barcodes(frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y , w, h = barcode.rect
            #1
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            
            #2
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
            #3
            with open("barcode_result.txt", mode ='w') as file:
                file.write("Recognized Barcode:" + barcode_info)
        return frame
    def main():
            #1
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        #2
        while ret:
            ret, frame = camera.read()
            frame = read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            print(frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        #3
        camera.release()
        cv2.destroyAllWindows()
    #4
    if __name__ == '__main__':
        main()

class img():
    import pyqrcode
    from PIL import Image
    from pyzbar.pyzbar import decode
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
    from PIL import Image
    import pathlib    
    def convertToPNG():
        export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
        image.save(export_file_path)
        path = export_file_path
        return path
    qr = pyqrcode.create("test1")
    image = filedialog.askopenfilename()
    path = pathlib.Path(image)
    if path.suffix != ".png":
        image = convertToPNG
    img_path = "".join(image)
    qr.png(img_path, scale=6)
    data = decode(Image.open(img_path))
    print(data)
while True:  
    print("Choose The Mode You want ? \n press 1 if you want a live video scan\npress 2 if you want to insert an image to scan \npress 3 if you want to exit\n")
    choose = int(input())
    while choose != 1 or choose != 2 or choose != 3:
        print("please press 1 or 2 or 3")
        choose = int(input())
    if choose == 1:
        launch = life()
    elif choose == 2:
        launch = img()
    else:
        exit



