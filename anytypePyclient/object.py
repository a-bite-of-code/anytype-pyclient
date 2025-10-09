from pydantic import BaseModel
from typing import Optional, TypeVar
from .apimodels import Schema, PropertyValue, Icon
from .api import AnytypePyClient
from .type import Type

Icon_Bound = TypeVar("Icon_Bound", bound=Icon)
PropertyValue_Bound = TypeVar("PropertyValue_Bound", bound=PropertyValue)

class Object(BaseModel):
    _endpoint:AnytypePyClient = AnytypePyClient()
    
    archived:bool
    icon:Optional[Icon_Bound] = None
    id:str
    layout:str
    markdown:str
    name:str
    object:str
    properties:list[PropertyValue_Bound]
    snippet:str
    space_id:str
    type:Optional[Type] = None
    
class ObjectSchema(Schema):
    data:list[Object]
    