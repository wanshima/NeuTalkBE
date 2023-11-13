#### 1. Login

**POST /api/login** 

###### request

Content-Type: application/json

```json
{
    "username" : "testuser",
    "password" : "testpassword"
}
```

###### response

fail

```json
{
    "HTTP Code": 401 Unauthorized,
    "msg": "invalid username or password"
}
```

success

```json
{
    "HTTP Code": 200,
    "data": {
        "userId": "12345678",
        "username": "testuser",
    }
}
```

#### 2.Register

**POST /api/register**

###### request

```json
{
    "username" : "testuser",
    "password" : "testpassword"
}
```

###### response

fail (user exists)

```json
{
    "HTTP Code": 409,
    "msg": "this username is already registered"
}
```


#### 3.Logout

**POST /user/logout**

###### request

```
no parameters
```



###### respond

fail

```json
{
    "HTTP Code": 500,
    "msg": "server error"
}
```

success

```json
{
    "HTTP Code": 200,
    "msg": "success"
}
```

#### 4. Create New Post

**POST /api/new** 

###### request

Content-Type: application/json

###### header
Authorization: Token <your-token>

```json
{
    "content": "Content of the new post"
}
```

###### response

fail

```json
{
    "HTTP Code": 400,
    "msg": "Content is required"
}
```

success

```json
{
    "HTTP Code": 200,
    "result": "Content of the new post"
}
```

