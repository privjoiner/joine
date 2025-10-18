import asyncio
import threading
import time

from discord import listener
from src.roblox import roblox_main


# https://github.com/notasnek/roblox-autojoiner
# буду рад звезде на репозитории / please STAR my repo


if __name__ == "__main__":
    print("volt joiner")
    print("made by rex")
    print("invite people to discord")

    
    print("You can also donate to me on Discord. Thank you!")
    print()

    print("beta")
    print("starting")
    print()

    time.sleep(2)

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())



