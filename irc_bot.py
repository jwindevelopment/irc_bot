from irc_class import *
import os
import random

## IRC Config
server = "chat.freenode.net" # Provide a valid server IP/Hostname
port = 6667
channel = "#adventureclub"
botnick = "IdiotBot"
botnickpass = ""
botpass = ""
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and channel in text and "help!" in text:
        irc.send(channel, bytes("Ask VNHY, he knows everything").encode("UTF-8"))