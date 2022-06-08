# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:48:52 2021

@author: DELL
"""

import cv2 
import os
import speech_recognition as sr
import numpy as np
# img
import datetime
path = "img"
#video
path_video = "video"
def voice():
    y=True
    while y == True:
             
        print("Hãy nói số thứ tự video bạn muốn mở(ví dụ: số 0)")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Adjusting noise ")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
                # read the audio data from the default microphone
            audio_data = r.record(source, duration=5)
            print("Kết quả nhận diện...")
                # convert speech to text
            try:
                query = r.recognize_google(audio_data,language="vi")
            except:
                continue 
            print(query)
            query=query.strip('số ')
            try:
                query=int(query)
                break 
            except:   
                continue
    return query

def getCam():
    cam = cv2.VideoCapture(0) 
    count = 0 
    folder = input("nhap ten folder: ")
    os.makedirs(folder, exist_ok=True)
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('p'):
            cv2.waitKey()
            ans = input("Bạn có muốn lưu hình này không?(y/n) ")
            if ans == "y":
                ts = datetime.datetime.now()
                cv2.imwrite(os.path.join(folder,ts.strftime("%Y-%m-%d_%H-%M-%S")+".jpg") ,frame) 
            else:
                continue
              
        elif cv2.waitKey(10) & 0xFF == ord('q'):
            break  
def getFileImg():
   
    myList = os.listdir(path)
            # in list images
    print("Danh sách file hình ảnh: ")
    for i in myList:
        
        print("{} : {}".format(myList.index(i),i))
    print ('''
                Chọn các chức năng
               1. Nạp bằng cách nhập số thứ tự
               2. Dùng giọng nói
              
               ''')
    chon = input("Chọn: ")
    if chon == "2":                  
        query = voice()
        img = cv2.imread("{}/{}".format(path,myList[query]))
        cv2.imshow("hinh", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
    elif chon == "1":
        nhap = int(input("Nhập số thứ tự file: "))
        img = cv2.imread("{}/{}".format(path,myList[nhap]))
        cv2.imshow("hinh", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
    return img
def getVideo():
    print('''
              Danh sách các file:
              ''')

    myList = os.listdir(path_video)
    # in list images
    print("Danh sách file hình ảnh: ")
    for i in myList:
        
        print("{} : {}".format(myList.index(i),i))
    print ('''
                Chọn các chức năng
               1. Nạp bằng cách nhập số thứ tự
               2. Dùng giọng nói
              
               ''')
    chon = input("Chọn: ") 
    
    if chon == "1":
        nhap = int(input("Nhập số thứ tự file: "))
        
        cap = cv2.VideoCapture("{}/{}".format(path_video,myList[nhap]))
        
        while cap.isOpened():
            ret, frame = cap.read()#chụp ra một khung hình: 
                                    #khung chụp được lưu vào biến frame; ret = vị trí tiếp theo của Video 
                                    #(sau khung hình vừa chụp)
            cv2.imshow('Khung Hinh', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    elif chon == "2":
        c = voice()
def gray(file):
    img_gray = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def getSize(file):
        (h, w, d) = file.shape
        print ("Kích thước hình ảnh là: ")
        print("width={}, height={}, depth={}".format(w, h, d))
        
        
        
def menu(file, lang):
    chon = True
    while chon:
        print("""
                  1. Chuyển ảnh xám
                  2. Lấy kích thước ảnh
                  3. Cắt ảnh
                  4. Xoay ảnh
                  5. Lấy giá trị màu tại vị trí
                  6. Thay đổi kích thước
                  7. Thoát
            """)
        chon = input("Chọn : ")
        if chon == "1":
           gray(file) 
        elif chon == "2":
            getSize(file)
def menuSelect():
     print("""
                        1. Nạp file hình ảnh
                        2. Chụp ảnh từ camera
                        3. Nạp video
                    
                        """)
        
def main():
    menuSelect()
    ans = input("CHon: ")    
    if ans == "1":
        img = getFileImg()
        menu(img)
    elif ans =="2":
        img = getCam()
    elif ans == "3":
        getVideo()
        
main()

