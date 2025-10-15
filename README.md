# Welcome to Anytype PyClient

## Features

- **Authentication**: use ApiKey to auth locally
- **Spaces**: create or update spaces
- **Objects**: crud for objects
- **Search**: search space or global
- **Types**: crud for types
- **Views**: manage list(query, collection) views
- **Members**: retrive members
- **Properties**: CRUD for properties
- **Tags**: CRUD for tags
- **Templates**: retrive templates

## QuickStart

when published

```python
pip install anytype-pyclient
```

### Examples
1. Space
```python
from anytype import (Anytype, Space, Object, Type, EmojiIcon)
myAny = Anytype()
#create space
spaceBody=SpaceCreate(description=get_random_desc(),name=get_random_letter(10))
newSpace = myAny.createSpace(spaceBody)
#list spaces
allSpaces = myAny.listSpaces()
```
2. Type
```python
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
```
3. Object
```python
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
objBody.addHeader(1,"Title")
objBody.addHeader(2, "Header")
objBody.addHeader(3, "SubHeader")
objBody.addDotListBlock()
objBody.addText("textfsgre")
objBody.addSplitLine()
objBody.addCheckbox("done", False)
objBody.addCodeblock("python", "y=x+1")
newObj=mySpace.createObject(body=objBody)
```

### Configure
```
**ANYTYPE_API_KEY=<api_key>**
```