Person
======

Person REST Resource basic documentation

## Actions
- [POST /person](#post-person)
- [GET /person](#get-personlimit)
- [DELETE /person](#delete-personid)

## POST /person

Register a new user.  
The system retrieves information about the user using a *facebook_id* and stores it in the database.

### Request

**Parameters**:
- **facebook_id**: integer
  - Facebook user id

**Content-type**: `multipart/form-data`  
**Example**: `curl ­X POST ­F facebook_id=100007710667474 http://localhost:xxxx/person/`

### Response

**Content-type**: text/plain  
**HTTP Status Code**: 201 (Created)  
  

## GET /person?limit=

Lists *limit* registered users information

### Request

**Parameters**:
- **limit**: integer
  - Number of users to retrieve information

**Content-type**: `multipart/form-data`  
**Example**: `curl ­X POST ­F facebook_id=100007710667474 http://localhost:xxxx/person/`

### Response

**Content-type**: application/json  
**HTTP Status Code**: 200 (OK)  
**Example**:  

```JSON
[
  {
    "username": "rpedigoni",
    "facebook_id": "670286562",
    "name": "Renato Pedigoni",
    "gender": "male"
  }
]

```

**REMARKS**: Top level arrays are NOT safe. See http://incompleteness.me/blog/2007/03/05/json-is-not-as-safe-as-people-think-it-is/ and http://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/.


## DELETE /person/:id

Deletes a user where user.id=:id

### Request

### Response

