import os

from app.utility.base_world import BaseWorld
from plugins.atomic.app.atomic_svc import AtomicService

name = 'GMonster'
description = 'Grail Cyber Tech test project'
address = None
access = BaseWorld.Access.RED
data_dir = os.path.join('plugins', 'cheat_sheet', 'data')


async def enable(services):
    # we only ingest data once, and save new abilities in the data/ folder of the plugin
    if "abilities" not in os.listdir(data_dir):
        cheat_sheet_svc = AtomicService()
        await cheat_sheet_svc.clone_th3_firstavenger_repo()
        await cheat_sheet_svc.populate_data_directory()
