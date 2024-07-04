#main.py
import sys
import socket
import datetime



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
    def __init__(self,command_name:"str"="None") -> None:
        self.cmd:"str"=command_name;
        self.active:"bool"=False;
        self.args:"list";
        self.argc:"int";
        commands:"list";
        if(command_name not in commands):
            commands+=str(command_name)
    
    def update(self,passInput:"str")->None:
        if (passInput[0:len(self.cmd)]==self.cmd):
            sys.stdout.write(f"\n{Ccolors.BOLD}{self.cmd}::{Ccolors.ENDC}")
            sys.stdout.flush();
            # #####
            if(self.cmd=="help"):
                sys.stdout.write("\ncommands:");
                sys.stdout.write(f"{Ccolors.OKCYAN}help- shows all commands and if they are running{Ccolors.ENDC} {Ccolors.BOLD}{Ccolors.WARNING}Enabled:{help.active}{Ccolors.ENDC}\n");
                sys.stdout.write(f"{Ccolors.OKCYAN}getTargets- show targets{Ccolors.ENDC} {Ccolors.BOLD}{Ccolors.WARNING}Enabled:{getTargets.active}{Ccolors.ENDC}\n");
            
            elif(self.cmd=="exit"):
                sys.exit();
            
            elif(self.cmd=="clear"):
                sys._clear_type_cache();
            # #####
            sys.stdout.write("\n")
            sys.stdout.flush();
        else:
            sys.stderr.write(f"{Ccolors.ENDC}{Ccolors.FAIL}{Ccolors.BOLD}Warning! {passInput} is not a valid command{Ccolors.ENDC}\n");


userInput:"str";

help:"command"=command(command_name="help");
exit:"command"=command(command_name="exit");
clear:"command"=command(command_name="clear");
getTargets:"command"=command(command_name="getTargets");

def main(argc:int,argv:list):
    while (True):
        rawTime=datetime.datetime.now();
        time=rawTime.strftime("%H:%M:%S")
        userInput=str(input(f"{Ccolors.OKBLUE}[{time}]|[{socket.gethostname()}]>>{Ccolors.ENDC}"));

        help.update(str(userInput));
        exit.update(str(userInput));
        clear.update(str(userInput));

if (__name__=="__main__") : main(len(sys.argv[1:]),sys.argv[1:]);