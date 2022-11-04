from fabric.api import run, env


env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
env.passwords = {
'root@172.16.200.101:22': 'root', 
'root@172.16.200.102:22': 'root'
}

def host_type():
	run('uname -s')
