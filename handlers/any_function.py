from pprint import pprint
from aiogram import types, Dispatcher
import hashlib
from youtube_search import YoutubeSearch as YT

def finder(text):
    return YT(text, max_results=15).to_dict()

async def inline_google_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://www.google.com/search?q={text}"
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title="Wiki: ",
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=f"Держи смотри\n\n https://www.google.com/search?q{text}"
        )
    )]
    await query.answer(articles, cache_time=60)

def register_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_google_handler)