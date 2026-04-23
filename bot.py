# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"

# # /start komandasi
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Salom! Men gaplashadigan botman 🤖")

# # xabarlarni qayta ishlash
# async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     text = update.message.text.lower()

#     if "salom" in text:
#         javob = "Salom! 😊"
#     elif "qalesan" in text or "qalay" in text:
#         javob = "Yaxshiman 😎 senchi?"
#     elif "isming nima" in text:
#         javob = "Men Husniddinning botiman 🤖"
#     elif "rahmat" in text or "raxmat" in text:
#         javob = "Arzimaydi 😊"
#     elif "bye" in text:
#         javob = "Xayr! 👋"
#     else:
#         javob = "Tushunmadim 🤔 boshqacha yozib ko‘r"

#     await update.message.reply_text(javob)

# # botni ishga tushirish
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# print("Bot ishlayapti...")



# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# from openai import OpenAI

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# OPENAI_API_KEY = "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"

# client = OpenAI(api_key=OPENAI_API_KEY)

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "Sen foydalanuvchiga yordam beradigan aqlli assistentsan."},
#             {"role": "user", "content": user_text}
#         ]
#     )

#     answer = response.choices[0].message.content
#     await update.message.reply_text(answer)

# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# app.run_polling()







# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# from groq import Groq

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# async def handle(update, context):
#     user_text = update.message.text

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "Sen Alica AI Botsan 🤖. "
#                     "FAQAT quyidagicha ishlaysan: "
#                     "agar foydalanuvchi 'isming nima?' desa faqat 'Mening ismim Alica AI Bot 🤖' deb javob berasan. "
#                     "Hech qanday qo‘shimcha so‘z yozmaysan. "
#                     "Har doim qisqa va aniq javob berasan."
#                 )
#             },
#            {
#     "role": "system",
#     "content": (
#         "Sen Alica AI Botsan 🤖. "
#         "Sen foydali yordamchisan, javoblaring qisqa va o'zbek tilida bo'lsin."
#         "Faqat juda sodda o‘zbek tilida javob ber. "
#         "Javob 1 yoki 2 gapdan oshmasin. "
#         "Hech qanday ortiqcha so‘z, izoh yoki kirish yozma. "
#         "Har doim aniq javob ber."
#     )
# }
#         ]
#     )

#     answer = response.choices[0].message.content.strip()
#     await update.message.reply_text(answer)


# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# app.run_polling()  






# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# from groq import Groq

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)



# async def handle(update, context):
#     user_text = update.message.text

#      response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "Sen Alica AI Botsan 🤖. "
#                     "FAQAT quyidagicha ishlaysan: "
#                     "agar foydalanuvchi 'isming nima?' desa faqat 'Mening ismim Alica AI Bot 🤖' deb javob berasan. "
#                     "Hech qanday qo‘shimcha so‘z yozmaysan. "
#                     "Har doim qisqa va aniq javob berasan."
#                 )
#             },
#            {
#     "role": "system",
#     "content": (
#         "Sen Alica AI Botsan 🤖. "
#         "Sen foydali yordamchisan, javoblaring qisqa va o'zbek tilida bo'lsin."
#         "Faqat juda sodda o‘zbek tilida javob ber. "
#         "Javob 1 yoki 2 gapdan oshmasin. "
#         "Hech qanday ortiqcha so‘z, izoh yoki kirish yozma. "
#         "Har doim aniq javob ber."
#     )
# }
#         ]
#     )

# if "isming nima" in user_text.lower():
#     await update.message.reply_text("Alica AI Bot 🤖")
#     return

# if "salom" in user_text.lower():
#     await update.message.reply_text("Salom 👋 Qanday yordam kerak?")
#     return


#     answer = response.choices[0].message.content.strip()
#     await update.message.reply_text(answer)


# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# app.run_polling()  



# // Asosiy kod


# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# from groq import Groq

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)


# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text.lower()

#     # 🔥 MUHIM JAVOBLAR (100% aniq)
#     if "isming nima" in user_text:
#         await update.message.reply_text("Alica AI Bot 🤖")
#         return

#     if "salom" in user_text:
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return

#     # 🤖 AI JAVOB
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.1,
#         messages=[
#             {
#                 "role": "system",
#                 "content": "Faqat juda qisqa va tushunarli  tilda javob ber."
#             },
#             {
#                 "role": "user",
#                 "content": user_text
#             }
#         ]
#     )

#     answer = response.choices[0].message.content.strip()
#     await update.message.reply_text(answer)


# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# app.run_polling()






# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# from groq import Groq

# # 🔑 TOKENLAR
# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# # 🧠 MEMORY (har user uchun)
# user_memory = {}


# # funksiyalar
# async def start(update, context):
#     await update.message.reply_text("Salom 👋 Men Xyron AI botman. Savol bering!")

# async def handle(update, context):
#     await update.message.reply_text("Yozganingizni oldim")

# # app
# app = ApplicationBuilder().token(TOKEN).build()

# # handlerlar
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# # run
# app.run_polling()
    
#     user_id = update.message.from_user.id
#     user_text = update.message.text

#     # 🔥 MAXSUS JAVOB (100% aniq)
#     if "isming nima" in user_text.lower():
#         await update.message.reply_text("Alica AI 🤖")
#         return

#     if "salom" in user_text.lower():
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return


#     if "raxmat" in user_text.lower():   
#         await update.message.reply_text("Arzimaydi! Senga yordam bera olganimdan xursandman!")
#         return


#     # 🧠 agar user yangi bo‘lsa
#     if user_id not in user_memory:
#         user_memory[user_id] = []

#     # user yozganini saqlaymiz
#     user_memory[user_id].append({
#         "role": "user",
#         "content": user_text
#     })

#     # oxirgi 10 ta xabarni ishlatamiz
#     messages = [
#         {
#             "role": "system",
#             "content": "Sen  AI botsan 🤖. Faqat qisqa va tushunarli o‘zbek tilida javob ber."
#         }
#     ] + user_memory[user_id][-10:]

#     # 🤖 AI javob
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.1,
#         messages=messages
#     )

#     answer = response.choices[0].message.content.strip()

#     # javobni ham saqlaymiz
#     user_memory[user_id].append({
#         "role": "assistant",
#         "content": answer
#     })



#     # await update.message.reply_text(answer)


# # 🚀 BOTNI ISHGA TUSHIRISH
# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# print("Bot ishga tushdi 🚀")
# app.run_polling()



# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
# from groq import Groq

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# # 🧠 MEMORY
# user_memory = {}


# # ✅ START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Salom 👋 Men Alica man 😊. Qanday yordam bera olaman 🤔?")


# # ✅ HANDLE (HAMMASI SHU ICHIDA BO‘LADI)
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     user_text = update.message.text

#     # 🔥 MAXSUS JAVOBLAR
#     if "isming nima" in user_text.lower():
#         await update.message.reply_text("Alica AI 🤖")
#         return

#     if "salom" in user_text.lower():
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return

#     if "rahmat" in user_text.lower() or "raxmat" in user_text.lower():
#         await update.message.reply_text("Arzimaydi 😊")
#         return

#     # 🧠 MEMORY BOSHLASH
#     if user_id not in user_memory:
#         user_memory[user_id] = []

#     user_memory[user_id].append({
#         "role": "user",
#         "content": user_text
#     })

#     messages = [
#         {
#             "role": "system",
#             "content": "Sen Alica AI botsan 🤖. Faqat qisqa va tushunarli o‘zbek tilida javob ber."
#         }
#     ] + user_memory[user_id][-10:]

#     # 🤖 AI
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.1,
#         messages=messages
#     )

#     answer = response.choices[0].message.content.strip()

#     user_memory[user_id].append({
#         "role": "assistant",
#         "content": answer
#     })

#     await update.message.reply_text(answer)


# # 🚀 APP
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# print("Bot ishga tushdi 🚀")
# app.run_polling()






from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from groq import Groq

# 🔑 TOKENLAR
TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# # 🧠 MEMORY
# user_memory = {}

# # 🟢 START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Salom 👋 Men Alica man 😊. Qanday yordam bera olaman 🤔?"
#     )

# # 🧠 HANDLE
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower()

#     # 🔥 MAXSUS JAVOBLAR
#     if "isming nima" in text:
#         await update.message.reply_text("Alica AI 🤖")
#         return

#     if "salom" in text:
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return

#     if any(word in text for word in ["rahmat", "raxmat", "thanks", "thx"]):
#         await update.message.reply_text("Arzimaydi 😊")
#         return

#     # 🧠 MEMORY BOSHLASH
#     if user_id not in user_memory:
#         user_memory[user_id] = []

#     user_memory[user_id].append({
#         "role": "user",
#         "content": text
#     })

#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "Sen Alica AI botsan 🤖. "
#                 "Faqat juda oddiy, qisqa va tushunarli o‘zbek tilida javob ber. "
#                 "Keraksiz gap yozma."
#             )
#         }
#     ] + user_memory[user_id][-8:]

#     # 🤖 AI JAVOB
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.2,
#         messages=messages
#     )

#     answer = response.choices[0].message.content.strip()

#     user_memory[user_id].append({
#         "role": "assistant",
#         "content": answer
#     })

#     await update.message.reply_text(answer)

# # 🚀 APP
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# print("Bot ishga tushdi 🚀")
# app.run_polling()


# /////////////////////////////////////////////////////////////////////////////////////////////

# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
# from groq import Groq
# from duckduckgo_search import DDGS   # 🌐 QO‘SHILDI

# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"


# client = Groq(api_key=GROQ_API_KEY)

# # 🧠 MEMORY
# user_memory = {}

# # 🌐 INTERNET FUNKSIYA (QO‘SHILDI)
# def search_internet(query):
#     with DDGS() as ddgs:
#         results = list(ddgs.text(query, max_results=1))
#         if results:
#             return results[0]["body"]
#     return ""


# # 🟢 START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Salom 👋 Men Alica man 😊. Qanday yordam bera olaman 🤔?"
#     )

# # 🧠 HANDLE
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower()

#     # 🔥 MAXSUS JAVOBLAR
#     if "isming nima" in text:
#         await update.message.reply_text("Alica AI 🤖")
#         return

#     if "salom" in text:
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return

#     if any(word in text for word in ["rahmat", "raxmat", "thanks", "thx"]):
#         await update.message.reply_text("Arzimaydi 😊")
#         return

#     # 🌐 INTERNET QO‘SHILDI
#     internet_info = search_internet(text)

#     # 🧠 MEMORY BOSHLASH
#     if user_id not in user_memory:
#         user_memory[user_id] = []

#     user_memory[user_id].append({
#         "role": "user",
#         "content": text
#     })

#     # 🔥 MESSAGES (internet bilan)
#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "Sen Alica AI botsan 🤖. "
#                 "Internetdan olingan ma'lumot asosida "
#                 "qisqa va tushunarli o‘zbek tilida javob ber."
#             )
#         },
#         {
#             "role": "system",
#             "content": f"Internet ma'lumot: {internet_info}"
#         }
#     ] + user_memory[user_id][-8:]

#     # 🤖 AI JAVOB
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.2,
#         messages=messages
#     )

#     answer = response.choices[0].message.content.strip()

#     user_memory[user_id].append({
#         "role": "assistant",
#         "content": answer
#     })

#     await update.message.reply_text(answer)

# # 🚀 APP
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# print("Bot ishga tushdi 🚀")
# app.run_polling()




















# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
# from groq import Groq
# from duckduckgo_search import DDGS

# # 🔑 TOKENLAR
# TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
# GROQ_API_KEY = "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"

# client = Groq(api_key=GROQ_API_KEY)

# # 🧠 MEMORY
# user_memory = {}

# # 🌐 INTERNET SEARCH
# def search_internet(query):
#     with DDGS() as ddgs:
#         results = list(ddgs.text(query, max_results=5))
#         texts = [r["body"] for r in results if "body" in r]
#         return " ".join(texts)


# # 🔍 SMART SEARCH (qidirish kerakmi)
# def need_search(text):
#     keywords = [
#         "kim", "nima", "qachon", "qayerda",
#         "yangilik", "2024", "2025", "2026",
#         "prezident", "narx", "texnologiya"
#     ]
#     return any(word in text for word in keywords)


# # 🟢 START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Salom 👋 Men Alica man 🤖\nSavolingizni yozing!"
#     )


# # 🧠 HANDLE
# async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower()

#     # 🔥 MAXSUS JAVOBLAR
#     if "isming nima" in text:
#         await update.message.reply_text("Alica AI 🤖")
#         return

#     if "salom" in text:
#         await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
#         return

#     if any(word in text for word in ["rahmat", "raxmat", "thanks", "thx"]):
#         await update.message.reply_text("Arzimaydi 😊")
#         return

#     # 🧠 MEMORY
#     if user_id not in user_memory:
#         user_memory[user_id] = []

#     # 🌐 INTERNET (faqat kerak bo‘lsa)
#     internet_info = ""
#     if need_search(text):
#         internet_info = search_internet(text)

#     # user xabarini saqlash
#     user_memory[user_id].append({
#         "role": "user",
#         "content": text
#     })

#     # 🧠 AI PROMPT
#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "Sen Alica AI botsan 🤖.\n"
#                 "Har doim juda oddiy, aniq va tushunarli o‘zbek tilida javob ber.\n"
#                 "Agar internet ma'lumot berilgan bo‘lsa, faqat eng yangi va to‘g‘ri qismini ishlat.\n"
#                 "Hozirgi yil 2026.\n"
#                 "Keraksiz gap yozma."
#             )
#         }
#     ]

#     # internet bo‘lsa qo‘shamiz
#     if internet_info:
#         messages.append({
#             "role": "system",
#             "content": f"Internet ma'lumot: {internet_info}"
#         })

#     messages += user_memory[user_id][-8:]

#     # 🤖 AI JAVOB
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         temperature=0.2,
#         messages=messages
#     )

#     answer = response.choices[0].message.content.strip()

#     # javobni saqlash
#     user_memory[user_id].append({
#         "role": "assistant",
#         "content": answer
#     })

#     await update.message.reply_text(answer)


# # 🚀 APP
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

# print("Bot ishga tushdi 🚀")
# app.run_polling()











from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from groq import Groq
from duckduckgo_search import DDGS

# 🔑 KEYS
TOKEN = "8762896641:AAGOVgezzgOrKNOUPufhGTgcRqr9mhoIS7E"
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# 🧠 MEMORY
user_memory = {}

# 🌐 INTERNET SEARCH
def search_internet(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

            texts = []
            for r in results:
                if "body" in r:
                    texts.append(r["body"])

            return " | ".join(texts)
    except:
        return ""


# 🧹 CLEAN FILTER (MUHIM)
def clean_info(text):
    if not text:
        return ""

    sentences = text.split(".")
    good = [s.strip() for s in sentences if len(s.strip()) > 40]

    return ". ".join(good[:5])


# 🔍 QACHON QIDIRISH KERAK
def need_search(text):
    keywords = [
        "kim", "nima", "qachon", "qayerda",
        "yangilik", "2024", "2025", "2026",
        "prezident", "kimdir", "tarix"
    ]
    return any(k in text for k in keywords)


# 🟢 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom 👋 Men Alica man 🤖\nQanday yordam bera olaman?"
    )


# 🧠 HANDLE
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.lower()

    # ⚡ QUICK ANSWERS
    if "isming nima" in text:
        await update.message.reply_text("Alica AI 🤖")
        return

    if "salom" in text:
        await update.message.reply_text("Salom 👋 Qanday yordam bera olaman?")
        return

    if any(w in text for w in ["rahmat", "raxmat", "thanks", "thx"]):
        await update.message.reply_text("Arzimaydi 😊")
        return

    # 🧠 MEMORY
    if user_id not in user_memory:
        user_memory[user_id] = []

    # 🌐 INTERNET
    internet_info = ""
    if need_search(text):
        raw = search_internet(text)
        internet_info = clean_info(raw)

    user_memory[user_id].append({
        "role": "user",
        "content": text
    })

    # 🤖 SYSTEM PROMPT (MUHIM)
    messages = [
        {
            "role": "system",
            "content": (
                "Sen Alica AI botsan 🤖. "
                "Faqat aniq, qisqa va tushunarli javob ber. "
                "Internet ma'lumot bo‘lsa, eng ishonchlisini ishlat. "
                "Agar ma'lumot aniq bo‘lmasa, 'aniq emas' deb ayt. "
                "O‘zingdan to‘qima."
            )
        }
    ]

    if internet_info:
        messages.append({
            "role": "system",
            "content": f"Ishonchli internet ma'lumot: {internet_info}"
        })

    messages += user_memory[user_id][-8:]

    # 🤖 AI RESPONSE
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        messages=messages
    )

    answer = response.choices[0].message.content.strip()

    user_memory[user_id].append({
        "role": "assistant",
        "content": answer
    })

    await update.message.reply_text(answer)


# 🚀 APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🤖 Alica AI bot ishga tushdi...")
app.run_polling()