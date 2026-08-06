import os
import json


class LocalMemory:
    def __init__(self, file_path="conversation.data"):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def load_memory(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_message(self, role, content):
        messages = self.load_memory()

        messages.append({
            "role": role,
            "content": content
        })

        with open(self.file_path, "w") as f:
            json.dump(messages, f, indent=4)

    def clear_message(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)
        