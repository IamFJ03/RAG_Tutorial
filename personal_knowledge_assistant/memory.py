import os
import json

class LocalMemory:
    def __init__(self, file_path = "conversation.data"):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def load_memory(self):
        with open(self.file_path, "r") as f:
            return json.load(f)
    
    def save_memory(self, question, answer, date):
        memory_data = self.load_memory()

        memory_data.append({
            "question": question,
            "answer": answer,
            "timestamp": date
        })

        with open(self.file_path, "w") as f:
            json.dump(memory_data, f, indent=4)

    def clear_memory(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)