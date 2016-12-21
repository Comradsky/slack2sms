# slack2sms
Slack to sms and back

1 To trigger the slack bot to send something contain one of these in the message
        @twilio, @twiliobot, @textbot,  @sms, @smsbot, @text        
        
2 To send to a number it must fist be varified on twilio since its a free account
        start the phone number with #
With this functionality you could send a slack to any number but since my Twilio account is a free version in order to send to a specific number it must first be added through the twilio website under the 'Verified Caller IDs' section
        
        
Example:

(slack)skylerhill [4:19 PM]  
@sms #5124122438 this could work * 8

received sms: 'Sent from your Twilio trial account - skylerhill in general says:   this could work * 8’
    
    
The program cuts out the @insert_bot_name and #1234567 to make the message shorter
