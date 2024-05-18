# Divedispatcher
A python-based Discord bot grabbing information about available planets in Helldivers 2 from the [Helldivers Training Manual](https://helldiverstrainingmanual.com/api) website API.

## More information

The bot uses app commands, so there is no need for a prefix.
After a command is given, the bot sends multiple messages (embeds) to given message.
In this version of the code, only the planetinfo command gets more messages instead of more embeds in one message, as discord has a limit for that (12 or so).
(I didn't bother doing that in the news command, since the API doesn't update it at all)
