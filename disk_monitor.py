import psutil

disk = psutil.disk_usage('/')

print("Disk Usage:", disk.percent, "%")
