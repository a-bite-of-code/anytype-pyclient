from typing import Optional
from .apimodels import Schema, ApiBase, Icon_Bound
from .property import Property


class Type(ApiBase):
    
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
    def listTemplates(self, offset:int=0, limit:int=100) -> "TemplateSchema":
        from .template import TemplateSchema
        orig = self._endpoint.list_templates(space_id=self.space_id, type_id=self.id, offset=offset, limit=limit)
        for dt in orig.data:
            if dt["type"]:
                dt["type"]["space_id"]=self.spaec_id
        return TemplateSchema(**orig)
        
    """
    Fetches full details for one template associated with a particular type in a space. 
    The response provides the template’s identifier, name, icon, and any other relevant metadata. 
    This endpoint is useful when a client needs to preview or apply a template to prefill object creation fields.
    """
    def getTemplate(self, template_id:str) -> "Template":
        from .template import Template
        orig = self._endpoint.get_template(space_id=self.space_id, type_id=self.id)
        return Template(**orig)
        
class TypeSchema(Schema):
    data:list[Type]
    