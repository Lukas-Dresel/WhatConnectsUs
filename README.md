# InBetweenUs
A `pyconstruct`-based python parser for the network protocol of the game `Among Us` (http://www.innersloth.com/gameAmongUs.php).

This is an implementation of the protocol based on my reverse engineering of the game, with some help from the great wiki at https://wiki.weewoo.net/wiki/Main_Page, the cool [Impostor](https://github.com/Impostor/Impostor/) project and the folks in the `Impostor` discord.
Even though `pyconstruct` should allow for packet creation as well, this is only tested for parsing for now. Furthermore, this is still Work-In-Progress and
I'm sure there's plenty of packets that are not handled correctly yet. 

Lastly, parts of the protocol of `Among Us` require a client that keeps track of game state, mainly the serialization/deserialization of `Components` identified by `NetIds`. Their contents are parsed as pure byte strings in the protocol, a game engine built on top will be responsible for deserializing them based on the current state of the game in the future once I get around to implementing that. 

