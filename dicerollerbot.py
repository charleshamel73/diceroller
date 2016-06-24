import time
from slackclient import SlackClient
import re

from src.main.Parser import Parser

BOT_TOKEN = "<insert_token>"

def main():
    sc = SlackClient(BOT_TOKEN)
    if sc.rtm_connect():
        # print sc.server.channels
        bot_id = sc.server.users.find("qds").id
        while True:
            data = sc.rtm_read()
            if data != []:
                print data[0]
                if "type" in data[0] and data[0]["type"] == "message" and "subtype" not in data[0]:
                    if data[0]["user"] != bot_id:
                        text =  data[0]["text"]
                        channel_id = data[0]["channel"]
                        channel = sc.server.channels.find(channel_id)
                        if "roll " in text:
                            try:
                                test = text.replace("roll ", "")
                                result = Parser().parse(test)
                                sc.rtm_send_message(channel.name,"Rolling a '%s' and got a result of %s"%(test,result.sum))
                                sc.rtm_send_message(channel.name,result.message)
                                #TODO: Support message level saving such that a user could track history of roll
                            except Exception as e:
                                sc.rtm_send_message(channel.name,"ROLL FAILED: %s"%e.message)

            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"

if __name__ == '__main__':
    main()