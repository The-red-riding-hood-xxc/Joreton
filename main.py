import discord
from discord.ext import commands
import os  # 新增：用於讀取系統環境變數
from dotenv import load_dotenv  # 新增：用於載入 .env 檔案

# 0. 載入 .env 檔案中的設定
load_dotenv()

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
    if message.author == bot.user:
        return

    msg = message.content.lower()
    a = "周雨同"
    sheep = ["喜羊羊", "替罪羊", "笑笑羊", "美羊羊", "懶羊羊", "沸羊羊", "暖羊羊", "慢羊羊", "電子羊", "陳紫羊", "昏睡羊"]

    for name in sheep:
        if name in msg:
            reply_text = (
                f"我，我是{name}\n"
                "跟日本人圈錢的，有別人\n"
                "誰？\n"
                "我不能說，說了我就沒命了\n"
                "呃\n"
                "李，李蘭群李蘭群"
            )
            await message.channel.send(reply_text)
            break 

    if a in msg:
        reply_text = (
            "眼見周雨同還不開竅老烏當即表示他周雨同既然當了這麼長時間的罕見怎麼可能就撈了20萬大洋眼看自己的事情敗露周雨同被嚇得尿不濕都尿濕了隨即他就老老實實告訴了老烏自己其實就是個替罪羊而已"
        )
        await message.channel.send(reply_text)

    await bot.process_commands(message)

# 5. 啟動機器人 
# 從 .env 檔案中抓取名為 DISCORD_TOKEN 的變數
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)