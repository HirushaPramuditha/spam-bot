import pyautogui
import time


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

        for i in range(1, 6):
            print(f"Starting in {i}...")
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

    for i in range(1, 6):
        print(f"Starting in {i}...")
        time.sleep(1)

    print("Boom!")

    for _ in range(int(count)):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
