import os
from dotenv import load_dotenv
from pathlib import Path

class Envs:    

    def __init__(
            self,
            entity_name: str):        
        
        self.entity_name = entity_name

    def load_env(self) -> str|Path:
            
        load_dotenv()

        env = os.getenv(self.entity_name)
        return env
    
class Dirs:

    def __init__(self, dir_path: str | Path):
        self.dir_path = Path(dir_path)

    def defines(self, *parts: str) -> Path:
        path = self.dir_path
        for part in parts:
            path /= part
        return path
