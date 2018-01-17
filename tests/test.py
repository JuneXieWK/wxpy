# coding: utf-8

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# 搜索名称含有 "游否" 的男性深圳好友
# my_friend = bot.friends().search('游否')[0]
# my_friend.send('Hello, Helen came and ask for setuping BMW Runner site')
# my_friend.send_image('/Users/june.xie/Desktop/tumblr_n8d80y1BDV1rk9vano1_500.gif')
# my_friend.send_video('/Users/june.xie/Desktop/test.mp4')


#Register a listener for friend requiring messge
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    # User have to send message including this keyword
    if 'wxpy' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('Hello World!')
        # 或 new_friend = msg.card.accept()
        # Send Video right after accepting
        new_friend.send_video('test.mp4')

#Register a listener for message with Friend
@bot.register(msg_types=TEXT)
def print_messages(msg):
    # User have to send message including this keyword
    if 'wxpy' in msg.text.lower():
        msg.sender.send_video('test.mp4')
    else:
        print(msg)
        
embed()