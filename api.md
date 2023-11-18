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

**POST /api/logout**

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
    "title": "Your title"
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
    "title": "Your title",
    "content": "Content of the new post",
    "author": "<author_id>",
    "created_at": "<creation_timestamp>"
}
```
#### 5. Get Post Detail

**GET /api/posts/<uuid:post_id>/** 
**POST /api/posts/<uuid:post_id>/** 


###### GET request

Content-Type: application/json

###### 

'post_id'


###### headers

Content-Type: application/json
Authorization: Token <your-token>


###### response

fail

```json
{
    "HTTP Code": 404,
}
```

success

```json
{
    "HTTP Code": 200,
    "post": "<post_id>",
    "title": "Post title",
    "content": "Post content",
    "author": "<author_username>",
    "created_at": "<creation_timestamp>"
       
}
```
###### POST request

Content-Type: application/json

###### 

'post_id'


###### headers

Content-Type: application/json
Authorization: Token <your-token>

###### response
fail

```json
{
    "HTTP Code": 400,
    "msg": "Post not found"
}
```

success

```json
{
    "HTTP Code": 201,
    "author": "<author_username>",
    "comment": "Comment content",
      
}
```
#### 6. Threads list

**POST /api/threads/** 


###### request

Content-Type: application/json

###### header
Authorization: Token <your-token>



###### response

fail

```json
{
    "HTTP Code": 400,
    "error": "Author not found"
}
```
fail

```json
{
    "HTTP Code": 201,
    "error": "Invalid start date format"
}
```
fail

```json
{
    "HTTP Code": 400,
    "error": "Invalid end date format"
}
```

success

```json
{
    "HTTP Code": 200,
    "threads": [
        {   
            "post": "<post_id>",
            "title": "<thread_title>",
            "content": "<thread_content>",
            "author": "<author_username>",
            "created_at": "<creation_timestamp>"
        
        },
    ]
}
```