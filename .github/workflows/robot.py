# Thanks to github.com/usernein

import os
import pyrogram

with open('AB.txt') as f:
    os.environ['CAT_FILE'] = f.read()

rom = os.getenv('ROM_NAME')
zip = os.getenv('ZIP_NAME')
cat = os.getenv('CAT_FILE')
romurl = os.getenv('ROM_URL')
dab = os.getenv('DOWNLOAD_AB')

with pyrogram.Client('bot', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN')) as client:
    client.send_message(
        text=f"""<b>{zip} GSI For A/AB Devices</b>

<b>Firmware Base:</b> <a href="{romurl}">HERE</a>

<b>Information:</b>
<code>{cat}</code>

<b>Download AB:</b> <a href="{dab}">HERE</a>

<b>Treble Experience</b> - <i>Channel</i>: @TrebleExperience

<a href="https://github.com/HitaloSama/ErfanGSIs">Ported using ErfanGSIs Tool - Hitsuki's Edit</a>""",
        chat_id=os.getenv('CHAT_ID'),
        parse_mode="html",
        disable_web_page_preview=True
    )
