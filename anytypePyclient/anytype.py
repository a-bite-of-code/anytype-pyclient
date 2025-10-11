import json
from .api import AnytypePyClient
from .space import SpaceSchema, Space
from .apimodels import SpaceCreate, SpaceUpdate, SearchCondition, ApiBase1
from .object import ObjectSchema


class Anytype(ApiBase1):
    """
    Retrieves a paginated list of all spaces that are accessible by the authenticated user. 
    Each space record contains detailed information such as the space ID, name, 
      icon (derived either from an emoji or image URL), and additional metadata. 
    This endpoint is key to displaying a user’s workspaces.
    """
    def listSpaces(self, offset:int=0, limit:int=100) -> SpaceSchema:
        orig = self._endpoint.list_spaces(offset=offset, limit=limit)
        return SpaceSchema(**orig)
    """
    Fetches full details about a single space identified by its space ID. 
    The response includes metadata such as the space name, icon, and various workspace IDs (home, archive, 
      profile, etc.). This detailed view supports use cases such as displaying space-specific settings.
    """
    def getSpace(self, space_id: str) -> Space:
        orig = self._endpoint.get_space(space_id=space_id)
        return Space(**orig)
    """
    Creates a new space based on a supplied name and description in the JSON request body. 
    The endpoint is subject to rate limiting and automatically applies default configurations such as 
      generating a random icon and initializing the workspace with default settings (for example, a default 
      dashboard or home page). 
    On success, the new space’s full metadata is returned, enabling the client to immediately switch context to the new internal.
    """
    def createSpace(self, space: SpaceCreate) -> Space:
        orig = self._endpoint.create_space(space=space)
        return Space(**orig)
        
    """
    Updates the name or description of an existing space. 
    The request body should contain the new name and/or description in JSON format. 
    This endpoint is useful for renaming or rebranding a workspace without needing to recreate it. 
    The updated space’s metadata is returned in the response.
    """
    def updateSpace(self, space_id:str, space: SpaceUpdate) -> Space:
        orig = self._endpoint.update_space(space_id=space_id, space=space)
        return Space(**orig)
        
    """
    Executes a global search over all spaces accessible to the authenticated user. 
    The request body must specify the query text (currently matching only name and snippet of an object), 
      optional filters on types (e.g., "page", "task"), and sort directives (default: descending by last 
      modified date). 
    Pagination is controlled via offset and limit query parameters to facilitate lazy loading in client UIs. 
    The response returns a unified list of matched objects with their metadata and properties.
    """
    def searchGlobal(self, body: SearchCondition, offset:int=0, limit:int=100) -> ObjectSchema:
        orig = self._endpoint.search_global(body=body, offset=offset, limit=limit)
        print(orig)
        for dt in orig["data"]:
            for prop in dt["properties"]:
                prop["space_id"]=dt["space_id"]
                
            if dt["type"]:
                dt["type"]["space_id"]=dt["space_id"]
                for prop2 in dt["type"]["properties"]:
                    prop2["space_id"] = dt["space_id"]
        return ObjectSchema(**orig)
        
