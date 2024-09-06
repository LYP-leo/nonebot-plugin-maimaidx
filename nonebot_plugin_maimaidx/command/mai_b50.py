# 各式各样的b50

import re

from nonebot import on_regex, on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.params import RegexMatched

from ..libraries.maimaidx_music_info import *
from ..libraries.maimaidx_player_score import *
from ..libraries.maimaidx_update_plate import *


# 条件b50, 条件为'ap', 'ap+', 'fc', 'fc+'等, 其优先级必须低于b50
lvb50   = on_regex(r'^/?[a-zA-Z0-9-~]*\+?b?50\s?.*$', re.IGNORECASE, priority=6)

fitb50  = on_command('拟合b50', aliases={'拟合50', '拟合定数b50', '拟合定数50'}, priority=5)
worst50  = on_command('丢人50', aliases={'w50', 'worst50'}, priority=5)
limit50  = on_command('寸止b50', aliases={'寸止50', '寸b50', '寸50', 'czb50', 'cz50', 'cb50', 'c50'}, priority=5)

command_list = ['b50', '/b50', 'B50', '/B50']

def get_at_qq(message: Message) -> Optional[int]:
    for item in message:
        if isinstance(item, MessageSegment) and item.type == 'at' and item.data['qq'] != 'all':
            return int(item.data['qq'])

@lvb50.handle()
async def _(event: MessageEvent, match=RegexMatched()):
    match_str = match.group(0)
    string_list = match_str.split()
    length = len(string_list)

    command = string_list[0]
    arg: Message = Message()
    if length > 1:
        arg = Message(string_list[1])

    if command in command_list:
        return

    qqid = get_at_qq(arg) or event.user_id

    username_list = arg.extract_plain_text().split()
    username = None
    if len(username_list) >= 1:
        username = username_list[0]

    if _q := get_at_qq(arg):
        qqid = _q

    b50_cmd = command.split('50')[0].rstrip('b')
    bef = None
    aft = None
    lv_list = []

    if '-' in b50_cmd:
        bef = b50_cmd.split('-')[0]
        aft = b50_cmd.split('-')[1]
    elif '~' in b50_cmd:
        bef = b50_cmd.split('~')[0]
        aft = b50_cmd.split('~')[1]

    if bef and aft:
        if 'lv' in bef:
            bef = bef.split('lv')[1]
        if 'lv' in aft:
            aft = aft.split('lv')[1]
        beg = levelList.index(bef)
        end = levelList.index(aft)
        for i in range(beg, end + 1):
            lv_list.append(levelList[i])

    if len(lv_list) != 0:
        await lvb50.finish(await generate(qqid, username, 'level', lv_list), reply_message=True)
    else:
        if b50_cmd.isdigit() or (b50_cmd[:-1].isdigit() and b50_cmd[-1] == '+'):
            await lvb50.finish(await generate(qqid, username, 'level', [b50_cmd]), reply_message=True)
        elif 'lv' in b50_cmd:
            level = b50_cmd.split('lv')[1]
            await lvb50.finish(await generate(qqid, username, 'level', [level]), reply_message=True)
        elif b50_cmd == 'fc':
            await lvb50.finish(await generate(qqid, username, 'fc', ['fc', 'fcp', 'ap', 'app']), reply_message=True)
        elif b50_cmd == 'fc+':
            await lvb50.finish(await generate(qqid, username, 'fc', ['fcp', 'ap', 'app']), reply_message=True)
        elif b50_cmd == 'ap':
            await lvb50.finish(await generate(qqid, username, 'fc', ['ap', 'app']), reply_message=True)
        elif b50_cmd == 'ap+':
            await lvb50.finish(await generate(qqid, username, 'fc', ['app']), reply_message=True)


@fitb50.handle()
async def _(event: MessageEvent, matcher: Matcher, arg: Message = CommandArg()):
    qqid = get_at_qq(arg) or event.user_id
    username = arg.extract_plain_text().split()
    if _q := get_at_qq(arg):
        qqid = _q
    await matcher.finish(await generate(qqid, username, 'fit', []), reply_message=True)


@worst50.handle()
async def _(event: MessageEvent, matcher: Matcher, arg: Message = CommandArg()):
    qqid = get_at_qq(arg) or event.user_id
    username = arg.extract_plain_text().split()
    if _q := get_at_qq(arg):
        qqid = _q
    await matcher.finish(await generate(qqid, username, 'worst', []), reply_message=True)

@limit50.handle()
async def _(event: MessageEvent, matcher: Matcher, arg: Message = CommandArg()):
    qqid = get_at_qq(arg) or event.user_id
    username = arg.extract_plain_text().split()
    if _q := get_at_qq(arg):
        qqid = _q
    await matcher.finish(await generate(qqid, username, 'limit', []), reply_message=True)