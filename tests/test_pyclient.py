import sys
from pathlib import Path
# 方法2：跨平台兼容（推荐）
sys.path.append(Path(__file__).parent.parent.as_posix())

from anytype import (Anytype, 
                     Space, 
                     Object, 
                     Type, 
                     EmojiIcon,
                     NamedIcon, 
                     SpaceCreate, 
                     SpaceUpdate, 
                     ObjectSchema, 
                     SearchCondition, 
                     SearchSort,
                     ObjectCreate,
                     ObjectUpdate,
                     Property,
                     TextProp,
                     NumberProp,
                     SelectProp,
                     MultiSelectProp,
                     DateProp,
                     FilesProp,
                     CheckboxProp,
                     URLProp,
                     EmailProp,
                     PhoneProp,
                     ObjectsProp,
                     PropertyCreate,
                     PropertyUpdate,
                     PropertyCreate,
                     PropertyUpdate,
                     TagCreate,
                     Tag,
                     TagUpdate,
                     TypeCreate,
                     TypeUpdate
                     )
import random
import string

##########################################
#                utils                   #
##########################################
def get_random_letter(length: int) -> str:
    letter=""
    for i in range(length):
        letter += random.choice(string.ascii_letters)
    return letter

def get_random_num() -> int:
    return random.randint(0, 9)

def get_random_desc() -> str:
    names = ["This is a object created by anytype api", 
            "Anytype api created this object", 
            "This object is create by anytype api"
            ]
    return random.choice(names)

def get_random_emoji() -> str:
    emojis=["😁", "📝", "😈"]
    
    return random.choice(emojis)

def test_anytype():
    # Create new Space
    spaceBody=SpaceCreate(description=get_random_desc(),name=get_random_letter(10))
    myAny = Anytype()
    newSpace = myAny.createSpace(spaceBody)
    assert newSpace is not None, "space create failed."
    print("End #Create new Space")
    # list spaces
    allSpaces = myAny.listSpaces()
    assert len(allSpaces.data) > 0,  "space list failed."
    print("End #list spaces")
    # get Space
    mySpace=myAny.getSpace(space_id=newSpace.id)
    assert mySpace is not None,  "space get failed."
    print("End #get Space")
    # update space
    updBody=SpaceUpdate(description=get_random_desc(),name="APIspace"+get_random_letter(5))
    updatedSpace=myAny.updateSpace(space_id=newSpace.id, space=updBody)
    assert updatedSpace is not None,  "space update failed."
    print("End #update space")
    # listMembers
    all_members=mySpace.listMembers()
    assert len(all_members.data) > 0,  "member list failed."
    print("End #listMembers")
    # getmember
    myMember=mySpace.getMember(member_id=all_members.data[0].id)
    assert myMember is not None, "member get failed."
    print("End #getmember")
    # listProperties
    all_props=mySpace.listProperties()
    assert len(all_props.data) > 0, "property list failed."
    print("End #listProperties")
    # get property
    myProp=mySpace.getProperty(property_id=all_props.data[0].id)
    assert myProp is not None, "property get failed."
    print("End #get property")
    # create property
    propBody=PropertyCreate(format="text",key="age",name="Age")
    newProp=mySpace.createProperty(body=propBody)
    assert newProp is not None,  "property create failed."
    print("End #create property")
    # update property
    updPropBody=PropertyUpdate(name="Age1")
    updProp=mySpace.updateProperty(property_id=newProp.id,body=updPropBody)
    assert updProp is not None, "property update failed."
    print("End #update property")
    
    # delete property
    deletedProp=mySpace.deleteProperty(property_id=updProp.id)
    assert deletedProp is not None, "property delete failed."
    print("End #delete property")
    
    # list objects
    all_objs=mySpace.listObjects()
    assert len(all_objs.data) > 0, "object list failed."
    print("End #list objects")
    # get object
    myObj=mySpace.getObject(object_id=all_objs.data[0].id)
    assert myObj is not None, "object get failed."
    
    # list types
    all_types=mySpace.listTypes()
    assert len(all_types.data) > 0, "type list failed."
    print("End #list types")
    # get type
    myType=mySpace.getType(type_id=all_types.data[0].id)
    assert myType is not None,  "type get failed."
    print("End #get type")
    # get type by name
    pageType=mySpace.getTypeByName(name="Page")
    assert pageType is not None,  "type get by name failed."
    print("End #get type by name")
    # create type
    typeBody=TypeCreate(icon=EmojiIcon(emoji="📝"),
                        key="test_type",
                        layout="basic",
                        name="TestType",
                        plural_name="TestType",
                        properties=[PropertyCreate(format="text", key="prop_text", name="PropText"),
                                    PropertyCreate(format="number", key="prop_number", name="PropNumber"),
                                    PropertyCreate(format="select", key="prop_select", name="PropSelect"),
                                    PropertyCreate(format="multi_select", key="prop_multi_select", name="PropMultiSelect"),
                                    PropertyCreate(format="date", key="prop_date", name="PropDate"),
                                    PropertyCreate(format="files", key="prop_files", name="PropFiles"),
                                    PropertyCreate(format="checkbox", key="prop_checkbox", name="PropCheckbox"),
                                    PropertyCreate(format="url", key="prop_url", name="PropUrl"),
                                    PropertyCreate(format="email", key="prop_email", name="PropEmail"),
                                    PropertyCreate(format="phone", key="prop_phone", name="PropPhone"),
                                    PropertyCreate(format="objects", key="prop_objects", name="PropObjects")
                                    ])
    newType=mySpace.createType(body=typeBody)
    assert newType is not None,  "type create failed."
    print("End #create type")
    
    # create object(page)
    objBody=ObjectCreate(body="textAAAA", 
                         icon=EmojiIcon(emoji="📝"),
                         name="obj_" + get_random_letter(10),
                         properties=[TextProp(key="prop_text", text="nameOk"),
                                     NumberProp(key="prop_number", number=100),
                                     SelectProp(key="prop_select", select="no1"),
                                     MultiSelectProp(key="prop_multi_select", multi_select=["ok1","ok2"]),
                                     DateProp(key="prop_date", date="2025-10-13T12:34:56Z"),
                                     CheckboxProp(key="prop_checkbox", checkbox=True),
                                     URLProp(key="prop_url", url="www.baidu.com"),
                                     EmailProp(key="prop_email", email="abc@gmail.com"),
                                     PhoneProp(key="prop_phone", phone="+811235489")
                                    ],
                         type_key="test_type"
                         )
    # ·add text to body
    objBody.addHeader(1,get_random_letter(10))
    objBody.addHeader(2,get_random_letter(10))
    objBody.addHeader(3,get_random_letter(10))
    objBody.addDotListBlock()
    objBody.addText(get_random_letter(10))
    objBody.addSplitLine()
    objBody.addCheckbox(get_random_letter(5), False)
    objBody.addCodeblock("python", "y=x+1")
    newObj=mySpace.createObject(body=objBody)
    assert newObj is not None,  "object create failed."
    print("End #create object(page)")
    
    # update object
    updObj=ObjectUpdate(icon=EmojiIcon(emoji=get_random_emoji()))
    updatedObj=mySpace.updateObject(object_id=newObj.id,obj=updObj)
    assert updatedObj is not None, "udpate object failed."
    print("End #update object")
    
    # create object(collection)
    objCollect=ObjectCreate(body="", 
                         icon=EmojiIcon(emoji=get_random_emoji()),
                         name="collect_" + get_random_letter(10),
                         type_key="collection"
                         )
    newCollect=mySpace.createObject(body=objCollect)
    assert newCollect is not None,  "collection create failed."
    print("End #create object(collection)")
    # list objects
    all_objs=mySpace.listObjects()
    assert len(all_objs.data) > 0, "list objects failed."
    print("End #list objects")
    # get object
    specific_obj=mySpace.getObject(object_id=all_objs.data[0].id)
    assert specific_obj is not None, "get object failed."
    print("End #get object")
    
    # getLists
    all_lists=mySpace.getLists(name="collect")
    assert len(all_lists.data) > 0, "get lists failed."
    print("End #getLists")
    
    # add obj to list
    myList=all_lists.data[0]
    objIds=[newObj.id]
    result=myList.addObjects(objectIds=objIds)
    print(result)
    print("End #add obj to list")
    # getListViews
    all_views=myList.getViews()
    assert len(all_views.data) > 0, "list views failed."
    print("End #getListViews")
    # get objects in view
    myView=all_views.data[0]
    list_objs=myView.getObjects()
    assert len(list_objs.data) > 0, "ilst view objects faild."
    print("End #get objects in view")
    
    # create tag
    tagBody=TagCreate(color="yellow",name="initial")
    newTag=myProp.createTag(tag=tagBody)
    assert newTag is not None, "create tag failed."
    print("End #create tag")
    # list tags
    all_tags=myProp.listTags()
    assert len(all_tags.data) > 0, "list tags failed"
    print("End #list tags")
    # get tag
    myTag = myProp.getTag(tag_id=newTag.id)
    assert myTag is not None, "get tag failed."
    print("End #get tags")
    # update tag
    updBody=TagUpdate(color="orange")
    updTag = myProp.updateTag(tag_id=myTag.id, tag=updBody)
    assert updTag is not None, "update tag failed."
    print("End #update tag")
    # delete tag
    deletedTag=myProp.deleteTag(tag_id=myTag.id)
    assert deletedTag is not None, "delete tag failed."
    print("End #delete tag")
    # remove obj from list
    result=myList.removeObject(object_id=newObj.id)
    print(result)
    print("End #remove obj from list")
    # search space
    cond=SearchCondition(query="collect",sort=SearchSort(direction="asc", property_key="name"),types=["page", "note", "set", "collection"])
    glbObjs=mySpace.searchSpace(body=cond)
    assert len(glbObjs.data) > 0 , "search space failed."
    print("End #search space")
    # search global
    cond=SearchCondition(query="collect",sort=SearchSort(direction="asc", property_key="name"),types=["page", "note", "set", "collection"])
    glbObjs=myAny.searchGlobal(body=cond)
    assert len(glbObjs.data) > 0,  "search global failed."
    print("End #search global")
    # delete object
    deletedObj=mySpace.deleteObject(object_id=newObj.id)
    assert deletedObj is not None, "object delete failed."
    print("End #delete object")
    # delete type
    deletedType=mySpace.deleteType(type_id=newType.id)
    assert deletedType is not None, "type delete failed."
    print("End #delete type")
    
if __name__ == "__main__":
    test_anytype()
