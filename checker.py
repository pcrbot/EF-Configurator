from . import reflection
import os
import json
import time
from nonebot import scheduler
from nonebot.log import logger

fd = os.path.dirname(__file__)


@scheduler.scheduled_job('interval', minutes=3)
async def block_checker():
    status = False
    try:
        with open(os.path.join(fd, "block_group.json"), "r") as f:
            block_group = json.load(f)
    except:
        block_group = None
    try:
        with open(os.path.join(fd, "block_user.json"), "r") as f:
            block_user = json.load(f)
    except:
        block_user = None

    if block_group is not None:
        remove_list=list()
        for k, v in block_group.items():
            if v < time.time():
                logger.info(f"群{k}拉黑时间过期")
                remove_list.append(k)
                await reflection.deleter("user" ,k)
                status = True
        for i in remove_list:
            block_group.pop(i, None)
        with open(os.path.join(fd, "block_group.json"), "w") as f:
            json.dump(block_group, f, indent=4)

    if block_user is not None:
        remove_list=list()
        for k, v in block_user.items(): 
            if v < time.time():
                logger.info(f"用户{k}拉黑时间过期")
                remove_list.append(k)
                await reflection.deleter("user" ,k)
                status = True
        for i in remove_list:
            block_user.pop(i, None)
        if status is True:
            with open(os.path.join(fd, "block_user.json"), "w") as f:
                json.dump(block_user, f, indent=4)
