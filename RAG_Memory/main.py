from memory import LocalMemory

memory = LocalMemory()

memory.save_message("user", "Hi Assistant")

memory.save_message("AI Agent", "Hello How are you")

result = memory.load_message()

print(result)