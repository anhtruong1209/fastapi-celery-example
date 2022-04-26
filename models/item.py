
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel, Field
from fastapi import Query
from typing import Optional

class Item(BaseModel):
    BucketNameAudio: Optional[str] = Query("testdataaa")
    BucketNamePdf: Optional[str] = Query("aisaledoc")
    KeyAudio: Optional[str] = Query("file audio_Vanntb2.mp3")
    PeopleNumber: Optional[int] = Field(..., gt=1, lt=4)
    Audio_Id: Optional[str] = Query("3fd7b64d74709414")
    KeyJson: Optional[str] = Query("file1")
    BucketNameJsonCategory: Optional[str] = Query("category")

class KeyWord(BaseModel):
    BucketDocTranscriptSaleMan: Optional[str] = Query("transcription_saleman")
    KeyTranscriptSaleMan: Optional[str] = Query("file1")




