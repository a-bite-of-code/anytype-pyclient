from typing import TypeVar, Optional, Any, Literal, Union, Annotated
from pydantic import BaseModel, root_validator, Field
from .constants import SortProperty, SortDirection, IconFormat
from .api import AnytypePyClient

class ApiBase1(BaseModel):
    _endpoint: AnytypePyClient =AnytypePyClient()

class ApiBase(ApiBase1):
    space_id: str

class Icon(BaseModel):
    format: str
    emoji: Optional[str]=""
    file: Optional[str]=""
    color: Optional[str]=""
    name: Optional[str]=""
    
    @root_validator(pre=True)
    def check_key(cls, values):
        format = values.get("format")
        if format not in IconFormat:
            raise ValueError("format should in [" + ','.join(IconFormat) + "]")
        return values
        
class EmojiIcon(BaseModel):
    format: Literal["emoji"] = "emoji"
    emoji: str
    
class FileIcon(BaseModel):
    format: Literal["file"] = "file"
    file:str
    
class NamedIcon(BaseModel):
    format: Literal["icon"] = "icon"
    color:str
    name:str
    
    
Icon_Bound = Annotated[Union[EmojiIcon, FileIcon, NamedIcon], Field(discriminator="format")]

class PropertyValue(BaseModel):
    id:str
    key:str
    name:str
    object:str
    
class TextPropertyValue(PropertyValue):
    format:Literal["text"] = "text"
    text:str
    
class NumberPropertyValue(PropertyValue):
    format:Literal["number"] = "number"
    number:int
    
    
class TagSelect(BaseModel):
    color:str
    id:str
    key:str
    name:str
    object:str
    
class SelectPropertyValue(PropertyValue):
    format:Literal["select"] = "select"
    select: Optional[TagSelect] = None
    
class MultiSelectSingleValue(BaseModel):
    color:str
    id:str
    key:str
    name:str
    object:str
    
class MultiSelectPropertyValue(PropertyValue):
    format:Literal["multi_select"] = "multi_select"
    multi_select: Optional[list[MultiSelectSingleValue]] = None
    
class DatePropertyValue(PropertyValue):
    format:Literal["date"] = "date"
    date:Optional[str]=None
    
class FilesPropertyValue(PropertyValue):
    format:Literal["files"] = "files"
    files:Optional[list[str]]=None
    
class CheckboxPropertyValue(PropertyValue):
    format:Literal["checkbox"] = "checkbox"
    checkbox:bool = False
    
class URLPropertyValue(PropertyValue):
    format:Literal["url"] = "url"
    url:Optional[str]=None
    
class EmailPropertyValue(PropertyValue):
    format:Literal["email"] = "email"
    email:Optional[str]=None
    
class PhonePropertyValue(PropertyValue):
    format:Literal["phone"] = "phone"
    phone:Optional[str]=None
    
class ObjectsPropertyValue(PropertyValue):
    format:Literal["objects"] = "objects"
    objects:Optional[list[str]]=None

PropertyValue_Bound = Annotated[Union[TextPropertyValue, NumberPropertyValue, SelectPropertyValue, MultiSelectPropertyValue, DatePropertyValue, FilesPropertyValue, CheckboxPropertyValue, URLPropertyValue, EmailPropertyValue, PhonePropertyValue, ObjectsPropertyValue], Field(discriminator="format")]

class PropertyCreate(BaseModel):
    format:str
    key:Optional[str] = None
    name:str
    
class PropertyUpdate(BaseModel):
    key:Optional[str] = None
    name:Optional[str] = None
    
class SpaceCreate(BaseModel):
    description:Optional[str] = None
    name:str
    
class SpaceUpdate(BaseModel):
    description:Optional[str] = None
    name:Optional[str] = None
    
class TagCreate(BaseModel):
    color:Optional[str] = None
    name:Optional[str] = None
    
class TagUpdate(TagCreate):
    pass
    
class TypeCreate(BaseModel):
    icon: Optional[Icon_Bound] = None
    key:Optional[str] = None
    layout:str
    name:str
    plural_name:str
    properties:Optional[list[PropertyCreate]] = None
    
class TypeUpdate(BaseModel):
    icon: Optional[Icon_Bound] = None
    key:Optional[str] = None
    layout:Optional[str] = None
    name:Optional[str] = None
    plural_name:Optional[str] = None
    properties:Optional[list[PropertyCreate]] = []
    
# The Pagination
class Pagination(BaseModel):
    has_more: bool
    limit: int
    offset: int
    total: int
    
class SearchSort(BaseModel):
    direction:str
    property_key:str
    
    @root_validator(pre=True)
    def check_key(cls, values):
        dire, key=values.get("direction"), values.get("property_key")
        if key not in SortProperty:
            raise ValueError("property_key should in [" + ','.join(SortProperty) + "]")
        if dire not in SortDirection:
            raise ValueError("direction should in [" + ",".join(SortDirection) + "]")
        return values
    
# The search parameters used to filter and sort the results
class SearchCondition(BaseModel):
    query: str
    sort: SearchSort
    types: list[str]

class Schema(BaseModel):
    data:Any
    pagination: Pagination
    
class Filter(BaseModel):
    condition:str
    format:str
    id:str
    property_key:str
    value:str
    
class Sort(BaseModel):
    format:str
    id:str
    property_key:str
    sort_type:str
