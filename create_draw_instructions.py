import cv2
import os
import pickle


def check_differences(current_frame, next_frame):
    diferent_pixels = []
    for row in range(0, 360):
        for column in range(0, 640):
            if current_frame[row][column] != next_frame[row][column]:
                diferent_pixels.append([row, column, next_frame[row][column]])
    return diferent_pixels


def generate_draw_instructions(bitmaps):
    if 'data' in os.listdir():
        os.remove('data')

    current_frame = cv2.imread('./bitmaps/' + bitmaps[0], -1).tolist()
    with open('data', 'ab') as f:
        pixels = []
        for row in range(0, 360):
                for column in range(0, 640):
                    pixels.append([row, column, current_frame[row][column]])
        pixels.append('F')
        pickle.dump(pixels, f)

    if len(bitmaps) > 1:
        for i in range(1, len(bitmaps)):
            next_frame = cv2.imread('./bitmaps/' + bitmaps[i], -1).tolist()
            different_pixels = check_differences(current_frame, next_frame)
            with open('data', 'ab') as f:
                different_pixels.append('F')
                pickle.dump(different_pixels, f)
            current_frame = next_frame


if __name__ == '__main__':
    bitmaps = os.listdir('./bitmaps')
    sorted_maps = sorted(bitmaps, key=lambda x: int(x[0:3].strip('.b')))
    generate_draw_instructions(sorted_maps)