import os
import json
from typing import Optional
from datetime import datetime
class LocalMemory:
    def __init__(self, file_path = "conversation.data"):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def load_memory(self,
                    timestamp: Optional[str] = None,
                    limit: Optional[str] = None,
                    search_term: Optional[str] = None
                    ):
        
        with open(self.file_path, "r") as f:
            messages =  json.load(f)

        if timestamp:
            try:
                target_time = datetime.fromisoformat(timestamp)
                
                filtered_messages = []
                
                for message in messages:
                    message_time = datetime.fromisoformat(message["timestamp"])
                    if len(timestamp) == 10:
                        if target_time.date() == message_time.date():
                            filtered_messages.append(message)
                
                    else:
                        if target_time == message_time:
                            filtered_messages.append(message)
                                        
                messages = filtered_messages

            except ValueError:
                raise ValueError(
                "Invalid timestamp format. Use YYYY-MM-DD "
                "or YYYY-MM-DDTHH:MM:SS"
            )

        if search_term:
            search_term = search_term.lower()

            messages = [
                message for message in messages
                if search_term in message["question"].lower()
                or search_term in message["answer"].lower()
            ]
        
        if limit:
            messages = messages[-limit:]

        return messages
    
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