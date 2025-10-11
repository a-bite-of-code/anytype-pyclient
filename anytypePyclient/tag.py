from pydantic import BaseModel
from .api import AnytypePyClient
from .apimodels import Schema, ApiBase

class Tag(ApiBase):
    property_id: str
    
    color: str
    id: str
    key: str
    name: str
    object: str
    

class TagSchema(Schema):
    data: list[Tag]
    