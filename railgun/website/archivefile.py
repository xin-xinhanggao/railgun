#coding: utf-8
import os
import zipfile
def unzip(zip_name, unzip_dir):
    if not os.path.exists(unzip_dir):
        os.mkdir(unzip_dir)
    zfobj = zipfile.ZipFile(zip_name)
    for file_name in zfobj.namelist():
        file_name = file_name.replace('\\', '/')
        if "MACOSX" in file_name:
            continue
        if file_name.endswith('/'):
            os.mkdir(os.path.join(unzip_dir, file_name))
        else:
            ext_filename = os.path.join(unzip_dir, file_name)
            ext_filedir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_filedir):
                os.mkdir(ext_filedir)
            data = zfobj.read(file_name)
            with open(ext_filename, 'w') as f:
                f.write(data)
    zfobj.close()