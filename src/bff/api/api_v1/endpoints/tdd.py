import uuid

import schemas.tdd as tdd_schema
from core.config import settings
from fastapi import APIRouter, HTTPException, Request

router = APIRouter()


@router.post("/tdd", response_model=tdd_schema.TddResponse)
def call_tdd(tdd_request: tdd_schema.TddRequest, request: Request):
    answer = "OK"

    return {"answer": answer}
