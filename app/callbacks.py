from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup

from app.utils import build_open_comments_button, create_post
from . import dispatcher


def start(update, context):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[["I did that"]],
        resize_keyboard=True,
        one_time_keyboard=False,
    )

    update.message.reply_text(
        "Welcome to my awesome bot! "
        "Add this bot to your channel and grant access "
        "to edit posts in channel",
        reply_markup=reply_markup,
    )


def after_promotion(update, context):
    update.message.reply_text("OK, now forward post to me from your channel")


def forwarded_post(update, context):
    forwarded_message = update.effective_message
    chat = forwarded_message.forward_from_chat
    me = dispatcher.bot.get_me()
    member = chat.get_member(me.id)

    if not (member and member.can_edit_messages):
        update.message.reply_text(
            'Bot does not have permission to edit messages in channel. '
            'Grant access and forward message again'
        )
        return

    post = create_post(forwarded_message)
    print(forwarded_message)
    dispatcher.bot.edit_message_reply_markup(
        chat_id=chat.id,
        message_id=forwarded_message.forward_from_message_id,
        reply_markup=InlineKeyboardMarkup([[build_open_comments_button(post)]]),
    )


def on_error(update, context):
    print('ERROR')
    print(context.error)



