import psutil

memory = psutil.virtual_memory()

print("Memory Usage:", memory.percent, "%")
