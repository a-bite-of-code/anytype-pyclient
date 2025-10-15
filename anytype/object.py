from pydantic import BaseModel
from typing import Optional, TypeVar
from .apimodels import Schema, PropertyValue_Bound, ApiBase, Icon_Bound
from .type import Type

class PropertyLinkValue(BaseModel):
    key:str
    
class TextProp(PropertyLinkValue):
    text:str
    
class NumberProp(PropertyLinkValue):
    number:int
    
class SelectProp(PropertyLinkValue):
    select:str
    
class MultiSelectProp(PropertyLinkValue):
    multi_select:list[str]
    
class DateProp(PropertyLinkValue):
    date:str
    
class FilesProp(PropertyLinkValue):
    files:list[str]
    
class CheckboxProp(PropertyLinkValue):
    checkbox:bool
    
class URLProp(PropertyLinkValue):
    url:str
    
class EmailProp(PropertyLinkValue):
    email:str
    
class PhoneProp(PropertyLinkValue):
    phone:str
    
class ObjectsProp(PropertyLinkValue):
    objects:list[str]
    
PropertyLinkValue_Bound = TypeVar("PropertyLinkValue_Bound", bound=PropertyLinkValue)

class Object(ApiBase):
    list_id: Optional[str] = ""
    
    archived:bool
    icon:Optional[Icon_Bound] = None
    id:str
    layout:str
    markdown:Optional[str] = ""
    name:str
    object:str
    properties:list[PropertyValue_Bound]
    snippet:str
    space_id:str
    type:Optional[Type] = None
    
class ObjectSchema(Schema):
    data:list[Object]
    
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
    name: Optional[str] = None
    properties: Optional[list[PropertyLinkValue_Bound]] = None
    
