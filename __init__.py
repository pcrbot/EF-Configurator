# 这里用来放配置命令，但是没想出有什么命令好放的

from nonebot import on_command
from . import reflection
from datetime import timedelta

@on_command("拉黑debug", only_to_me=True)
async def block_debug(session):
    user_id = session.ctx['user_id']
    reflection.set_permanent_block_user(user_id, timedelta(minutes=1))
