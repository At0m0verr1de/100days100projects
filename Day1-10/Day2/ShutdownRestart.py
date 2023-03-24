import os
import platform


def shutdown():
    if platform.system() == "Windows":
        os.system("shutdown -s")
    else:
        os.system("shutdown -h now")


def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    else:
        os.system("reboot now")


command = input("Enter command (r for restart, s for shutdown) : ")

if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Invalid command")
