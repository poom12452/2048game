from src.controller import controller
import _thread


def start_controller():
    mycontroller = controller(4)
    print("Thread Created")

mythread = _thread.start_new_thread(start_controller, ())

while(1):
    pass

