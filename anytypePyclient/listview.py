from pydantic import BaseModel
from .api import AnytypePyClient
from .apimodels import Schema, ApiBase

class AnyList(BaseModel):
    id: str
    name: str
    
    """
    Adds one or more objects to a specific list (collection only) by submitting a JSON array of object IDs. 
    Upon success, the endpoint returns a confirmation message. 
    This endpoint is vital for building user interfaces that allow drag‑and‑drop or multi‑select additions to 
    collections, enabling users to dynamically manage their collections without needing to modify 
    the underlying object data.
    """
    def addObjects(self, objectIds: list[str]) -> str:
        return self._endpoint.add_objects_to_list(space_id=self.space_id, list_id=self.id, objectIds=objectIds)
        
    """
    Removes a given object from the specified list (collection only) in a space. 
    The endpoint takes the space, list, and object identifiers as path parameters and is subject to rate 
      limiting. It is used for dynamically managing collections without affecting the underlying object data.
    """
    def removeObject(self, object_id:str) -> str:
        return self._endpoint.remove_object_from_list(space_id=self.space_id, list_id=self.id, object_id=object_id)
        
    """
    Returns a paginated list of views defined for a specific list (query or collection) within a space. 
    Each view includes details such as layout, applied filters, and sorting options, enabling clients to 
    render the list according to user preferences and context. This endpoint is essential for applications 
    that need to display lists in various formats (e.g., grid, table) or with different sorting/filtering criteria.
    """
    def getViews(self, offset:int=0, limit:int=100) -> Schema:
        return self._endpoint.get_list_views(space_id=self.space_id, list_id=self.id, offset=offset, limit=limit)
        
    """
    Returns a paginated list of objects associated with a specific list (query or collection) within a space. 
    When a view ID is provided, the objects are filtered and sorted according to the view's configuration. 
    If no view ID is specified, all list objects are returned without filtering and sorting. 
    This endpoint helps clients to manage grouped objects (for example, tasks within a list) by returning 
    information for each item of the list.
    """
    def getObjects(self, view_id: str, offset:int=0, limit:int=100) -> Schema:
        return self._endpoint.get_objects_in_list(space_id=self.space_id, list_id=space.list_id, view_id=view_id, offset=offset, limit=limit)
        
    

class ListSchema(Schema):
    data: list[AnyList]
    