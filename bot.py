bot = TeleBot(1227767014:AAGbATukzvKZg0_7eWaxE8vAPC14oXNKLAc)


@bot.message_handler(content_types=['new_chat_member'])
def new_chat_member_handler(message: Message):
    try:
        bot.restrict_chat_member(
            message.chat.id,
            message.from_user.id,
            until_date=None,
            can_send_messages=False,
            can_send_media_messages=True,
            can_send_other_messages=False,
            can_add_web_page_previews=False
        )
    except ApiException:
        bot.send_message(
            message.chat.id,
            "Please, promote me to admin."
        )
        
        
bot.polling()
$admin=123123;//Admin ID raqami
$chat_id = $message->chat->id;
$message_id = $message->message_id;
$fadmin = $message->from->id;
if($admin!=$fadmin){
    if($update->message->video || $update->message->photo){
    }else{
    Bot('deletemessage',[
    'chat_id'=>$chat_id,
    'message_id'=>$message_id
    ]);    
    }
    
}
