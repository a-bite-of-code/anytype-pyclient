from pydantic import BaseModel
from typing import Optional, TypeVar
from .apimodels import Schema, TagCreate
from .api import AnytypePyClient
from .tag import Tag, TagSchema

class Property(BaseModel):
    _endpoint:AnytypePyClient = AnytypePyClient()
    
    format:str
    id:str
    key:str
    name:str
    object:str
    
    """
    This endpoint retrieves a paginated list of tags available for a specific property within a space. 
    Each tag record includes its unique identifier, name, and color. 
    This information is essential for clients to display select or multi-select options to users when they 
      are creating or editing objects. 
    The endpoint also supports pagination through offset and limit parameters.
    """
    def listTags(self) -> Schema:
        return self._endpoint.list_tags(space_id=self.space_id, property_id=self.id)
    
    """
    This endpoint retrieves a tag for a given property id. 
    The tag is identified by its unique identifier within the specified space. 
    The response includes the tag's details such as its ID, name, and color. 
    This is useful for clients to display or when editing a specific tag option.
    """
    def getTag(self, tag_id:str) -> Tag:
        return self._endpoint.get_tag(space_id=self.space_id, property_id=self.id, tag_id=tag_id)
        
    """
    This endpoint retrieves a tag for a given property id. 
    The tag is identified by its unique identifier within the specified space. 
    The response includes the tag's details such as its ID, name, and color. 
    This is useful for clients to display or when editing a specific tag option.
    """
    def createTag(self, tag:TagCreate) -> Tag:
        return self._endpoint.create_tag(space_id=self.space_id, property_id=self.id, tag=tag)
        
    
class PropertySchema(Schema):
    data:list[Property]

