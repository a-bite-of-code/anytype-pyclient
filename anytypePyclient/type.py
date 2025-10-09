from pydantic import BaseModel, Field
from typing import TypeVar, Optional
from .apimodels import Icon, Schema
from .api import AnytypePyClient
from .template import Template, TemplateSchema
from .property import Property

Icon_Bound = TypeVar("Icon_Bound", bound=Icon)


class Type(BaseModel):
    _endpoint: AnytypePyClient =AnytypePyClient()
    
    archived: bool
    icon: Optional[Icon_Bound] = None
    id: str
    key: str
    layout: str
    name: str
    object: str
    plural_name: str
    properties: Optional[list[Property]] = None
    
    """
    This endpoint returns a paginated list of templates that are associated with a specific type within a space. 
    Templates provide pre‑configured structures for creating new objects. 
    Each template record contains its identifier, name, and icon, so that clients can offer users a selection 
      of templates when creating objects.
    """
    def listTemplates(self, offset:int=0, limit:int=100) -> TemplateSchema:
        orig = self._endpoint.list_templates(space_id=self.space_id, type_id=self.id, offset=offset, limit=limit)
        return TemplateSchema(**orig)
        
    """
    Fetches full details for one template associated with a particular type in a space. 
    The response provides the template’s identifier, name, icon, and any other relevant metadata. 
    This endpoint is useful when a client needs to preview or apply a template to prefill object creation fields.
    """
    def getTemplate(self, template_id:str) -> Template:
        orig = self._endpoint.get_template(space_id=self.space_id, type_id=self.id)
        return Template(**orig)
        
class TypeSchema(Schema):
    data:list[Type]
    