from urllib.parse import quote
from fastapi import FastAPI,  Query, HTTPException

from typing import Annotated

app = FastAPI()


@app.get("/")
async def encrypt_url(
        url: Annotated[
            str, Query(regex="^(http|https):\/\/")
        ]
):
    try:
        return {
            "status": 200,
            "data": {
                "encrypted_url": quote(url, safe=':/?=&'),
            },
            "details": None,
        }
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None
            })
    