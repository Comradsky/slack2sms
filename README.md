# slack2sms
Slack to sms and back

Make sure the proper libraries are installed 
        $ pip install slackclient twilio flask
   
Webhook:   
Run ngrok to create you're webhook and copy the forwarding https: ex. https://4ee379f8.ngrok.io
   
Setup Slack   
Generate slack tokens for a team you have admin priveleges on and save it to put into the slack2sms.py later (SLACK_TOKEN)
Go to outgoing webhooks and under URLs put your ngrok https and add /slack to the end
ex. https://4ee379f8.ngrok.io/slack
And then save the webhook token on the same page (SLACK_WEBHOOK_SECRET)
Also enter your trigger words, ex. @twilio, @sms, @text, @twiliobot, @smsbot, @textbot

Configure Twilio
Set up your twilio phone number
Get your account sid (TWILIO_ACCOUNT_SID) and your twilio token (TWILIO_AUTH_TOKEN)
Also go to the web hook, select https webhook and enter in your ngrok + /twilio ex. https://4ee379f8.ngrok.io/twilio


Using the app:
Enter in the required keys near the top of the slack2sms.py, also enter youre twilio number and your user number.

To send to a number it must fist be varified on twilio since if its a free account, but otherwise you can send a message to any number if it's a payed account or the number is already registered
        
In slack: start with @sms and then anywhere in the message include the phone number you want to send to starting with a #
        
        
Example:

(slack)skylerhill [4:19 PM]  
@sms #5124122438 this could work

received sms: 'Sent from your Twilio trial account - skylerhill in general says:   this could work’    
    
The program cuts out the @insert_bot_name and #1234567 to make the message shorter

To respond to the bot on the phone number just text back.
