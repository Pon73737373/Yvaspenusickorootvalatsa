from pyrogram import Client, filters

from random import choice



api_id = 19973164 

api_hash = "763a792a4883df9840e940558047fa95"

app = Client("account", api_id, api_hash) 



prefix = '.'



@app.on_message(filters.command('tid',prefixes=prefix) & filters.me)

async def my_handler(client, message):

    print(message)

    

@app.on_message(filters.command('help',prefixes=prefix) & filters.me)  

async def tmat_com(_, msg):

    await msg.edit('Помощь команды: .help список команд .tid получить информацию об чате .tmat куча матов(высер агро школньика) .tjoke рандом андекдот')





@app.on_message(filters.command('tmat',prefixes=prefix) & filters.me)  

async def tmat_com(_, msg):

    await msg.edit('Заткни свое ебало я тебя в рот ебал блядина ебучая что бы тебя поездом перехуярило тварь ебучая соси хуй пидрила я тебя на хую вертел тварюка хуйлуша ')



from random import choice



jokes = [

  'На соревнованиях по плаванию электрик Олег замкнул тройку лидеров.',

  'Сын червечок подходит к маме "Мам, а где папа?" она отвечает: "C мужиками на рыбалку уехал.".',

]



@app.on_message(filters.command('tjoke',prefixes=prefix) & filters.me)  

async def tmat_com(_, msg):

    await msg.edit(choice(jokes))







def run():

    print("ЮзерБот от Тузика помогали рим мир к и пурпл,версия 0.2 global update,спасибо за использование юзербота <3")

    app.run()



run()
