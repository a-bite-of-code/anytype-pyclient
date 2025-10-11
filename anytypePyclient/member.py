from pydantic import BaseModel
from typing import Optional, TypeVar
from .apimodels import Schema, Icon, ApiBase, Icon_Bound


class Member(ApiBase):
    global_name: str
    icon: Optional[Icon_Bound] = None
    id: str
    identity: str
    name: str
    object: str
    role: str
    status: str
    
class MemberSchema(Schema):
    data: list[Member]
    