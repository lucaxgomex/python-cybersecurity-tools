from pynput.mouse import Listener

def write_to_file(x, y):
    print('Position of current mouse: {0}'.format((x, y)))

with Listener(on_move=write_to_file) as listener:
    listener.join()