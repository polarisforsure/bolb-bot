

# If not, you can modify it according to your needs following the steps below:

## Pre-requisites:
* Have  2.7>Python Version<3.7.X installed (you don't need it if you aren't planning to run it on your PC though) 
* Have Discord.py installed, see [Discord.py](https://github.com/Rapptz/discord.py) for that.
## Step-By-Step:
* Go to [Apex API](https://apex.tracker.gg/site-api) and request your API Key.
* Create your Discord App on [Discord Developers](https://discordapp.com/login?redirect_to=%2Fdevelopers%2Fapplications%2F) (There are many youtube videos teaching that) and get your discord token.
* Once you have your 2 needed keys, replace them on the specified place at the code.
* Once my bot only accepts commands that are sent in the right channel, you'll have to replace the channel name placeholder with your desired channel's name in every function.
* That's it.

## Running on Heroku (Optional)
In case you want to host your bot 24/7 on Heroku, i have provided the needed files altogether (main.py, requirements.txt, Procfile), all you need to do is:
* Upload your project to your github
* Go on Heroku, create your app, then go on Deploy and sync it with the right repository on github
* Go on Setting and add a buildpack (heroku/python)
* Go back on Deploy and deploy the branch.
* That's it

## Functions:
* !set_level PLATFORM NICKNAME: Searchs for this Origin nickname, check it's level on apex, and autorole the message author with the related role.
* >check_level PLATFORM NICKNAME: Searchs for this Origin nickname, check it's level on apex tells the level but doens't autorole
* >check_kills PLATFORM NICKNAME: Searchs for this Origin nickname, check it's number of kills and tells it.
* >help: Help function, unfortunately i couldn't manage to override the help function, so i made another with different name.



## Support:
* Go to [Octavia Media](https://octaviamedia.se) to request support.
