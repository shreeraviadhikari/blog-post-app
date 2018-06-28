# Article App Using Django-Rest-Framework

## Models

### Article

Method | Permission
---|---
Create | Normal User
Publish | Admin
Archive | Owner, Admin
Update | Owner

### Like
Method | Permission
---|---
Like| Normal User
Unlike | Owner

### Comment
Method | Permission
---|---
Create | Normal User
Delete | Owner, Commentator, Admin


## Dashboard

### Normal User Dashboard

* List
* Update
* Create
* Archive

### Admin Dashboard

* Publish Unpublished Articles
* Archive Published Articles
* List Published Articles

