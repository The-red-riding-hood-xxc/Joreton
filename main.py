import discord
from discord.ext import commands

# 1. 設定權限 (Intents)
intents = discord.Intents.default()
intents.message_content = True 

# 2. 建立機器人物件
bot = commands.Bot(command_prefix="!", intents=intents)

# 3. 當機器人上線時的提示
@bot.event
async def on_ready():
    print(f'成功登入！目前身分是：{bot.user}')
    print('--- 機器人已就緒 ---')

# 4. 關鍵字偵測邏輯
@bot.event
async def on_message(message):
    # 【注意】以下所有的程式碼都必須比 async def 往右縮進 4 個空格
    
    # 如果訊息是機器人自己發的，就不要理它
    if message.author == bot.user:
        return

    # 將訊息內容存進一個變數，方便判斷
    msg = message.content.lower()

    a = "周雨同"
    # 定義羊群清單
    sheep = ["喜羊羊", "替罪羊", "笑笑羊", "美羊羊", "懶羊羊", "沸羊羊", "暖羊羊", "慢羊羊", "電子羊"]

    # 遍歷清單，看看是哪隻羊被點名了
    for name in sheep:
        if name in msg:
            # 使用 f-string 組合字串，並用 \n 換行
            reply_text = (
                f"我，我是{name}\n"
                "跟日本人圈錢的，有別人\n"
                "誰？\n"
                "我不能說，說了我就沒命了\n"
                "呃\n"
                "李，李蘭群李蘭群"
            )
            await message.channel.send(reply_text)
            break # 找到一個符合的就停止，避免重複發送
    if a in msg:
        reply_text = (
            "眼見周雨同還不開竅老烏當即表示他周雨同既然當了這麼長時間的罕見怎麼可能就撈了20萬大洋眼看自己的事情敗露周雨同被嚇得尿不濕都尿濕了隨即他就老老實實告訴了老烏自己其實就是個替罪羊而已"
        )
        await message.channel.send(reply_text)

    # 確保其他「指令」功能（如 !help）還能運作
    await bot.process_commands(message)

# 5. 啟動機器人 (把你的 Token 填在括號內，記得要用引號包起來)
bot.run('MTQ2ODkxNDYxNjcyODk0NDY2MA.G68Bkt.RQ9-KBRD-W1rNpxkoNjlNf5Jl_GDJxFLcy1om8')