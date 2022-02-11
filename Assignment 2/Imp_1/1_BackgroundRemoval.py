import numpy as np
import cv2
import time

# Open Video
cap = cv2.VideoCapture('video.mp4')
# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=20)

# Store selected frames in an array
frames = []
for fid in frameIds:
    # Go to each selected frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Calculate median across the selected frames, convert to gray
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
medianGray = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)


# Display median frame
cv2.imshow('frame', medianFrame)
#cv2.imshow('gray', medianGray)
cv2.imwrite('1_background.png',medianFrame)
cap.release()

# Replay video to extract cars
cap = cv2.VideoCapture('video.mp4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('1_cars.avi',cv2.VideoWriter_fourcc('M','J','P','G'),
                     20, (frame_width,frame_height))

# Remove the background from video
ret = True
while(ret):
    ret, frame = cap.read()

    if ret == True:
        # Grayscale difference to detect car
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frameGray, medianGray)
        th, diffFrame = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)
        # Extract the cars from mask
        result = cv2.bitwise_and(frame, frame, mask=diffFrame)
        out.write(result)
    else:
        break

cap.release()
out.release()
