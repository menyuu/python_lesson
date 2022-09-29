# import os
import subprocess

# os.system('ls')は現在推奨されていない
# os.system('ls')

subprocess.run(['dir'], shell=True)
# subprocess.run('dir -ah', shell=True)

