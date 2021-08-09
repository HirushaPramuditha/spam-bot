import pyautogui
import time


countdown = [5, 4, 3, 2, 1]


class ReadFile:
    def __init__(self, file):
        self.file = file

    def spam(self):
        f = open(self.file, "r")

        print("""
╔═══╗─────────╔══╗───╔╗
║╔═╗║─────────║╔╗║──╔╝╚╗
║╚══╦══╦══╦╗╔╗║╚╝╚╦═╩╗╔╝
╚══╗║╔╗║╔╗║╚╝║║╔═╗║╔╗║║
║╚═╝║╚╝║╔╗║║║║║╚═╝║╚╝║╚╗
╚═══╣╔═╩╝╚╩╩╩╝╚═══╩══╩═╝
────║║
────╚╝
	""")

        print(
            "To stop the program, move the curser to the upper left corner of the screen.")
        print("")

        for num in countdown:
            print(f"Starting in {num}...")
            time.sleep(1)

        print("Boom!")

        for line in f:
            pyautogui.typewrite(line)
            pyautogui.press("enter")


def spam(msg, count):

    print("""
╔═══╗─────────╔══╗───╔╗
║╔═╗║─────────║╔╗║──╔╝╚╗
║╚══╦══╦══╦╗╔╗║╚╝╚╦═╩╗╔╝
╚══╗║╔╗║╔╗║╚╝║║╔═╗║╔╗║║
║╚═╝║╚╝║╔╗║║║║║╚═╝║╚╝║╚╗
╚═══╣╔═╩╝╚╩╩╩╝╚═══╩══╩═╝
────║║
────╚╝
""")

    print("To stop the program, move the curser to the upper left corner of the screen.")
    print("")

    for num in countdown:
        print(f"Starting in {num}...")
        time.sleep(1)

    print("Boom!")

    for _ in range(int(count)):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
