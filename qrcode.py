import cv2
import numpy as np
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
import pyautogui

"""
    author : https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
    url : https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
"""

# screenshot convert to cv2 image
def screenshot():
        img = pyautogui.screenshot()
        open_cv_image = np.array(img) 
        return open_cv_image[:, :, ::-1].copy()

# find the barcodes in the image and decode each of the barcodes
def detect_barcode(image):
        rsult = []
        barcodes = pyzbar.decode(image, symbols=[ZBarSymbol.QRCODE])
        # loop over the detected barcodes
        for barcode in barcodes:
                # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # the barcode data is a bytes object so if we want to draw it on
                # our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                # barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                # text = "{} ({})".format(barcodeData, barcodeType)
                # cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                #        0.5, (0, 0, 255), 2)
                # print the barcode type and data to the terminal
                # print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
                rsult.append(barcodeData);
        return rsult

if __name__ == "__main__":
        image = screenshot()
        for url in detect_barcode(image):
                print("[INFO] QR CODE URL : {}".format(url))
