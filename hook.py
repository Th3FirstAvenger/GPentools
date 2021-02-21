import os

from app.utility.base_world import BaseWorld
from plugins.gptools.app.gptools_svc import GPToolsService

name = 'GPTools'
description = 'The origin of this project is due to the end-of-degree project. My goal is to share my methodology to perform a pentesting attack and others can use it to improve theirs and add content.'
address = None
access = BaseWorld.Access.RED
data_dir = os.path.join('plugins', 'gptools', 'data')


async def enable(services):
    # we only ingest data once, and save new abilities in the data/ folder of the plugin
    if "abilities" not in os.listdir(data_dir):
        gptools_svc = GPToolsService()
        await atomic_svc.populate_data_directory()
