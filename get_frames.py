import cv2
import os

def get_frames():
    vidcap = cv2.VideoCapture('./video.mp4')
    success, image = vidcap.read()
    count = 0
    while success:
        scale_frame(image, count)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


def scale_frame(frame, count):
    resized = cv2.resize(frame, (640, 360))
    cv2.imwrite("./frames/%d.png" % count, resized)


def create_bitmaps(frames):
    count = 0
    for frame in frames:
        img = cv2.imread('./frames/' + frame)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
        edges = cv2.Canny(img_blur, 10, 200)
        inverted = cv2.bitwise_not(edges)

        cv2.imwrite(f'./bitmaps/{count}.bmp', inverted)
        count += 1


if __name__ == '__main__':
    get_frames()
    frames = os.listdir('./frames')
    sorted_frames = sorted(frames, key=lambda x: int(x[0:3].strip('.p')))
    create_bitmaps(sorted_frames)