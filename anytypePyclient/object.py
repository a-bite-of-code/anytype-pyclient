from pydantic import BaseModel
from typing import Optional, TypeVar
from .apimodels import Schema, PropertyValue, Icon, ApiBase, Icon_Bound
from .api import AnytypePyClient
from .type import Type

PropertyValue_Bound = TypeVar("PropertyValue_Bound", bound=PropertyValue)

class Object(ApiBase):
    list_id: Optional[str] = ""
    
    archived:bool
    icon:Optional[Icon_Bound] = None
    id:str
    layout:str
    markdown:Optional[str] = ""
    name:str
    object:str
    properties:list[PropertyValue_Bound]
    snippet:str
    space_id:str
    type:Optional[Type] = None
    
class ObjectSchema(Schema):
    data:list[Object]
    