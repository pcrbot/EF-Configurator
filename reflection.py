import asyncio
import nonebot
from hoshino import priv

import json
import os
import time as m_time

bot = nonebot.get_bot()

fd=os.path.dirname(__file__)
with open(os.path.join(fd, "config.json"), "r") as f:
    config = json.load(f)


async def writer(type, id):
    try:
        with open(config["filter_path"], "r") as f:
            filter_config = json.load(f)
    except:
        filter_config = dict()
    if ".not" not in filter_config:
        filter_config[".not"] = dict()
    # filter_config[".not"]["message_type"] = "group"

    if type == "group":
        if "group_id" not in filter_config[".not"]:
            filter_config[".not"]["group_id"] = dict()
        if ".in" not in filter_config[".not"]["group_id"]:
            filter_config[".not"]["group_id"][".in"] = list()
        filter_config[".not"]["group_id"][".in"].append(id)

    if type == "user":
        if "user_id" not in filter_config[".not"]:
            filter_config[".not"]["user_id"] = dict()
        if ".in" not in filter_config[".not"]["user_id"]:
            filter_config[".not"]["user_id"][".in"] = list()
        filter_config[".not"]["user_id"][".in"].append(id)

    with open(config["filter_path"], "w") as f:
        json.dump(filter_config, f, indent=4)
    await bot.reload_event_filter()

# 糊弄糊弄 期末完再重构
async def deleter(type, id):
    try:
        with open(config["filter_path"], "r") as f:
            filter_config = json.load(f)
    except:
        filter_config = dict()
    if ".not" not in filter_config:
        filter_config[".not"] = dict()
    # filter_config[".not"]["message_type"] = "group"

    if type == "group":
        if "group_id" not in filter_config[".not"]:
            filter_config[".not"]["group_id"] = dict()
        if ".in" not in filter_config[".not"]["group_id"]:
            filter_config[".not"]["group_id"][".in"] = list()
        try:
            filter_config[".not"]["group_id"][".in"].remove(int(id))
        except:
            nonebot.log.logger.warning("移除失败，跳过操作，是否手动编辑过过滤器文件？")

    if type == "user":
        if "user_id" not in filter_config[".not"]:
            filter_config[".not"]["user_id"] = dict()
        if ".in" not in filter_config[".not"]["user_id"]:
            filter_config[".not"]["user_id"][".in"] = list()
        try:
            filter_config[".not"]["user_id"][".in"].remove(int(id))
        except:
            nonebot.log.logger.warning("移除失败，跳过操作，是否手动编辑过过滤器文件？")

    with open(config["filter_path"], "w") as f:
        json.dump(filter_config, f, indent=4)
    await bot.reload_event_filter()

def set_permanent_block_group(group_id, time):
    try:
        with open(os.path.join(fd, "block_group.json"), "r") as f:
            block_group = json.load(f)
    except:
        block_group = dict()
    block_group[group_id] = m_time.time()+time.seconds
    with open(os.path.join(fd, "block_group.json"), "w") as f:
        json.dump(block_group, f, indent=4)
    loop=asyncio.get_running_loop()
    asyncio.run_coroutine_threadsafe(writer("group", group_id), loop)


def set_permanent_block_user(user_id, time):
    try:
        with open(os.path.join(fd, "block_user.json"), "r") as f:
            block_user = json.load(f)
    except:
        block_user = dict()
    block_user[user_id] = m_time.time()+time.seconds
    with open(os.path.join(fd, "block_user.json"), "w") as f:
        json.dump(block_user, f, indent=4)
    loop=asyncio.get_running_loop()
    asyncio.run_coroutine_threadsafe(writer("user", user_id), loop)


setattr(priv, "set_block_group", set_permanent_block_group)
setattr(priv, "set_block_user", set_permanent_block_user)
