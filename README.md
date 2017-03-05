# embedbot
A selfbot for Discord.
You need discord.py to run this.
https://github.com/Rapptz/discord.py

Ask any questions here: discord.gg/KFYAUyw

__Features__

Custom embeds!

![Example of embeds](https://files.catbox.moe/6d1npp.gif)

Text triggers!

![Example of text triggers](https://files.catbox.moe/vnviqz.gif)

__Usage__

Open up config.json with any text editor.

Change the email and password to... your email and password.

Change the invoker if you like.

If you have more than one account, the bot supports config arguments.

If your config is named "Account1.json", run the file in your shell, with the argument "Account1.json".

Example: embedbot.py Account1.json

(This also help a lot with testing.)

(Hey, sometimes I'm lazy.)

If you like, you can use a token by replacing bot.run(email, password, bot=False) with bot.run("your token", bot=False).

Config layout:

{
           "token": "None",
           "email": "example@example.com",
           "password": "abc123",
           "invoker": "me!",
           "textargs": "True",
           "advancedmode": "False",
           "autoremoveinvokermessage": "False",
           "silentmode": "False",
           "loadmode": "0"
}

token: If you don't want to use your email and password, or if you use 2 factor identification (2fa or mfa), you may insert your token here.
email: If you're not using your token, it defaults to this, and your pass.
password: If you're not using your token, it defaults to this, and your email.
invoker: Can be anything, sadly. Default is \*.
textargs: True if you want stuff like {shrug} to be replaced.
advancedmode: Enabled commands like eval.
autoremoveinvokermessage: I don't really know, ask HYP3R.
silentmode: I don't know this, either.
loadmode: 0 for dots during loading, 1 for a spinning line.
