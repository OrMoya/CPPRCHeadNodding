import cv2
import os

#'D:/School/CPPRC/c_bot/Test Video.mp4'
cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('D:/School/CPPRC/c_bot/OutputVideo.avi', fourcc, 30.0, (640, 480),
                      isColor=False)

#folder# and path directory
folder = 3
path = ("D:/School/CPPRC/c_bot/HeadNod_%d/" % folder)
os.makedirs(path)

# Used in saving frames
n = 10
count = 0

#dimension for frame
dim = (640, 480)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to greyscale and resize the frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

    # if statement that saves every nth frame
    if (count % n == 0):
        cv2.imwrite("D:/School/CPPRC/c_bot/HeadNod_%d" % folder + "/frame%d.jpg" % count, res, [int(cv2.IMWRITE_JPEG_QUALITY), 15])
    count += 1

    # Save video
    out.write(gray)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()