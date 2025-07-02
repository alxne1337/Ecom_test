from fastapi import UploadFile, HTTPException, File
from httpx import AsyncClient

import requests
from dotenv import load_dotenv
import os



async def check_img(file: File) -> bool:
    try:
        load_dotenv()

        if not os.getenv('API_KEY'):
            raise HTTPException(status_code=500, detail="API key not configured")

        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Файл должен быть изображением!")
        
        async with AsyncClient() as client:
            
            contents = await file.read()

            files = {
                'image': (file.filename, contents, file.content_type)
            }

            response = await client.post("https://api.deepai.org/api/nsfw-detector",
                                files=files,
                                headers={'Api-Key': os.getenv('API_KEY')}
                            )

            if response.status_code != 200:
                error_text = response.text
                raise HTTPException(status_code=502, detail=f"API error: {response.status_code} - {error_text}")

            try:
                data = response.json()
            except Exception:
                raise HTTPException(status_code=502, detail=f"Invalid JSON response: {response.text}")

            if 'output' not in data or 'nsfw_score' not in data['output']:
                raise HTTPException(status_code=502, detail=f"Unexpected API response: {data}")

            nsfw_score = data['output']['nsfw_score']
            return nsfw_score <= 0.7

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    
    finally:
        await file.close()

