from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
path="./Download"

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1-f8QEs8Pfm1zC9mF8NVNNYugG6VPvY5r')}).GetList()
for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
	print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
	x = os.path.join(path, file['title'])

	file.GetContentFile(x)