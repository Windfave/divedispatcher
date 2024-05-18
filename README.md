# Divedispatcher
A python-based Discord bot grabbing information about available planets in Helldivers 2 from the [Helldivers Training Manual](https://helldiverstrainingmanual.com/api) website API.

## More information

The bot uses app commands, so there is no need for a prefix.
After a command is given, the bot sends multiple messages (embeds) to given message.
In this version of the code, only the planetinfo command gets more messages instead of more embeds in one message, as discord has a limit for that (12 or so).
(I didn't bother doing that in the news command, since the API doesn't update it at all)
----------------------------------------------------------------------------------------------
The code went through multiple changes, like adding support for null information in Biome in planetinfo, or as mentioned above,
changing the way the bot replies to messages.
I find it unlikely I will add anything else to the bot right now, as the API isn't that accessible.
If the API has new stuff, like player information, or store information, I will add that.
Otherwise I will just fix stuff if it breaks.

**Python 3.12 was used.**
