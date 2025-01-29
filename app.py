from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI(title="Background Remover")

@app.post("/")
async def remove_background(file: UploadFile = File(...)):
    image = Image.open(file.file)
    result = remove(image)
    
    byte_arr = io.BytesIO()
    result.save(byte_arr, format="PNG")
    byte_arr.seek(0)
    
    return Response(content=byte_arr.getvalue(), media_type="image/png")
