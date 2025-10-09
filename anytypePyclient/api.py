import json
from typing import Any
from .utils import ApiEndPoint

class AnytypePyClient:
    def __init__(self):
        self.api_endpoint = ApiEndPoint()
    
    def is_connected(self) -> bool:
        try:
            sps=self.list_spaces()
            return True
        except Exception as e:
            return False
            
    #Search
    """
    """
    def search_global(self, body: object, offset:int=0, limit:int=100) -> Any:
        api="search"
        cleaned_dump = {k: v for k, v in body.model_dump().items() if v is not None}
        payload = json.dumps(cleaned_dump)
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=api, data=payload, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to search in; must be retrieved from ListSpaces endpoint
    """
    def search_space(self, space_id: str, body: object, offset:int=0, limit:int=100) -> Any:
        api=f"spaces/{space_id}/search"
        cleaned_dump = {k: v for k, v in body.model_dump().items() if v is not None}
        payload = json.dumps(cleaned_dump)
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=api, data=payload, params=params)
        return resp.json()
    
    #Spaces
    """
    """
    def list_spaces(self, offset:int=0, limit:int=100) -> Any:
        api="spaces"
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=api, params=params)
        return resp.json()
    """
    """
    def create_space(self, space: object) -> Any:
        api = "spaces" 
        cleaned_dump = {k: v for k, v in space.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("POST", url=api, data=payload)
        data = resp.json().get("space")
        if not data:
            raise RuntimeError("Spaces create failed.")
        return data
    """
    space_id    string    required
    The ID of the space to retrieve; must be retrieved from ListSpaces endpoint
    """
    def get_space(self, space_id: str) -> Any:
        api = f"spaces/{space_id}"
        resp = self.api_endpoint.requestApi("GET", url=api)
        data = resp.json().get("space")
        if not data:
            raise RuntimeError("Spaces create failed.")
        return data
    """
    space_id    string    required
    The ID of the space to update; must be retrieved from ListSpaces endpoint
    """
    def update_space(self, space_id: str, space: object) -> Any:
        api = f"spaces/{space_id}" 
        cleaned_dump = {k: v for k, v in space.model_dump().items() if v is not None}
        payload = json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("PATCH", url=api, data=payload)
        data = resp.json().get("space")
        if not data:
            raise RuntimeError("Space create failed.")
        return data
        
    #Lists
    """
    space_id    string    required
    The ID of the space to which the list belongs; must be retrieved from ListSpaces endpoint

    list_id    string    required
    The ID of the list to which objects will be added; must be retrieved from SearchSpace endpoint with types: ['collection', 'set']
    """
    def adad_objects_to_list(self, space_id: str, list_id: str, objectIds: list[str]) -> str:
        api = f"spaces/{space_id}/lists/{list_id}/objects" 
        payload = json.dumps(objectIds)
        resp = self.api_endpoint.requestApi("POST", url=api, data=payload, params=params)
        if not resp:
            raise RuntimeError("object add failed.")
        return resp
    """
    space_id    string    required
    The ID of the space to which the list belongs; must be retrieved from ListSpaces endpoint

    list_id    string    required
    The ID of the list from which the object will be removed; must be retrieved from SearchSpace endpoint with types: ['collection', 'set']

    object_id    string    required
    The ID of the object to remove from the list; must be retrieved from SearchSpace or GlobalSearch endpoints or obtained from response context
    """
    def remove_object_from_list(self, space_id: str, list_id: str, object_id: str) -> str:
        api = f"spaces/{space_id}/lists/{list_id}/objects/{object_id}" 
        resp = self.api_endpoint.requestApi("DELETE", url=api)
        if not resp:
            raise RuntimeError("object remove failed.")
        return resp
    """
    space_id    string    required
    The ID of the space to which the list belongs; must be retrieved from ListSpaces endpoint

    list_id    string    required
    The ID of the list to retrieve views for; must be retrieved from SearchSpace endpoint with types: ['collection', 'set']
    """
    def get_list_views(self, space_id: str, list_id: str, offset:int=0, limit:int=100) -> Any:
        api = f"spaces/{space_id}/lists/{list_id}/views" 
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=api, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to which the list belongs; must be retrieved from ListSpaces endpoint

    list_id    string    required
    The ID of the list to retrieve objects for; must be retrieved from SearchSpace endpoint with types: ['collection', 'set']

    view_id    string    required
    The ID of the view to retrieve objects for; must be retrieved from ListViews endpoint or omitted if you want to get all objects in the list
    """
    def get_list_objects(self, space_id: str, list_id: str, view_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/lists/{list_id}/views/{view_id}/objects" 
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=url, params=params)
        return resp.json()
    
    #Members
    """
    space_id    string    required
    The ID of the space to list members for; must be retrieved from ListSpaces endpoint
    """
    def list_members(self, space_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/members" 
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=url, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to get the member from; must be retrieved from ListSpaces endpoint

    member_id    string    required
    Member ID or Identity; must be retrieved from ListMembers endpoint or obtained from response context
    """
    def get_member(self, space_id: str, member_id: str) -> Any:
        url = f"spaces/{space_id}/members/{member_id}" 
        resp = self.api_endpoint.requestApi("GET", url=url)
        data = resp.json().get("member")
        return data
    
    #Objects
    """
    space_id    string    required
    The ID of the space in which to list objects; must be retrieved from ListSpaces endpoint
    """
    def list_objects(self, space_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/objects" 
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=url, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space in which to create the object; must be retrieved from ListSpaces endpoint
    """
    def create_object(self, space_id: str, obj: object) -> Any:
        url = f"spaces/{space_id}/objects" 
        cleaned_dump = {k: v for k, v in obj.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint("POST", url=url, data=payload)
        data = resp.json().get("object")
        if not data:
            raise RuntimeError("no objects created.")
        return data
    """
    space_id    string    required
    The ID of the space in which the object exists; must be retrieved from ListSpaces endpoint

    object_id    string    required
    The ID of the object to delete; must be retrieved from ListObjects, SearchSpace or GlobalSearch endpoints or obtained from response context
    """
    def delete_object(self, space_id: str, object_id: str) -> Any:
        url = f"spaces/{space_id}/objects/{object_id}" 
        resp = self.api_endpoint.requestApi("DELETE", url=url)
        data = resp.json().get("object")
        if not data:
            raise RuntimeError("object delete failed")
        return data
    """
    space_id    string    required
    The ID of the space in which the object exists; must be retrieved from ListSpaces endpoint

    object_id    string    required
    The ID of the object to delete; must be retrieved from ListObjects, SearchSpace or GlobalSearch endpoints or obtained from response context
    """
    def get_object(self, space_id: str, object_id: str) -> Any:
        url = f"spaces/{space_id}/objects/{object_id}" 
        resp = self.api_endpoint.requestApi("GET", url=url)
        data = resp.json().get("object")
        if not data:
            raise RuntimeError("invalid object_id.")
        return data
    """
    space_id    string    required
    The ID of the space in which the object exists; must be retrieved from ListSpaces endpoint

    object_id    string    required
    The ID of the object to delete; must be retrieved from ListObjects, SearchSpace or GlobalSearch endpoints or obtained from response context
    """
    def update_object(self, spaec_id:str, object_id:str, obj: object) -> Any:
        url = f"spaces/{space_id}/objects/{object_id}" 
        cleaned_dump = {k: v for k, v in obj.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("PATCH", url=url, data=payload)
        data = resp.json().get("object")
        if not data:
            raise RuntimeError("object update failed.")
        return data
        
    #Properties
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint
    """
    def list_properties(self, space_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/properties" 
        params = {"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url=url, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint
    """
    def create_property(self, space_id: str, prop: object) -> Any:
        url = f"spaces/{space_id}/properties" 
        cleaned_dump = {k: v for k, v in prop.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("POST", url, data=payload)
        resp.raise_for_status()
        data = resp.json().get("property")
        if not data:
            raise RuntimeError("property create failed.")
        return data
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete; must be retrieved from ListProperties endpoint or obtained from response context
    """
    def delete_property(self, space_id: str, property_id: str) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}" 
        resp = self.api_endpoint.requestApi("DELETE", url)
        resp.raise_for_status()
        data = resp.json().get("property")
        if not data:
            raise RuntimeError("property delete failed.")
        return data
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete; must be retrieved from ListProperties endpoint or obtained from response context
    """
    def get_property(self, space_id: str, property_id: str) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}" 
        resp = self.api_endpoint.requestApi("GET", url)
        resp.raise_for_status()
        data = resp.json().get("property")
        if not data:
            raise RuntimeError("invalid property id.")
        return data
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete; must be retrieved from ListProperties endpoint or obtained from response context
    """
    def update_property(self, space_id: str, property_id:str, prop: object) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}" 
        cleaned_dump = {k: v for k, v in prop.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("PATCH", url, data=payload)
        data = resp.json().get("property")
        if not data:
            raise RuntimeError("property update failed.")
        return data
        
    #Tags
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete; must be retrieved from ListProperties endpoint or obtained from response context
    """
    def list_tags(self, space_id: str, property_id: str) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}/tags" 
        resp = self.api_endpoint.requestApi("GET", url)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to list properties for; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete; must be retrieved from ListProperties endpoint or obtained from response context
    """
    def create_tag(self, space_id: str, tag: object) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}/tags" 
        cleaned_dump = {k: v for k, v in tag.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("POST", url, data=payload)
        data = resp.json().get("tag")
        if not data:
            raise RuntimeError("tag create failed.")
        return data
    """
    space_id    string    required
    The ID of the space to delete the tag from; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete the tag for; must be retrieved from ListProperties endpoint or obtained from response context

    tag_id    string    required
    The ID of the tag to delete; must be retrieved from ListTags endpoint or obtained from response context
    """
    def delete_tag(self, space_id: str, property_id: str, tag_id: str) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}/tags/{tag_id}" 
        resp = self.api_endpoint.requestApi("DELETE", url)
        data = resp.json().get("tag")
        if not data:
            raise RuntimeError("tag delete failed.")
        return data
    """
    space_id    string    required
    The ID of the space to delete the tag from; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete the tag for; must be retrieved from ListProperties endpoint or obtained from response context

    tag_id    string    required
    The ID of the tag to delete; must be retrieved from ListTags endpoint or obtained from response context
    """
    def get_tag(self, space_id: str, property_id: str, tag_id: str) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}/tags/{tag_id}" 
        resp = self.api_endpoint.requestApi("GET", url)
        data = resp.json().get("tag")
        if not data:
            raise RuntimeError("no tag found.")
        return data
    """
    space_id    string    required
    The ID of the space to delete the tag from; must be retrieved from ListSpaces endpoint

    property_id    string    required
    The ID of the property to delete the tag for; must be retrieved from ListProperties endpoint or obtained from response context

    tag_id    string    required
    The ID of the tag to delete; must be retrieved from ListTags endpoint or obtained from response context
    """
    def update_tag(self, space_id: str, property_id: str, tag_id: str, tag: object) -> Any:
        url = f"spaces/{space_id}/properties/{property_id}/tags/{tag_id}" 
        cleaned_dump = {k: v for k, v in tag.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("PATCH", url, data=payload)
        data = resp.json().get("tag")
        if not data:
            raise RuntimeError("tag update failed.")
        return data
        
    #Types
    """
    space_id    string    required
    The ID of the space to retrieve types from; must be retrieved from ListSpaces endpoint
    """
    def list_types(self, space_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/types" 
        params={"offset":offset,"limit":limit}
        resp = self.api_endpoint.requestApi("GET", url, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to retrieve types from; must be retrieved from ListSpaces endpoint
    """
    def create_type(self, space_id: str, type: object) -> Any:
        url = f"spaces/{space_id}/types" 
        cleaned_dump = {k: v for k, v in type.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("POST", url, data=payload)
        data = resp.json().get("type")
        if not data:
            raise RuntimeError("type create failed.")
        return data
    """
    space_id    string    required
    The ID of the space from which to delete the type; must be retrieved from ListSpaces endpoint

    type_id    string    required
    The ID of the type to delete; must be retrieved from ListTypes endpoint or obtained from response context
    """
    def delete_type(self, space_id: str, type_id: str) -> Any:
        url = f"spaces/{space_id}/types/{type_id}" 
        resp = self.api_endpoint.requestApi("DELETE", url)
        data = resp.json().get("type")
        if not data:
            raise RuntimeError("type delete failed.")
        return data
    """
    space_id    string    required
    The ID of the space from which to delete the type; must be retrieved from ListSpaces endpoint

    type_id    string    required
    The ID of the type to delete; must be retrieved from ListTypes endpoint or obtained from response context
    """
    def get_type(self, space_id: str, type_id: str) -> Any:
        url = f"spaces/{space_id}/types/{type_id}" 
        resp = self.api_endpoint.requestApi("GET", url)
        data = resp.json().get("type")
        if not data:
            raise RuntimeError("invalid type_id.")
        return data
    """
    space_id    string    required
    The ID of the space from which to delete the type; must be retrieved from ListSpaces endpoint

    type_id    string    required
    The ID of the type to delete; must be retrieved from ListTypes endpoint or obtained from response context
    """
    def update_type(self, space_id: str, type_id: str, type: object) -> Any:
        url = f"spaces/{space_id}/types/{type_id}" 
        cleaned_dump = {k: v for k, v in type.model_dump().items() if v is not None}
        payload=json.dumps(cleaned_dump)
        resp = self.api_endpoint.requestApi("PATCH", url, data=payload)
        data = resp.json().get("type")
        if not data:
            raise RuntimeError("type update failed.")
        return data
        
    #Templates
    """
space_idstringrequired
The ID of the space to which the type belongs; must be retrieved from ListSpaces endpoint

type_idstringrequired
The ID of the type to retrieve templates for; must be retrieved from ListTypes endpoint or obtained from response context
    """
    def list_templates(self, space_id: str, type_id: str, offset:int=0, limit:int=100) -> Any:
        url = f"spaces/{space_id}/types/{type_id}/templates" 
        params={"offset":offset, "limit":limit}
        resp = self.api_endpoint.requestApi("GET", url, params=params)
        return resp.json()
    """
    space_id    string    required
    The ID of the space to which the template belongs; must be retrieved from ListSpaces endpoint

    type_id    string    required
    The ID of the type to which the template belongs; must be retrieved from ListTypes endpoint or obtained from response context

    template_id    string    required
    The ID of the template to retrieve; must be retrieved from ListTemplates endpoint or obtained from response context
    """
    def get_template(self, space_id: str, type_id: str, template_id: str) -> Any:
        url = f"spaces/{space_id}/types/{type_id}/templates/{template_id}" 
        resp = self.api_endpoint.requestApi("GET", url)
        data = resp.json().get("template")
        if not data:
            raise RuntimeError("no template found.")
        return data
        