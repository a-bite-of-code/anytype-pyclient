from pydantic import BaseModel
from .api import AnytypePyClient
from .apimodels import Schema, ApiBase
from .view import ViewSchema
from .object import Object

class ATList(Object):
    """
    Adds one or more objects to a specific list (collection only) by submitting a JSON array of object IDs. 
    Upon success, the endpoint returns a confirmation message. 
    This endpoint is vital for building user interfaces that allow drag‑and‑drop or multi‑select additions to 
      collections, enabling users to dynamically manage their collections without needing to modify the underlying object data.
    """
    def addObjects(self, objectIds: list[str]) -> str:
        return self._endpoint.add_objects_to_list(space_id=self.space_id, list_id=self.id, objectIds=objectIds)
        
    """
    Removes a given object from the specified list (collection only) in a space. 
    The endpoint takes the space, list, and object identifiers as path parameters and is subject to rate limiting. 
    It is used for dynamically managing collections without affecting the underlying object data.
    """
    def removeObject(self, object_id:str) -> str:
        return self._endpoint.remove_object_from_list(space_id=self.space_id, list_id=self.id, object_id=object_id)
        
    """
    Returns a paginated list of views defined for a specific list (query or collection) within a space. 
    Each view includes details such as layout, applied filters, and sorting options, enabling clients to render the list 
      according to user preferences and context. This endpoint is essential for applications that need to display lists 
      in various formats (e.g., grid, table) or with different sorting/filtering criteria.
    """
    def getViews(self, offset:int=0, limit:int=100) -> ViewSchema:
        orig = self._endpoint.get_list_views(space_id=self.space_id, list_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"]=self.space_id
            dt["list_id"]=self.id
        
        return ViewSchema(**orig)
        

class ListSchema(Schema):
    data: list[ATList]
    