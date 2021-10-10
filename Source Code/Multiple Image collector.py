#|================================================================================================================================================================================
#                                                                                           MULTIPLE PICTURE TAKER
#|================================================================================================================================================================================
# Author : Hardik Shah
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This python program will click multiple photos from the compuers webcam.
# To start clicking pictures press "SPACEBAR". You can also use the "SPACEBAR" to pause the process. Press "ESC" key to exit.
# This program can be executed directly or through command line.
# commade to execute the program-  python "Multiple Image collector".py "destination folder name" "NO. of pictures you want to take"
# command example- python "Multiple Image collector".py Myiamges 100
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#|================================================================================================================================================================================


# IMPORTS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import time
import cv2
from tkinter import filedialog
from tkinter import *
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Function to start camera and take pictures----->
def cam():
    start = False
    count = 0
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        if count == num_samples:                        #Stop if number of images clicked reach disired number
            break
        if start:
            save_path = os.path.join(save_images_path, '{}.png'.format(count + 1))
            cv2.imwrite(save_path, frame)               #saving clicked images to destination
            count += 1                                           #counting number of images clicked
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Collecting {}".format(count),(5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)   # Adding text to video vindow
        cv2.imshow("Collecting images", frame)

        k = cv2.waitKey(33)
        if k == 32:                     #Check to see if spacebar is pressed
            start = not start         #pause if spacebar is pressed

        if k == 27:                     #Check to see if "ESC" is pressed
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print()
    print('IMAGES SAVED TO : ', save_images_path)
    time.sleep(5)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Function For Direct Execution-------------------->

def direct_exc():
    #For presentation
    print('-'*20)
    print(' '*10,'Multiple Image collector')
    print('-'*20)
    print()
    #------------------
    
    print('SELECT DISTINATION FOLDER')
    time.sleep(1)
    Tk().withdraw()
    destination_path=filedialog.askdirectory()                     # Using tinker to open a GUI based path selector
    global save_images_path                                              # Declaring 'Image path' as a global variable
    save_images_path=os.path.join(destination_path,'Images')
    try:
        def ask():
            global num_samples                                              # Declaring 'Number of pictures to take' as a global variable
            num_samples= int(input('Enter the number of Pictures you want to click : '))  # Asking user for number of images to click
        ask()
    except:
        print('!! INVALID INPUT !!')
        print()
        print(' INPUT SHOULD BE A NUMBER ')
        print()
        ask()
    try:
        os.mkdir(save_images_path)   #Creating folder to save images
    except FileExistsError:
        pass
    cam()   # Starting WebCam To collect pictures.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Global code---------------------------------------->

if len(sys.argv)==1:                       #CHECK TO SEE IF CODE IS NOT EXECUTED THROUGH COMMAND LINE
    direct_exc()                           #CODE PROCEDES TO DIRECT EXECUTION
else:
    try:
        # GETTING VALUES IF CODE EXECUTED FROM COMMAND LINE
        label_name = sys.argv[1]
        num_samples = int(sys.argv[2])
        save_images_path= label_name
        
        try:
            os.mkdir(label_name)   #Creating folder to save images
        except FileExistsError:
            pass
        
        cam()                                        # Starting WebCam To collect pictures.
        
    except:
        print(sys.argv)
        print("Arguments missing.")
        print()
        print('-'*50)
        print(''' commade to execute the program-  python "Multiple Image collector".py "destination folder name" "NO. of pictures you want to take"
     command example- python "Multiple Image collector".py Myiamges 100''')
        exit()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#|================================================================================================================================================================================
#                                                                                               END OF CODE
#|================================================================================================================================================================================
