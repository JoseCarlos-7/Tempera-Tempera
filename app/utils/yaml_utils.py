import yaml
from pathlib import Path

class Yaml_metadata:

    def __init__(
        self,
        # file: dict,
        directory: str | Path
    ):


        # self.file = file
        self.directory = directory

    def read_yaml(self):

        with open(self.directory, 'r', encoding='utf-8') as file:
            metadata = yaml.safe_load(file)
        
        return metadata