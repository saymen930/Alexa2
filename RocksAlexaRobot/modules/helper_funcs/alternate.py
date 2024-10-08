# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit



from telegram.error import BadRequest
from functools import wraps
from telegram import ChatAction


def send_message(message, text, *args, **kwargs):
    try:
        return message.reply_text(text, *args, **kwargs)
    except BadRequest as err:
        if str(err) == "Cevap mesajı bulunamadı":
            return message.reply_text(text, quote=False, *args, **kwargs)


def typing_action(func):
    """Fonksiyon komutunu işlerken yazma eylemi gönderir."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        return func(update, context, *args, **kwargs)

    return command_func


def send_action(action):
    """Fonksiyon komutunu işlerken action gönderir."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(
                chat_id=update.effective_chat.id, action=action
            )
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo
