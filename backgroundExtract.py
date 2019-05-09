import cv2
import numpy as np
import argparse
from matplotlib import pyplot

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="path of video file")
    ap.add_argument("-o", "--output", required=False, help="Name of output file",default="output")
    args = vars(ap.parse_args())
    cap = cv2.VideoCapture(args["video"])
    ret, frame = cap.read()
    AllFrames = np.zeros(frame.shape, dtype=int)
    frameNUmber = 1
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        AllFrames = (AllFrames*(frameNUmber-1)+frame)/frameNUmber
        AllFrames.astype(int)
        frameNUmber += 1
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # it closes program
            break
        if key == ord('c'):  # reinitialize process
            AllFrames = np.zeros(frame.shape, dtype=int)
            frameNUmber = 1
        if key == ord("s"):  # it saves and shows image
            cv2.imwrite(args["output"] + ".jpg", AllFrames)
            cv2.imshow("Result", cv2.imread(args["output"] + ".jpg"))

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
