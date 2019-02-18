import praw
import time
from keep_alive import keep_alive

SECONDS_PER_MIN = 60

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent',
                     username='your_username',
                     password='your_password')

//loops through unread messages for specified sender and replies with specified response
def CheckMsg(author, reply):
    print("Checking messages...")
    inbox = reddit.inbox.unread()
    for message in inbox:
      if(message.author.name==author):
        print(message.body)
        print(">responding with: " + reply)
        message.reply(reply)
        message.mark_read()

def main():
  keep_alive()
  interval = 10 
  while True:
    //respond to a person with a message
    CheckMsg("person_to_respond_to", "message_to_respond_with")
    print("-----------------------------")
    time.sleep(SECONDS_PER_MIN * interval)

main()
