# Automate the Boring Stuff with Python
# Chapter 4 - Lists
# 2-June-2019

# Version 2 of the Magic 8 Ball
import random
print('Ask the Magic 8 Ball a Question..')
messages=['It is certain',
          'It is decidely so',
          'Yes definitely',
          'Reply hazy, try again',
          'Ask again later',
          'Concentrate and ask again',
          'My reply is no',
          'Outlook not so good',
          'Very doubtful']
print(messages[random.randint(0, len(messages)-1)])
