"""Commands: 
.x, .xperu,.xthanos,.xchua,.xfuke,.xhard,.xface,.xchase
\n\nPorted by @NeoMatrix90
\nImproved by @amnd33p"""

import os
import urllib
import requests
from asyncio import sleep
from uniborg import SYNTAX
from uniborg.util import admin_cmd
import random

@borg.on(admin_cmd(pattern="x(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "peru":
    		emoticons = [
                        "`YOU PRO NIMBA DONT MESS WIDH MEH`",
                        "`Haha yes`",
                        "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
                        "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",
                        "`Some Nimbas need to open their small minds instead of their big mouths`",
                        "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
                        "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
                        "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
                        ]
    elif input_str in "thanos":
       	    emoticons = [
                        "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
                        "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
                        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
                        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
                        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
                        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
                        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
                        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
                        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
                        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
                        ]
    elif input_str in "chua":
      emoticons = [
                        "`Taare hai Asmaan me very very bright`\n`Jhaat na jla bskd dekh le apni height.`",
                        "`Zindagi ki na toote lari`\n`Iski lulli hoti nhi khadi`",
                        "`Kbhi kbhi meri dil me khyaal ata hai`\n`Aise chutiyo ko kon paida kr jata hai😂.`",
                        "`Saawan ka mahina pawan kare shor`\n`Jake gand mara bskd kahi aur.`", 
                        "`Dil ke armaa aansuon me beh gye`\n`Tum bskd ke chutiye hi reh gye.`",
                        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya`\n`Maine is lodu ko randi khane me paya.`",
                        "`Mirza galib ki yeh khani hai`\n`Tu bhosdika hai, yeh sab ki jubani hai.`",
                        ]
    elif input_str in "fuke":
           	emoticons = [
                        "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
                        "`Talking to a liberal is like trying to explain social media to a 70 years old`",
                        "`CHAND PE HAI APUN LAWDE.`",
                        "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
                        "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",
                        "`Cachaa Ooo bhosdi wale Chacha`",
                        "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
                        "`Nachoo Bhosdike Nachoo`",
                        "`Jinda toh jaat ke baal bhi hai`",
                        "`Sab ko pta tu randi ka baccha hai (its just a joke)`", 
                        ]
    elif input_str in "hard":
          	emoticons = [
                        "`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
                        "`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
                        "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
                        "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
                        "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
                        "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
                        "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
                        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
                        "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
                        "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
                        "`Pani kam hai matke me gand marlunga jhatke me.`",
                        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
                        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
                        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
                        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
                        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
                        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
                        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
                        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
                        ]
    elif input_str in "face":
           	   emoticons = [
                        "ʘ‿ʘ",
                        "ヾ(-_- )ゞ",
                        "(っ˘ڡ˘ς)",
                        "(´ж｀ς)",
                        "( ಠ ʖ̯ ಠ)",
                        "(° ͜ʖ͡°)╭∩╮",
                        "(ᵟຶ︵ ᵟຶ)",
                        "(งツ)ว",
                        "ʚ(•｀",
                        "(っ▀¯▀)つ",
                        "(◠﹏◠)",
                        "( ͡ಠ ʖ̯ ͡ಠ)",
                        "( ఠ ͟ʖ ఠ)",
                        "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
                        "(⊃｡•́‿•̀｡)⊃",
                        "(._.)",
                        "{•̃_•̃}",
                        "(ᵔᴥᵔ)",
                        "♨_♨",
                        "⥀.⥀",
                        "ح˚௰˚づ ",
                        "(҂◡_◡)",
                        "ƪ(ړײ)‎ƪ​​",
                        "(っ•́｡•́)♪♬",
                        "◖ᵔᴥᵔ◗ ♪ ♫ ",
                        "(☞ﾟヮﾟ)☞",
                        "[¬º-°]¬",
                        "(Ծ‸ Ծ)",
                        "(•̀ᴗ•́)و ̑̑",
                        "ヾ(´〇`)ﾉ♪♪♪",
                        "(ง'̀-'́)ง",
                        "ლ(•́•́ლ)",
                        "ʕ •́؈•̀ ₎",
                        "♪♪ ヽ(ˇ∀ˇ )ゞ",
                        "щ（ﾟДﾟщ）",
                        "( ˇ෴ˇ )",
                        "눈_눈",
                        "(๑•́ ₃ •̀๑) ",
                        "( ˘ ³˘)♥ ",
                        "ԅ(≖‿≖ԅ)",
                        "♥‿♥",
                        "◔_◔",
                        "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
                        "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
                        "( ఠൠఠ )ﾉ",
                        "٩(๏_๏)۶",
                        "┌(ㆆ㉨ㆆ)ʃ",
                        "ఠ_ఠ",
                        "(づ｡◕‿‿◕｡)づ",
                        "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
                        "“ヽ(´▽｀)ノ”",
                        "༼ ༎ຶ ෴ ༎ຶ༽",
                        "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
                        "(づ￣ ³￣)づ",
                        "(⊙.☉)7",
                        "ᕕ( ᐛ )ᕗ",
                        "t(-_-t)",
                        "(ಥ⌣ಥ)",
                        "ヽ༼ ಠ益ಠ ༽ﾉ",
                        "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
                        "ミ●﹏☉ミ",
                        "(⊙_◎)",
                        "¿ⓧ_ⓧﮌ",
                        "ಠ_ಠ",
                        "(´･_･`)",
                        "ᕦ(ò_óˇ)ᕤ",
                        "⊙﹏⊙",
                        "(╯°□°）╯︵ ┻━┻",
                        r"¯\_(⊙︿⊙)_/¯",
                        "٩◔̯◔۶",
                        "°‿‿°",
                        "ᕙ(⇀‸↼‶)ᕗ",
                        "⊂(◉‿◉)つ",
                        "V•ᴥ•V",
                        "q(❂‿❂)p",
                        "ಥ_ಥ",
                        "ฅ^•ﻌ•^ฅ",
                        "ಥ﹏ಥ",
                        "（ ^_^）o自自o（^_^ ）",
                        "ಠ‿ಠ",
                        "ヽ(´▽`)/",
                        "ᵒᴥᵒ#",
                        "( ͡° ͜ʖ ͡°)",
                        "┬─┬﻿ ノ( ゜-゜ノ)",
                        "ヽ(´ー｀)ノ",
                        "☜(⌒▽⌒)☞",
                        "ε=ε=ε=┌(;*´Д`)ﾉ",
                        "(╬ ಠ益ಠ)",
                        "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
                        "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
                        r"¯\_(ツ)_/¯",
                        "ʕᵔᴥᵔʔ",
                        "(`･ω･´)",
                        "ʕ•ᴥ•ʔ",
                        "ლ(｀ー´ლ)",
                        "ʕʘ̅͜ʘ̅ʔ",
                        "（　ﾟДﾟ）",
                        r"¯\(°_o)/¯",
                        "(｡◕‿◕｡)",
                        ]
    elif input_str in "chase":
        	      emoticons = [
                        "Where do you think you're going?",
                        "Huh? what? did they get away?",
                        "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
                        "Get back here!",
                        "Not so fast...",
                        "Look out for the wall!",
                        "Don't leave me alone with them!!",
                        "You run, you die.",
                        "Jokes on you, I'm everywhere",
                        "You're gonna regret that...",
                        "You could also try /kickme, I hear that's fun.",
                        "Go bother someone else, no-one here cares.",
                        "You can run, but you can't hide.",
                        "Is that all you've got?",
                        "I'm behind you...",
                        "You've got company!",
                        "We can do this the easy way, or the hard way.",
                        "You just don't get it, do you?",
                        "Yeah, you better run!",
                        "Please, remind me how much I care?",
                        "I'd run faster if I were you.",
                        "That's definitely the droid we're looking for.",
                        "May the odds be ever in your favour.",
                        "Famous last words.",
                        "And they disappeared forever, never to be seen again.",
                        "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
                        "Yeah yeah, just tap /kickme already.",
                        "Here, take this ring and head to Mordor while you're at it.",
                        "Legend has it, they're still running...",
                        "Unlike Harry Potter, your parents can't protect you from me.",
                        "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
                        "be the next Vader.",
                        "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
                        "Legend has it, they're still running.",
                        "Keep it up, not sure we want you here anyway.",
                        "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
                        "NO RUNNING IN THE HALLWAYS!",
                        "Hasta la vista, baby.",
                        "Who let the dogs out?",
                        "It's funny, because no one cares.",
                        "Ah, what a waste. I liked that one.",
                        "Frankly, my dear, I don't give a damn.",
                        "My milkshake brings all the boys to yard... So run faster!",
                        "You can't HANDLE the truth!",
                        "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
                        "Hey, look at them! They're running from the inevitable banhammer... Cute.",
                        "Han shot first. So will I.",
                        "What are you running after, a white rabbit?",
                        "As The Doctor would say... RUN!",
                        ]
    else:
       	emoticons = [
                    "( ͡° ͜ʖ ͡°)",
                    "¯\_(ツ)_/¯",
                    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
                    "ʕ•ᴥ•ʔ",
                    "(▀ Ĺ̯▀   )",
                    "(ง ͠° ͟ل͜ ͡°)ง",
                    "༼ つ ◕_◕ ༽つ",
                    "ಠ_ಠ",
                    "(☞ ͡° ͜ʖ ͡°)☞",
                    "¯\_༼ ି ~ ି ༽_/¯",
                    "c༼ ͡° ͜ʖ ͡° ༽⊃",
                    ]
    index = random.randint(0, (len(emoticons)-1))
    output_str = emoticons[index]
    await event.edit(output_str)

@borg.on(admin_cmd(pattern="boobs(?: |$)(.*)"))
async def boobs(e):
    await e.edit("`Finding some big boobs...`")
    await sleep(3)
    await e.edit("`Sending some big boobs...`")
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'boobs.jpg')
    await e.client.send_file(e.chat_id, "boobs.jpg")
    os.remove("boobs.jpg")
    await e.delete()

@borg.on(admin_cmd(pattern="butts(?: |$)(.*)"))
async def butts(e):
    await e.edit("`Finding some beautiful butts...`")
    await sleep(3)
    await e.edit("`Sending some beautiful butts...`")
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'butts.jpg')
    await e.client.send_file(e.chat_id, "butts.jpg")
    os.remove("butts.jpg")
    await e.delete()

SYNTAX.update({
    'nsfw':
    ">`.boobs`"
    "\nUsage: Get boobs image.\n"
    ">`.butts`"
    "\nUsage: Get butts image."
})
    