from .apimodels import Schema, TagCreate, ApiBase, TagUpdate
from .tag import Tag, TagSchema
from .utils import get_random_color

class Property(ApiBase):
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
    def listTags(self, offset: int=0, limit: int=100) -> TagSchema:
        orig = self._endpoint.list_tags(space_id=self.space_id, property_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["property_id"]=self.id
            dt["space_id"]=self.space_id
        return TagSchema(**orig)
    
    """
    This endpoint retrieves a tag for a given property id. 
    The tag is identified by its unique identifier within the specified space. 
    The response includes the tag's details such as its ID, name, and color. 
    This is useful for clients to display or when editing a specific tag option.
    """
    def getTag(self, tag_id:str) -> Tag:
        orig = self._endpoint.get_tag(space_id=self.space_id, property_id=self.id, tag_id=tag_id)
        orig["property_id"]=self.id
        orig["space_id"]=self.space_id
        return Tag(**orig)
        
    """
    get or create Tag by Name
    """
    def getOrCreateTagByName(self, tag_name: str) -> Tag:
        offset=0
        limit=10
        has_more=True
        gettedTag=None
        while has_more:
            all_tags=self.listTags()
            for tg in all_tags.data:
                if tg.name == tag_name:
                    gettedTag=tg
                    break
            
            offset += limit
            has_more=all_tags.pagination.has_more
            
        if gettedTag:
            return gettedTag
        else:
            return self.createTagByName(name=tag_name)
        
    """
    This endpoint retrieves a tag for a given property id. 
    The tag is identified by its unique identifier within the specified space. 
    The response includes the tag's details such as its ID, name, and color. 
    This is useful for clients to display or when editing a specific tag option.
    """
    def createTag(self, tag:TagCreate) -> Tag:
        orig = self._endpoint.create_tag(space_id=self.space_id, property_id=self.id, tag=tag)
        orig["property_id"]=self.id
        orig["space_id"]=self.space_id
        return Tag(**orig)
        
    """
    call createTag with random color and specified name
    """
    def createTagByName(self, name: str) -> Tag:
        newTag=TagCreate(color=get_random_color(), name=name)
        return self.createTag(tag=newTag)
        
    """
    This endpoint updates a tag for a given property id in a space. 
    The update process is subject to rate limiting. 
    The tag is identified by its unique identifier within the specified space. 
    The request must include the tag's name and color. 
    The response includes the tag's details such as its ID, name, and color. 
    This is useful for clients when users want to edit existing tags for a property.
    """
    def updateTag(self, tag_id: str, tag: TagUpdate) -> Tag:
        orig=self._endpoint.update_tag(space_id=self.space_id, property_id=self.id, tag_id=tag_id, tag=tag)
        orig["property_id"]=self.id
        orig["space_id"]=self.space_id
        return Tag(**orig)
        
    """
    This endpoint “deletes” a tag by marking it as archived. 
    The deletion process is performed safely and is subject to rate limiting. 
    It returns the tag’s details after it has been archived. 
    Proper error handling is in place for situations such as when the tag isn’t found or the deletion 
      cannot be performed because of permission issues.
    """
    def deleteTag(self, tag_id: str) -> Tag:
        orig=self._endpoint.delete_tag(space_id=self.space_id, property_id=self.id, tag_id=tag_id)
        orig["property_id"]=self.id
        orig["space_id"]=self.space_id
        return Tag(**orig)
    
class PropertySchema(Schema):
    data:list[Property]

