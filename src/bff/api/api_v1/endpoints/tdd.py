import uuid

import schemas.tdd as tdd_schema
from core.config import settings
from fastapi import APIRouter, HTTPException, Request

router = APIRouter()


@router.post("/tdd", response_model=tdd_schema.TddResponse)
def call_tdd(tdd_request: tdd_schema.TddRequest, request: Request):
    answer = "OK"

    return {"answer": answer}

class ArrayOperations:
    def __init__(self, array):
        self.array = array

    def raw(self):
        return self.array

    def is_all_even(self):
        # self.arrayの要素を1つずつ取り出して、奇数があればFalseを返す
        for num in self.array:
            if num % 2 != 0:
                return False

        return True

    def divided_by_2(self):
        response_array = []
        for num in self.array:
            if num % 2 != 0:
                return self.array
            response_array.append(num // 2)

        return response_array
