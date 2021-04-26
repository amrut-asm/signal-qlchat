## Needs signal-cli (https://github.com/AsamK/signal-cli)
# signal-qlchat
Minqlx plugins to chat with people in your Signal group from in-game (Quake Live) and vice-versa

# Modifications required
* Make sure you put in your signal bot's phone number in the script. Also, be sure to change the group name to your Signal group.

* Writing a message from in-game to a Signal group requires the groupID (a byte array) for the group. 

* You can get the groupID for your group by printing out the groupID when you receive a message from Signal (in signal_read.py)

# Usage
* For sending a message from in-game to a Signal group : Type **!s** followed by your message in the game chat.

* For sending a message from a Signal group to in-game : Type **.s** followed by your message in the Signal chat.

# Warning
* Sometimes it just so happens that Signal does not know your name. In that case you could use **.sa** which does not use your name while writing your message from a Signal group to the in-game chat.
