Person
======

Person REST Resource basic documentation

## Actions
- [Adding an user](#adding-an-user)
- [Listing users](#listing-users)
- [Deleting a registered](#deleting-a-registered-user)

## Adding an user

### POST /person

Register a new user.  
The system retrieves information about the user using a *facebook_id* and stores it in the database.  
  
Information retrieved:
- Facebook id
- Name
- Username
- Gender

#### Request

**Parameters**:

| Parameter       | Type   | Description      |
| --------------- | ------ | ---------------- |
| **facebook_id** | string | Facebook user id |

**Content-type**: `multipart/form-data`  
**Example request**:  
```bash
curl -X POST -F facebook_id=100007710667474 http://localhost:xxxx/person
```

#### Response

**Content-type**: text/plain  
**HTTP Status Code**: 201 (Created)  

## Listing users

### GET /person?limit=

Lists *limit* registered users information

#### Request

**Parameters**:

| Parameter       | Type    | Description                             |
| --------------- | ------- | --------------------------------------- |
| **limit**       | integer | Number of users to retrieve information |


**Example request**:  

```bash
curl http://localhost:xxxx/person/?limit=xxx
```

#### Response

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

## Deleting a registered user

### DELETE /person/:id

Deletes a user where user.id=:id

#### Request

**Parameters**:

| Parameter | Type   | Description      |
| --------- | ------ | ---------------- |
| **id**    | string | Facebook user id |


**Example request**:  
```bash
curl -X DELETE http://localhost:xxxx/person/100007710667474
```

#### Response

**HTTP Status Code**: 204 (No Content)  

## Remarks

Requests that contains invalid parameters or content-type receives 400 (Bad Request) as HTTP Status Code

