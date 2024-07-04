#main.py
import sys
import socket
import datetime

userInput:"str";

class Ccolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    WARNING = "\033[93m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class command:
    def __init__(self) -> None:
        pass;

def main(argc:int,argv:list):
    while (True):
        rawTime=datetime.datetime.now();
        time=rawTime.strftime("%H:%M:%S")
        input(f"{Ccolors.OKBLUE}[{time}]|[{socket.gethostname()}]>>{Ccolors.ENDC}");

if (__name__=="__main__") : main(len(sys.argv[1:]),sys.argv[1:]);