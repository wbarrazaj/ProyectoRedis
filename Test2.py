import os

home_dir = os.system("pwd")

#print(home_dir)


import subprocess

list_files = subprocess.run(["redis-cli", "INFO" , "SERVER"])
print(subprocess.STDOUT)

#useless_cat_call = subprocess.run(["redis-cli --stat"], stdout=subprocess.PIPE, text=True, input="Hello from the other side")
#print(useless_cat_call.stdout)  # Hello

