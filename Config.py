import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("889717984:AAEOFn6fDMNEY68ChA8Hx1eMpQVPCWuDSO0", None)
    DATABASE_URL = os.environ.get("postgres://nllkrhwbzjsaio:721c70c346a29d1ec14769b6a8b16db81e4e861f94e66612f1b410969a6b8f38@ec2-23-22-191-232.compute-1.amazonaws.com:5432/de7p1bsrglg5j7", None)
    APP_ID = os.environ.get(938778, 6)
    API_HASH = os.environ.get("903ac837a4987887dbdc8185ac9da008", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(855811628)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1635725479:AAF4vbfVZkFgKQOAlHMNkB4YH67JqvRU4LE"
    DATABASE_URL = "postgres://wsjgsymwdbemzd:60cb1a5ecfc628182b4c08a083c77922a18c154c695e6cdf78a5788553e8291e@ec2-3-223-72-172.compute-1.amazonaws.com:5432/d3jvlfqidj9isa"
    APP_ID = "1387167"
    API_HASH = "13de1882ed65185020dfe89235ee8ee5"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(855811628)
    SUDO_USERS.append(1060060191)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @viperadnan**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
