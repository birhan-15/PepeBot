# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Urban Dictionary
Syntax: .ud Query"""
import urbandict
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ud ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("processing...")
    str = event.pattern_match.group(1)
    if not str:
        get = await event.get_reply_message()
        str = get.text
    try:
        mean = urbandict.define(str)
        if len(mean) > 0:
            await event.edit(
                'Text: **' +
                str +
                '**\n\nMeaning: **' +
                mean[0]['def'] +
                '**\n\n' +
                'Example: \n__' +
                mean[0]['example'] +
                '__'
            )
        else:
            await event.edit("No result found for **" + str + "**")
    except BaseException:
        await event.edit("No result found for **" + str + "**")
