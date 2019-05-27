# Blogghr

Blogger website with an API Rest

## Installation steps
```bash
> pip install -r requirements.txt
> python manage.py migrate    
> python manage.py createsuperuser
> python manage.py runserver
```

## WEBSITE
| URL | Description |
| --- | --- |
| Users |
| `/login/` | Login the website |
| `/logout/` | Logout from the website |
| `/signup/` | Creation of a new user|
| Blogs |
| `/` | Shows all recently posts  |
| `/blogs/<str:username>` | Shows the posts from a user |
| `/blogs/<str:username>/<int:pk>` | Show detailed information of a post |
| `/new-post/` | Creation of a new post |
    
## ENDPOINTS
| URL | Method | Description | Who|
| --- | --- | --- | --- |
| Users |
|`/apiv1/users/` | GET | Show users | Only admin | 
|`/apiv1/users/` | POST | User creation | Anyone |
|`/apiv1/users/<int:pk>` | GET, PUT, DELETE | User detail, modification and delete | Admin and auth user |    
| Blogs |
|`/apiv1/blogs/` | GET | Show all blogs with urls | Anyone |
|`/apiv1/posts/` | GET | Show all posts | Anyone, but with restrictions |
|`/apiv1/posts/` | POST | Creation of a post | Admin and auth user |
|`/apiv1/posts/<int:pk>` | GET | Show specific post | Anyone |
|`/apiv1/posts/<int:pk>` | PUT, DELETE | Post modification and delete | Admin and auth user |

    
