from fastapi import FastAPI, WebSocket, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import asyncio
from video_decoder import convert_and_stream_resolutions
from helper import write_file
from path_provider import MediaPath, get_media_path
from pathlib import Path
import os
import uuid

app = FastAPI()

class RecordedSession(BaseModel):
    title:str
    desc:str

@app.get("/")
def index():
    return "This is test"

@app.post("/api/add-recorded-session")
async def add_recorded_session(file: UploadFile):
    response = await asyncio.to_thread(write_file, file, get_media_path(MediaPath.RECORDED_SESSION_MEDIA))
    # triggering video decoding
    if(response['status']):
        print("File written successfully")
        # triggering video decoding
        # output_path = os.path.dirname(response['response'])
        return {
            "status":status.HTTP_201_CREATED,
            'message':response['response']
        }    
    else:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=response['response'])
