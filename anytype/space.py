from typing import Optional
from .apimodels import (Schema, SearchSort, 
                        SearchCondition, ApiBase1, 
                        Icon_Bound, TypeCreate,
                        TypeUpdate, PropertyCreate, 
                        PropertyUpdate)
from .object import (ObjectCreate, 
                     ObjectUpdate,
                     ObjectSchema, 
                     Object
                    )
from .type import TypeSchema, Type
from .property import Property, PropertySchema
from .member import Member, MemberSchema
from .list import ListSchema

class Space(ApiBase1):
    description:Optional[str]
    gateway_url:str
    icon: Optional[Icon_Bound]
    id:str
    name:str
    network_id:str
    object:str
    
    """
    Performs a search within a single space (specified by the space_id path parameter). 
    Like the global search, it accepts pagination parameters and a JSON payload containing the search query, 
      types, and sorting preferences. The search is limited to the provided space and returns a list of objects 
      that match the query. 
    This allows clients to implement space‑specific filtering without having to process extraneous results.
    """
    def searchSpace(self, body: SearchCondition, offset:int=0, limit:int=100) -> ObjectSchema:
        orig = self._endpoint.search_space(space_id=self.id, body=body, offset=offset, limit=limit)
        for dt in orig["data"]:
            for prop in dt["properties"]:
                prop["space_id"]=dt["space_id"]
                
            if dt["type"]:
                dt["type"]["space_id"]=dt["space_id"]
                for prop2 in dt["type"]["properties"]:
                    prop2["space_id"] = dt["space_id"]
        return ObjectSchema(**orig)
        
    """
    Get list to retrieve views for.
    Limited to types: ['collection', 'set']
    """
    def getLists(self, name: str, offset:int=0, limit:int=1000) -> ListSchema:
        body=SearchCondition(query=name, sort=SearchSort(direction="asc", property_key="last_modified_date"), types=['collection', 'set'])
        orig = self._endpoint.search_space(space_id=self.id, body=body, offset=offset, limit=limit)
        for dt in orig["data"]:
            for prop in dt["properties"]:
                prop["space_id"]=dt["space_id"]
                
            if dt["type"]:
                dt["type"]["space_id"]=dt["space_id"]
                for prop2 in dt["type"]["properties"]:
                    prop2["space_id"] = dt["space_id"]
        return ListSchema(**orig)
        
    """
    Returns a paginated list of members belonging to the specified space. 
    Each member record includes the member’s profile ID, name, icon (which may be derived from an emoji or image), 
      network identity, global name, status (e.g. joining, active) and role (e.g. Viewer, Editor, Owner). 
    This endpoint supports collaborative features by allowing clients to show who is in a space and manage 
    access rights.
    """
    def listMembers(self, offset:int=0, limit:int=100) -> MemberSchema:
        orig = self._endpoint.list_members(space_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"]=self.id
        return MemberSchema(**orig)
        
    """
    Fetches detailed information about a single member within a space. 
    The endpoint returns the member’s identifier, name, icon, identity, global name, status and role. 
    The member_id path parameter can be provided as either the member's ID (starting with _participant) 
      or the member's identity. This is useful for user profile pages, permission management, and displaying 
      member-specific information in collaborative environments.
    """
    def getMember(self, member_id: str) -> Member:
        orig = self._endpoint.get_member(space_id=self.id, member_id=member_id)
        orig["space_id"] = self.id
        return Member(**orig)
        
    """
    ⚠ Warning: Properties are experimental and may change in the next update. ⚠ 
    Retrieves a paginated list of properties available within a specific space. 
    Each property record includes its unique identifier, name and format. 
    This information is essential for clients to understand the available properties for filtering or 
      creating objects.
    """
    def listProperties(self, offset:int=0, limit:int=100) -> PropertySchema:
        orig = self._endpoint.list_properties(space_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"]=self.id
        return PropertySchema(**orig)
        
    """
    get all properties in one list
    """
    def getAllProperties(self) -> list[Property]:
        has_more=True
        resultProps=[]
        offset=0
        limit=10
        while has_more:
            offset_Props=self.listProperties(offset=offset, limit=limit)
            resultProps.extend(offset_Props.data)
            has_more=offset_Props.pagination.has_more
            offset += limit
        
        return resultProps
        
    """
    Warning: Properties are experimental and may change in the next update. ⚠ 
    Fetches detailed information about one specific property by its ID. 
    This includes the property’s unique identifier, name and format. 
    This detailed view assists clients in showing property options to users and in guiding the user 
      interface (such as displaying appropriate input fields or selection options).
    """
    def getProperty(self, property_id:str) -> Property:
        orig = self._endpoint.get_property(space_id=self.id, property_id=property_id)
        orig["space_id"]=self.id
        return Property(**orig)
        
    """
    ⚠ Warning: Properties are experimental and may change in the next update. ⚠ 
    Creates a new property in the specified space using a JSON payload. 
    The creation process is subject to rate limiting. 
    The payload must include property details such as the name and format. 
    The endpoint then returns the full property data, ready for further interactions.
    """
    def createProperty(self, body:PropertyCreate) -> Property:
        orig = self._endpoint.create_property(space_id=self.id, prop=body)
        orig["space_id"]=self.id
        return Property(**orig)
        
    """
    ⚠ Warning: Properties are experimental and may change in the next update. ⚠ 
    This endpoint updates an existing property in the specified space using a JSON payload. 
    The update process is subject to rate limiting. The payload must include the name to be updated. 
    The endpoint then returns the full property data, ready for further interactions.
    """
    def updateProperty(self, property_id: str, body:PropertyUpdate) -> Property:
        orig = self._endpoint.update_property(space_id=self.id, property_id=property_id, prop=body)
        orig["space_id"]=self.id
        return Property(**orig)
        
    """
    ⚠ Warning: Properties are experimental and may change in the next update. ⚠ 
    This endpoint “deletes” a property by marking it as archived. 
    The deletion process is performed safely and is subject to rate limiting. 
    It returns the property’s details after it has been archived. 
    Proper error handling is in place for situations such as when the property isn’t found or the 
      deletion cannot be performed because of permission issues.
    """
    def deleteProperty(self, property_id: str) -> Property:
        orig = self._endpoint.delete_property(space_id=self.id, property_id=property_id)
        orig["space_id"]=self.id
        return Property(**orig)
    
    """
    Retrieves a paginated list of objects in the given space. 
    The endpoint takes query parameters for pagination (offset and limit) and returns detailed data about 
      each object including its ID, name, icon, type information, a snippet of the content (if applicable), 
      layout, space ID, blocks and details. It is intended for building views where users can see all objects in 
      a space at a glance.
    """
    def listObjects(self, offset:int=0, limit:int=100) -> ObjectSchema:
        orig = self._endpoint.list_objects(space_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"]=self.id
            if dt["type"]:
                dt["type"]["space_id"]=self.id
                if dt["type"]["properties"]:
                    for prop in dt["type"]["properties"]:
                        prop["space_id"]=self.id
            for prop2 in dt["properties"]:
                prop2["space_id"]=self.id
        return ObjectSchema(**orig)
        
    """
    Fetches the full details of a single object identified by the object ID within the specified space. 
    The response includes not only basic metadata (ID, name, icon, type) but also the complete set of blocks 
      (which may include text, files, properties and dataviews) and extra details (such as timestamps and 
      linked member information). 
    This endpoint is essential when a client needs to render or edit the full object view.
    """
    def getObject(self, object_id:str) -> Object:
        orig = self._endpoint.get_object(space_id=self.id, object_id=object_id)
        orig["space_id"] = self.id
        if orig["type"]:
            orig["type"]["space_id"]=self.id
            if orig["type"]["properties"]:
                for prop in orig["type"]["properties"]:
                    prop["space_id"] = self.id
        return Object(**orig)
        
    """
    Creates a new object in the specified space using a JSON payload. 
    The creation process is subject to rate limiting. 
    The payload must include key details such as the object name, icon, description, body content (which may support Markdown), 
      source URL (required for bookmark objects), template identifier, and the type_key (which is the non-unique identifier of 
      the type of object to create). Post-creation, additional operations (like setting featured properties or fetching bookmark 
      metadata) may occur. 
    The endpoint then returns the full object data, ready for further interactions.
    """
    def createObject(self, body: ObjectCreate) -> Object:
        # Check Parameter Valid
        tp=self.getTypeByKey(body.type_key)
        if tp:
            # get Properties
            all_props={p.key: p for p in tp.properties}
            if body.properties:
                for prop in body.properties:
                    prop_obj=all_props.get(prop.key)
                    if prop_obj:
                        # set id for value ## Select
                        if prop_obj.format == "select":
                            # get Tag
                            if prop.select:
                                prop.select = prop_obj.getOrCreateTagByName(prop.select).id
                        elif prop_obj.format == "multi_select":
                            for i in range(len(prop.multi_select)):
                                # get Tag
                                if prop.multi_select[i]:
                                    prop.multi_select[i] = prop_obj.getOrCreateTagByName(prop.multi_select[i]).id
                        elif prop_obj.format == "objects":
                            for i in range(len(prop.objects)):
                                obj=self.getObject(object_id=prop.objects[i])
                                if obj:
                                    pass
                                else:
                                    raise RuntimeError(f"object id {prop.objects[i]} is invalid")
                    else:
                        raise RuntimeError(f"property key {prop.key} does not exist in type {tp.key}")
        else:
            raise RuntimeError("can not find Type by key:" + body.type_key)
        
        orig = self._endpoint.create_object(space_id=self.id, obj=body)
        orig["space_id"]=self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        if orig["type"]:
            orig["type"]["space_id"]=self.id
            if orig["type"]["properties"]:
                for prop2 in orig["type"]["properties"]:
                    prop2["space_id"]=self.id
        return Object(**orig)
        
    """
    This endpoint “deletes” an object by marking it as archived. 
    The deletion process is performed safely and is subject to rate limiting. 
    It returns the object’s details after it has been archived. 
    Proper error handling is in place for situations such as when the object isn’t found or 
      the deletion cannot be performed because of permission issues.
    """
    def deleteObject(self, object_id: str) -> Object:
        orig = self._endpoint.delete_object(space_id=self.id, object_id=object_id)
        orig["space_id"]=self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        if orig["type"]:
            orig["type"]["space_id"]=self.id
            if orig["type"]["properties"]:
                for prop2 in orig["type"]["properties"]:
                    prop2["space_id"]=self.id
        return Object(**orig)
        
    """
    This endpoint updates an existing object in the specified space using a JSON payload. 
    The update process is subject to rate limiting. 
    The payload must include the details to be updated. 
    The endpoint then returns the full object data, ready for further interactions.
    """
    def updateObject(self, object_id: str, obj: ObjectUpdate) -> Object:
        orig = self._endpoint.update_object(space_id=self.id, object_id=object_id, obj=obj)
        orig["space_id"]=self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        if orig["type"]:
            orig["type"]["space_id"]=self.id
            if orig["type"]["properties"]:
                for prop2 in orig["type"]["properties"]:
                    prop2["space_id"]=self.id
        return Object(**orig)
        
    """
    This endpoint retrieves a paginated list of types (e.g. 'Page', 'Note', 'Task') available within the 
      specified space. 
    Each type’s record includes its unique identifier, type key, display name, icon, and layout. While a type's id 
      is truly unique, a type's key can be the same across spaces for known types, e.g. 'page' for 'Page'. 
    Clients use this information when offering choices for object creation or for filtering objects by 
    type through search.
    """
    def listTypes(self, offset:int=0, limit:int=100) -> TypeSchema:
        orig = self._endpoint.list_types(space_id=self.id, offset=offset, limit=limit)
        for dt in orig["data"]:
            dt["space_id"] = self.id
            if dt["properties"]:
                for prop in dt["properties"]:
                    prop["space_id"]=self.id
        return TypeSchema(**orig)
        
    """
    Fetches detailed information about one specific type by its ID. 
    This includes the type’s unique key, name, icon, and layout. 
    This detailed view assists clients in understanding the expected structure and style for objects of that 
      type and in guiding the user interface (such as displaying appropriate icons or layout hints).
    """
    def getType(self, type_id:str) -> Type:
        orig = self._endpoint.get_type(space_id=self.id, type_id=type_id)
        orig["space_id"] = self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        return Type(**orig)
        
    """
    Fetches detaild information about one specific type by its Key.
    """
    def getTypeByKey(self, key: str) -> Type:
        has_more=True
        offset=0
        limit=100
        while has_more:
            all_types=self.listTypes(offset=offset, limit=limit)
            for tp in all_types.data:
                if tp.key == key:
                    return tp
            has_more=all_types.pagination.has_more
            offset += limit
        return {}
    """
    Fetches first detaild informatino about one specific type by its NAME
    This includes the type’s unique key, name, icon, and layout. 
    This detailed view assists clients in understanding the expected structure and style for objects of that 
      type and in guiding the user interface (such as displaying appropriate icons or layout hints).
    """
    def getTypeByName(self, name: str) -> Type:
        offset=0
        limit=100
        has_more=True
        
        while has_more:
            all_types=self.listTypes(offset=offset,limit=limit)
            for tp in all_types.data:
                if tp.name == name:
                    return tp
            has_more=all_types.pagination.has_more
            offset += limit
        return {}
        
    """
    Creates a new type in the specified space using a JSON payload. 
    The creation process is subject to rate limiting. 
    The payload must include type details such as the name, icon, and layout. 
    The endpoint then returns the full type data, ready to be used for creating objects.
    """
    def createType(self, body: TypeCreate) -> Type:
        orig = self._endpoint.create_type(space_id=self.id, type=body)
        orig["space_id"]=self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        return Type(**orig)
        
    """
    This endpoint “deletes” an type by marking it as archived. 
    The deletion process is performed safely and is subject to rate limiting. 
    It returns the type’s details after it has been archived. 
    Proper error handling is in place for situations such as when the type isn’t found or 
      the deletion cannot be performed because of permission issues.
    """
    def deleteType(self, type_id:str) -> Type:
        orig = self._endpoint.delete_type(space_id=self.id, type_id=type_id)
        orig["space_id"]=self.id
        for prop in orig["properties"]:
            prop["space_id"]=self.id
        return Type(**orig)
    
class SpaceSchema(Schema):
    data:list[Space]
    