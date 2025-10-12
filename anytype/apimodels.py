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
    
    
class SelectPropertyValue(PropertyValue):
    format:Literal["select"] = "select"
    select: str
    
class MultiSelectSingleValue(BaseModel):
    color:str
    id:str
    key:str
    name:str
    object:str
    
class MultiSelectPropertyValue(PropertyValue):
    format:Literal["multi_select"] = "multi_select"
    multi_select: list[MultiSelectSingleValue]
    
class DatePropertyValue(PropertyValue):
    format:Literal["date"] = "date"
    date:str
    
class FilesPropertyValue(PropertyValue):
    format:Literal["files"] = "files"
    files:list[str]
    
class CheckboxPropertyValue(PropertyValue):
    format:Literal["checkbox"] = "checkbox"
    checkbox:bool
    
class URLPropertyValue(PropertyValue):
    format:Literal["url"] = "url"
    url:str
    
class EmailPropertyValue(PropertyValue):
    format:str = "email"
    email:str
    
class PhonePropertyValue(PropertyValue):
    format:Literal["phone"] = "phone"
    phone:str
    
class ObjectsPropertyValue(PropertyValue):
    format:Literal["objects"] = "objects"
    objects:list[str]

PropertyValue_Bound = Annotated[Union[TextPropertyValue, NumberPropertyValue, SelectPropertyValue, MultiSelectPropertyValue, DatePropertyValue, FilesPropertyValue, CheckboxPropertyValue, URLPropertyValue, EmailPropertyValue, PhonePropertyValue, ObjectsPropertyValue], Field(discriminator="format")]

class PropertyCreate(BaseModel):
    format:str
    key:Optional[str] = None
    name:str
    
class PropertyUpdate(BaseModel):
    key:Optional[str] = None
    name:str
    
class PropertyLinkValue(BaseModel):
    key:str
    
class TextPropertyLinkValue(PropertyLinkValue):
    text:str
    
class NumberPropertyLinkValue(PropertyLinkValue):
    number:int
    
class SelectPropertyLinkValue(PropertyLinkValue):
    select:str
    
class MultiSelectPropertyLinkValue(PropertyLinkValue):
    multi_select:list[str]
    
class DatePropertyLinkValue(PropertyLinkValue):
    date:str
    
class FilesPropertyLinkValue(PropertyLinkValue):
    files:list[str]
    
class CheckboxPropertyLinkValue(PropertyLinkValue):
    checkbox:bool
    
class URLPropertyLinkValue(PropertyLinkValue):
    url:str
    
class EmailPropertyLinkValue(PropertyLinkValue):
    email:str
    
class PhonePropertyLinkValue(PropertyLinkValue):
    phone:str
    
class ObjectsPropertyLinkValue(PropertyLinkValue):
    objects:list[str]
    
PropertyLinkValue_Bound = TypeVar("PropertyLinkValue_Bound", bound=PropertyLinkValue)

class ObjectCreate(BaseModel):
    body:Optional[str] = None
    icon:Optional[Icon_Bound] = None
    name:Optional[str] = None
    properties:Optional[list[PropertyLinkValue_Bound]] = None
    template_id:Optional[str] = None
    type_key:str
    
    def addText(self, text:str) -> None:
        
        self.body += f"{text}\n"
        
    def addHeader(self, level:int, text:str) -> None:
        if level not in (1, 2, 3):
            raise RuntimeError("level should be 1, 2 or 3")
        self.body += f"{'#' * level} {text}\n"
        
    def addDotListBlock(self) -> None:
        self.body += f"\n+ "
        
    def addSplitLine(self) -> None:
        self.body += f"\n---"
        
    def addDotSplitLine(self) -> None:
        self.body += f"\n***"
        
    def addNumListBlock(self) -> None:
        self.body += f"\n1. "
        
    def addCheckbox(self, text:str, checked:bool=False) -> None:
        self.body += f"- [x] {text}\n" if checked else f"- [ ] {text}\n"
        
    def addBullet(self, text:str) -> None:
        self.body += f"- {text}\n"
        
    def addCodeblock(self, language:str, code:str) -> None:
        self.body += f"``` {language}\n{code}\n```\n"
        
    def add_image(self, image_url: str, alt: str = "", title: str = "") -> None:
        if title:
            self.body += f'![{alt}]({image_url} "{title}")\n'
        else:
            self.body += f"![{alt}]({image_url})\n"
            
    def addCodeInline(self, code:str) -> None:
        self.body += f"**{code}**"
        
    def addBoldInline(self, text:str) -> None:
        self.body += f"`{text}`"
        
    def addSlashInline(self, text:str) -> None:
        self.body += f"*{text}*"
        
    def addDeleteInline(self, text:str) -> None:
        self.body += f"~~{text}~~"
        
    def addRightArrowInline(self, text:str) -> None:
        self.body += f"-->"
        
    def addLeftArrowInline(self, text:str) -> None:
        self.body += f"<--"
        
    def addDoubleArrowInline(self, text:str) -> None:
        self.body += f"<-->"
        
    def addShortLeftArrowInline(self, text:str) -> None:
        self.body += f"<-"
        
    def addShortRightArrowInline(self, text:str) -> None:
        self.body += f"->"
        
    def addLongDashInline(self, text:str) -> None:
        self.body += f"--"
        
    def addCopyrightInline(self, text:str) -> None:
        self.body += f"(c)"
        
    def addRegisterInline(self, text:str) -> None:
        self.body += f"(r)"
        
    def addTrademarkInline(self, text:str) -> None:
        self.body += f"(tm)"
        
    def addDotsInline(self, text:str) -> None:
        self.body += f"..."
        
class ObjectUpdate(BaseModel):
    icon: Optional[Icon_Bound] = None
    name: str
    properties: Optional[list[PropertyLinkValue_Bound]] = None
    
class SpaceCreate(BaseModel):
    description:Optional[str] = None
    name:str
    
class SpaceUpdate(BaseModel):
    description:Optional[str] = None
    name:Optional[str] = None
    
class TagCreate(BaseModel):
    color:str
    name:str
    
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
    