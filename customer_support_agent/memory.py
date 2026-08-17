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

    def save_memory(self, conversation):
        memory_content = self.load_memory()

        timestamp =  datetime.now().isoformat()

        memory_text = '\n'.join(
            f"{message.type.upper()}: {message.content}"
            for message in conversation
        )
        
        memory_content.append({
            "page_content": memory_text,
            "timestamp": timestamp
        })

        with open(self.file_path, "w") as f:
            json.dump(memory_content, f, indent=4)

    def clear_memory(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)