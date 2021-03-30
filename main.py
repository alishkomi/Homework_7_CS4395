# Other example implementations: https://chatterbot.readthedocs.io/en/stable/examples.html

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(name='Project1',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.BestMatch'
              ],
              database_uri='sqlite:///database.db')

trainer = ListTrainer(bot)

trainer.train([
    'Hi there!',
    'Hello!',
    'How is it going?',
    'I am happy to be here.',
    'I\'m fine, thanks.',
    'Glad to hear that.',
    'Sorry to hear that. Sometimes, taking a quiet moment can help.',
    'What is your name?',
    'You are welcome.',
    'Thank you.'
])

print('Hi, my name is Project1, I am a chatbot. Ask me anything.')
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

