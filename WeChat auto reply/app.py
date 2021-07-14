import itchat
from itchat.content import *
import re
import time

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    friend = itchat.search_friends(userName=msg['FromUserName'])
    if msg['Type'] == 'Text':
        if re.search(r"换头像", msg['Content']):
            itchat.send('我在学分认证')
    print("于【%s】收到好友【%s（昵称：%s）】发来的【%s】: 【%s】" % (
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), friend['NickName'], friend['RemarkName'], msg['Type'],
    msg['Content']))
    print("于【%s】回复：%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '我在学分认证' + '\n'))


itchat.auto_login(True)
itchat.run()