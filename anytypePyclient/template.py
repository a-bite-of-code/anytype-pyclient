from pydantic import BaseModel
from typing import TypeVar, Optional
from .api import AnytypePyClient
from .apimodels import Icon, Schema
from .property import Property, PropertySchema

Icon_Bound = TypeVar("Icon_Bound", bound=Icon)

class Template(BaseModel):
    _endpoint:AnytypePyClient = AnytypePyClient()
    
    archived:bool
    icon:Icon_Bound
    id:str
    layout:str
    markdown:str
    name:str
    object:str
    properteis:list[Property]
    snippet:str
    space_id:str
    type:object
    
class TemplateSchema(Schema):
    data: list[Template]
    