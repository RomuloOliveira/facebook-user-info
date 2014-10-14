Person
======

Person REST Resource basic documentation

## Actions
- [POST /person](#post-person)
- [GET /person](#get-personlimitlimit)
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
  

## GET /person?limit=:limit

Lists *limit* registered users

### Request

### Response


## DELETE /person/:id

Deletes a user where user.id=:id

### Request

### Response

