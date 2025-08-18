import cv2
import numpy as np

# def create_blank_pic():
#     height,width=10,10
#     arr=np.zeros((height,width,3),dtype=np.uint8)*255
#     arr=cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)
#     arr[:,:,:]=[100,120,140]
#     cv2.imwrite('original.png',arr,params=None)

def LSB_encode():
    img=cv2.imread('original.png')
    text_binary=""
    text_binary_ptr=0
    for i in text:
        text_binary+=format(ord(i),'08b')
    text_binary+="00000000" #end_of_msg
    img2=img.copy()
    flag=0
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i][j][2]=int(f'{img[i][j][2]:08b}'[1:][2:-1]+text_binary[text_binary_ptr],2)
            if(text_binary_ptr+1<len(text_binary)):
                text_binary_ptr+=1
            else:
                flag=1
                break
        if(flag==1):
            break

    cv2.imwrite("LSB/LSB_encode.png",img2,params=None)


def LSB_decode():
    img=cv2.imread('LSB/LSB_encode.png')
    text_binary=""
    text=""
    for i in range(len(img)):
        for j in range(len(img[0])):
            text_binary+=f'{img[i][j][2]:08b}'[1:][-1]

    for i in range(0,len(text_binary),8):
        if(int(text_binary[i:i+8],2)!=0):
            text+=chr(int(text_binary[i:i+8],2))
        else:
            break
    open('LSB/output.txt','w').write(text)

def LSB_RGB_encode():
    img=cv2.imread('original.png')
    text_binary=""
    text_binary_ptr=0
    for i in text:
        text_binary+=format(ord(i),'08b')
    text_binary+="00000000" #end_of_msg
    img2=img.copy()
    flag=0
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            for k in range(3):
                img2[i][j][k]=int(f'{img[i][j][k]:08b}'[2:-1]+text_binary[text_binary_ptr],2)
                if(text_binary_ptr+1<len(text_binary)):
                    text_binary_ptr+=1
                else:
                    flag=1
                    break
            if(flag==1):
                break
        if(flag==1):
            break
        
    cv2.imwrite("LSB/LSB_encode_RGB.png",img2,params=None)


def LSB_RGB_decode():
    img=cv2.imread('LSB/LSB_encode_RGB.png')
    text_binary=""
    text=""
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                text_binary+=f'{img[i][j][k]:08b}'[1:][-1]

    for i in range(0,len(text_binary),8):
        if((int(text_binary[i:i+8],2)!=0)):
            text+=chr(int(text_binary[i:i+8],2))
        else:
            break

    open('LSB/output_RGB.txt','w').write(text)


def MSB_encode():
    img=cv2.imread('original.png')
    text_binary=""
    text_binary_ptr=0
    for i in text:
        text_binary+=format(ord(i),'08b')
    text_binary+="00000000" #end_of_msg
    img2=img.copy()
    flag=0
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i][j][0]=int(text_binary[text_binary_ptr]+f'{img[i][j][0]:08b}'[1:],2)
            if(text_binary_ptr+1<len(text_binary)):
                text_binary_ptr+=1
            else:
                flag=1
                break
        if(flag==1):
            break

    cv2.imwrite("MSB/MSB_encode.png",img2,params=None)


def MSB_decode():
    img=cv2.imread('MSB/MSB_encode.png')
    text_binary=""
    text=""
    for i in range(len(img)):
        for j in range(len(img[0])):
            text_binary+=f'{img[i][j][0]:08b}'[0]

    for i in range(0,len(text_binary),8):
        if(int(text_binary[i:i+8],2)!=0):
            text+=chr(int(text_binary[i:i+8],2))
        else:
            break

    open('MSB/output.txt','w').write(text)

def MSB_RGB_encode():
    img=cv2.imread('original.png')
    text_binary=""
    text_binary_ptr=0
    for i in text:
        text_binary+=format(ord(i),'08b')
    text_binary+="00000000" #end_of_msg
    img2=img.copy()
    flag=0
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            for k in range(3):
                img2[i][j][k]=int(text_binary[text_binary_ptr]+f'{img[i][j][k]:08b}'[1:],2)
                if(text_binary_ptr+1<len(text_binary)):
                    text_binary_ptr+=1
                else:
                    flag=1
                    break
            if(flag==1):
                break
        if(flag==1):
            break
        
    cv2.imwrite("MSB/MSB_RGB_encode.png",img2,params=None)


def MSB_RGB_decode():
    img=cv2.imread('MSB/MSB_RGB_encode.png')
    text_binary=""
    text=""
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                text_binary+=f'{img[i][j][k]:08b}'[0]

    for i in range(0,len(text_binary),8):
        if(int(text_binary[i:i+8],2)!=0):
            text+=chr(int(text_binary[i:i+8],2))
        else:
            break

    open('MSB/output_RGB.txt','w').write(text)

def encode():
    LSB_encode()
    print('LSB_encode Done')
    LSB_RGB_encode()
    print('LSB_RGB_encode Done')
    MSB_encode()
    print('MSB_encode Done')
    MSB_RGB_encode()
    print('MSB_RGB_encode Done')
    print('---------------------------')

def decode():
    LSB_decode()
    print('LSB_decode Done')
    LSB_RGB_decode()
    print('LSB_RGB_decode Done')
    MSB_decode()
    print('MSB_decode Done')
    MSB_RGB_decode()
    print('MSB_RGB_decode Done')


text=open('secret.txt','r').read()
encode()
decode()