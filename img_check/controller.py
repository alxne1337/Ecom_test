from fastapi import APIRouter, UploadFile
from .service import check_img
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/nsfw-check', tags=['nsfw-check'])

@router.post('/')
async def check_image(file: UploadFile):
    try:
        if await check_img(file):
            return JSONResponse(
                    status_code=200,
                    content={
                        "status": "REJECTED",
                        "reason": "NSFW content",
                    }
                )
        else:
            return JSONResponse(
                    status_code=200,
                    content={
                        "status": "OK",
                    }
                ) 
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "reason": str(e)
            }
        )