from instabot import Bot

my_Bot = Bot()

# login
my_Bot.login(username="busani_radebe", password="XLMXRPZEC1$")

# unfollow the non-followers
my_Bot.unfollow_non_followers()
# send message to user
my_Bot.send_message('Hello Busani Radebe how are you today', 'busani_radebe')
