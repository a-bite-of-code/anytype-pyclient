from typing import Optional
from .apimodels import Schema, ApiBase, Icon_Bound
from .property import Property
from .type import Type

class Template(ApiBase):
    
    archived:bool
    icon:Optional[Icon_Bound]=None
    id:str
    layout:str
    markdown:str
    name:str
    object:str
    properteis:list[Property]
    snippet:str
    space_id:str
    type:Optional[Type] = None
    
class TemplateSchema(Schema):
    data: list[Template]
    