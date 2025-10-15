from typing import Optional
from .apimodels import Schema, ApiBase, Icon_Bound


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
    