from pydantic import BaseModel
from .api import AnytypePyClient
from .apimodels import Schema

class Tag(BaseModel):
    _endpoint:AnytypePyClient = AnytypePyClient()
    
    


class TagSchema(Schema):
    data: list[Tag]
    