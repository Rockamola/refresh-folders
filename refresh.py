import os
import shutil


def cleanse(path):
    print(f"deleting recursive file tree {path}...")
    shutil.rmtree(path)
    print(f"Making new directory {path}....")
    os.makedirs(path)

cleanse_list = [ '/home/justin/Desktop/test/test_1',
	 '/home/justin/Desktop/test/tests']


try:
[cleanse(folder) for folder in cleanse_list]

except OSError:
	print('Something went wrong!')