#!/usr/bin/env python3

# Skyler Hill   Slack2SMS

''' I am groot
A slack to SMS bot that can send a slack message to any number and back via twilio, slack API, flask, and ngrok
'''

import os
import sys

from argparse import ArgumentParser
from slackclient import SlackClient
from twilio import twiml
from twilio.rest import TwilioRestClient
from flask import Flask, request, Response

receiving_channel = '#general'



# initialize flask app to route webhooks
app = Flask(__name__)

'''
    Fill all of the empty quotes with the slack and twilio tokens etc.
'''
# setting up Slack
SLACK_TOKEN = 'enter_slack_token'
SLACK_WEBHOOK_SECRET = 'enter_slack_webhook'   # our outgoing slack webhook
slack_client = SlackClient(SLACK_TOKEN)


# setting up Twilio
TWILIO_ACCOUNT_SID = 'enter_twilio_sid'
TWILIO_AUTH_TOKEN = 'enter_twilio_token'
twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# the number twilio sends form, set up through twilio.com
TWILIO_NUMBER = 'enter_twilio_num'      # ex +11231234567
USER_NUMBER = 'enter_your_phone'

# todo could change this to environment variables like:
'''
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
USER_NUMBER = os.environ.get('USER_NUMBER', None)

slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET', None)
'''

# twilio post function
@app.route('/twilio', methods=['POST'])
def twilio_post():
    response = twiml.Response()

    message = request.form['From'] + ': ' + request.form['Body']    # text for the message and show who sent it
    # todo: make 'channel' a constant or setable as menu
    slack_client.api_call('chat.postMessage', channel=receiving_channel,   # create the message for sending
                            text=message, username='sms_bot',
                            icon_emoji=':robot_face:')
    return Response(response.toxml(), mimetype='text/xml'), 300


@app.route('/slack', methods=['POST'])
def slack_post():
    if request.form['token'] == SLACK_WEBHOOK_SECRET:
        username = request.form['user_name']
        in_channel = request.form['channel_name']

        text = request.form['text']
        # get @ and # strings, for bot and to phone number, hacky but quick
        # todo: use regex instead, because mo' powa
        my_number = substring_after(text, '#')
        my_number = my_number[0: my_number.find(' ')]
        at = substring_after(text, '@')
        at = at[0: at.find(' ')]
        text = text.replace('#'+my_number, '')  # cut out to phone number, not needed
        text = text.replace('@'+at, '')  # cut out to phone number, not needed

        # if you just want to send it to yourself everytime for testing and not have to type #1234567
        # my_number = USER_NUMBER

        # writing the message and sending it
        response_message = username + ' in ' + in_channel + ' says: ' + text
        twilio_client.messages.create(to=my_number, from_=TWILIO_NUMBER,
                                        body=response_message)
        # todo add capability to send to multiple numbers at once
    return Response(), 200


# gets substrings for a delimiter
def substring_after(s, delim):
    return s.partition(delim)[2]


@app.route('/', methods=['GET'])
def test():
    return Response('Works!')


# checking Flask
'''app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
'''


# argparse command line options
def main(argv):
    from argparse import ArgumentParser

    # set up parser
    parser = ArgumentParser(description='slack2sms script')
    parser.add_argument('--channel', default='general', help='Channel to Receive Sms, ex. general')

    args = parser.parse_args(argv)
    global receiving_channel
    receiving_channel = '#' + args.channel

    app.run(debug=True)
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
