from typing import Optional
from pydantic import BaseModel
from .property import Property
from .apimodels import Icon

_TEXT_STYLE=("Paragraph", "Header1", "Header2", "Header3", "Header4", "Quote", "Code", "Title", "Checkbox", "Marked", "Numbered", "Toggle", "Description", "Callout")

class File(BaseModel):
    added_at: int
    hash: Optional[str]=""
    mime: Optional[str]=""
    name: Optional[str]=""
    size: Optional[int]=0
    state: Optional[str]=""
    style: Optional[str]=""
    target_object_id: Optional[str]=""
    type: Optional[str]=""
    
class Text(BaseModel):
    checked: Optional[bool] = False
    color: Optional[str]=""
    icon: Optional[Icon]=None
    style: Optional[str]="Paragraph"
    text: Optional[str]=""
    
class Block(BaseModel):
    space_id: str
    
    align: str
    background_color: str
    children_ids: list[str]
    file: File
    id: str
    property: Property
    text: Text
    vertical_align: str
    