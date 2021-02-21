import json 
import os
import re 
import yaml

from app.utility.base_world import BaseWorld 
from app.utility.base_service import BaseService
from app.objects.c_agent import Agent

class GPToolsService(BaseService):
    def __init__(self):
        self.log = self.add_service('gptools_svc', self)

        self.methodology = defaultdict(list)

        self.gptools_dir = os.path.join('plugins', 'gptools')
        self.data_dir = os.path.join(self.gptools_dir, 'data')

        async def build_data_directory(self, path_yaml=None):
            """
            build data
            """

