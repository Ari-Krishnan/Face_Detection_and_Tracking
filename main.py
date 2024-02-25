import cv2

alg = "haarcascade_frontalface_default.xml" # Face detection Algarithm

haar_cascade = cv2.CascadeClassifier(alg)  # Loading Algarithm into the variable

cam = cv2.VideoCapture(0) #  Initializing the camera Id

while True:

    _,img = cam.read() # Reading frame from Camera

    grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Converting Color image to gray scale image

    face = haar_cascade.detectMultiScale(grayscale, 1.3, 4)
    # Getting coordinates  using haarcascade frontalface Algorithm

    for (x, y, w, h) in face: # Getting parameter for rectangle 
        cv2.rectangle(img, (x, y), (x+w, y+h), (155, 0, 255), 3)
        # Drawing the ractanlge

    cv2.imshow("Face Detaction",img)
    # Streaming video

    key = cv2.waitKey(10)  # Wait for the exit key
    if key == 27: #Press the waitkey they key value qual to 27 and break the loop
        break
    
cam.release() # Release the camera
cv2.destroyAllWindows() # Closing the windows
