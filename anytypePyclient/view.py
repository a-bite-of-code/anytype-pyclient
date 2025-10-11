from .apimodels import ApiBase, Filter, Sort, Schema
from typing import Optional
from .object import ObjectSchema

class View(ApiBase):
    list_id: str
    
    filters: Optional[list[Filter]]=None
    id: str
    layout: str
    name: str
    sorts: Optional[list[Sort]]=None
    
    """
    Returns a paginated list of objects associated with a specific list (query or collection) within a space. 
    When a view ID is provided, the objects are filtered and sorted according to the view's configuration. 
    If no view ID is specified, all list objects are returned without filtering and sorting. 
    This endpoint helps clients to manage grouped objects (for example, tasks within a list) by returning 
    information for each item of the list.
    """
    def getObjectsInView(self, offset:int=0, limit:int=100) -> ObjectSchema:
        orig = self._endpoint.get_list_objects(space_id=self.space_id, list_id=self.list_id, view_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"]=self.space_id
            dt["list_id"]=self.id
            for prop1 in dt["properties"]:
                prop1["space_id"]=self.space_id
            if dt["type"]:
                dt["type"]["space_id"]=self.space_id
                if dt["type"]["properties"]:
                    for prop2 in dt["type"]["properties"]:
                        prop2["space_id"]= self.space_id
                        
        return ObjectSchema(**orig)
    
class ViewSchema(Schema):
    data: list[View]
    