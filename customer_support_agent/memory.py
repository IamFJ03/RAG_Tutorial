import json
import os
from datetime import datetime

class LocalMemory:
    def __init__(self, file_path="conversation.data"):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def load_memory(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_memory(self, User, agent):
        memory_content = self.load_memory()

        timestamp =  datetime.now().isoformat()

        memory_content.append({
            "user": User,
            "agent": agent,
            "timestamp": timestamp
        })

        with open(self.file_path, "w") as f:
            json.dump(memory_content, f, indent=4)

    def clear_memory(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)