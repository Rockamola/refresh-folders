import os
import shutil


def cleanse(path):
    print(f"deleting recursive file tree {path}...")
    shutil.rmtree(path)
    print(f"Making new directory {path}....")
    os.makedirs(path)

cleanse_list = [ '/path/to/file/directory',
	 '/path/to/secondary/file/directory']


try:
[cleanse(folder) for folder in cleanse_list]

except OSError:
	print('Something went wrong!')
