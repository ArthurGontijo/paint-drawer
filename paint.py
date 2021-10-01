import cv2
import pyautogui
import os
import pickle
from time import sleep


pyautogui.PAUSE = 0.000000000001
CANVAS_POSITION = (5, 144)


def pick_color(color):
    if color == 0:
        pyautogui.click(400, 80)
    else:
        pyautogui.click(313, 102)
    sleep(0.05)


def draw_in_paint(pickle_file):
    draw_instructions = []
    with open(pickle_file, "rb") as openfile:
        while True:
            try:
                draw_instructions.append(pickle.load(openfile))
            except EOFError:
                break
    pick_color(0)
    count = 0
    last_color = 0
    for frame in draw_instructions:
        sorted_instructions = sorted(frame, key=lambda x: int(x[2]) if len(x) > 1 else -1000, reverse=True)
        if count == 0:
            for instruction in sorted_instructions:
                if instruction == 'F':
                    print(f'Frame {count} completed')
                    screenshot = pyautogui.screenshot()
                    screenshot.save(f'./screenshots/frame{count}.png')
                elif instruction[2] == 0:
                    pyautogui.click(instruction[1] + CANVAS_POSITION[0], instruction[0] + CANVAS_POSITION[1])
        else:
            for instruction in sorted_instructions:
                if instruction == 'F':
                    print(f'Frame {count} completed')
                    screenshot = pyautogui.screenshot()
                    screenshot.save(f'./screenshots/{count}.png')
                else:
                    if instruction[2] == 0:
                        if last_color != 0:
                            pick_color(0)
                            last_color = 0
                        pyautogui.click(instruction[1] + CANVAS_POSITION[0], instruction[0] + CANVAS_POSITION[1])
                    else:
                        if last_color != 1:
                            pick_color(1)
                            last_color = 1
                        pyautogui.click(instruction[1] + CANVAS_POSITION[0], instruction[0] + CANVAS_POSITION[1])
        count += 1    

                



def main():
    input('Press Enter to start: ')
    draw_in_paint('./data')
    

if __name__ == '__main__':
    main()
