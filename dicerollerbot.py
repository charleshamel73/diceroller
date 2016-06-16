import time
from slackclient import SlackClient

BOT_TOKEN = "xoxb-51415107092-0OAMiG9zBzX7zBL6qZcOdW4k"

def main():
    sc = SlackClient(BOT_TOKEN)
    if sc.rtm_connect():
        # print sc.server.channels
        bot_id = sc.server.users.find("qds").id
        while True:
            data = sc.rtm_read()
            if data != []:
                print data[0]
                if 'text' in data[0] and 'user' != bot_id and 'reply_to' not in data[0]:
                    print data[0]["text"]
                    sc.rtm_send_message("random","YOU MESSAGED ME")
            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"

if __name__ == '__main__':
    main()