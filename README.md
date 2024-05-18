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

![Example of planetinfo](https://github.com/Windfave/divedispatcher/assets/39003171/f2ea5a8f-832c-4a6e-b459-264c0ff03c92)

- Bot shows information such as: Name, Faction that resides on such planet, amount of players fighting there, Health of the planet and the percentage of our progress on said planet and information about the planet.
- Bot shows that for all planets that a player can play on currently
- The embed has three variants: Green (if we are above ~55% in progress), Grey/Neutral (if we are inbetween ~45% and ~55%) and Red (if we are below ~45%). This way we can immediately see which planets need liberation.
- Bot shows 10 embeds for News and contains the NewsID and the content of the message.

![Example of news](https://github.com/Windfave/divedispatcher/assets/39003171/70d56381-3089-43fa-a9a8-88c0b0eaeb0f)


