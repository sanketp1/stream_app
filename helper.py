from fastapi import UploadFile
import os
from fastapi import status
import uuid

def write_file(file: UploadFile, path:str):
    
    try:
        dir = str(uuid.uuid4())
        os.mkdir(os.path.join(path, dir))

        with open(os.path.join(path,dir, file.filename), "wb") as xfile:
            xfile.write(file.file.read())
    
        xfile.close()
    except:
        return {
            'status':False,
            'response':'Unable to complete operation'
        }
    # for success returning path of file 
    return {
        'status':True,
        'response': os.path.join(path,dir, file.filename)
    }