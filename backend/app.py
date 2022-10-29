from distutils.log import debug
from mimetypes import init
from urllib import request
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
import logging
import uvicorn
import shutil
import os   
from commentry.getcomment import GetComment
import uuid

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pipeline").setLevel(logging.INFO)

app = FastAPI(title="Chaarminar", version="1.0.0")

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
@app.get("/commentry")
def commentry():
    comment = GetComment()
    new,path = comment.checkdb_commentry()
    if new == 0:
        return {
            'status': 200,
            'result':{
                "new": new
            }
        }
    else:
        return {
            'status': 200,
            'result':{
                "new": new,
                "path": path
            }
        }

@app.get('/goals')
def goals():
    return{
        'status':200,
        'result':
        {
            'goal1':0,
            'goal2':1
        }
    }
@app.get('/test')
def test():
    return{
        'status':200,
        'result':
        [
            {'name':'bot'},
            {'name':'bot'},
            {'name':'bot'},
            {'name':'bot'},
            {'name':'bot'}
        ]
    }

# def generate_job_id():
#     try:
#         logging.info("generating unique job id")
#         id = uuid.uuid4().hex
#         return id[::2][:10]
#     except Exception as e:
#         logging.error(e)
#         logging.error("error generating unique job_id")


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5000,
        host="127.0.0.1",
    )


