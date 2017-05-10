# Python-Django-Blog-Application

###### This project is about creating a blog which can be used by social network application. This is a multiuser blog so, you can think of it more of company blog rather than personal blog. There are two models - Post and Comment. Only authorized user can post a blog to the site. If the user did not publish the blog then those changes will be stored in drafts. Only published blogs can be seen on homepage under MyBlog tab. Also anyone can comment on the blog but comment will be shown only when author has approved that comment. Author has given options to approve or remove the comments.

### Technologies Used:
Python, Django Framework.
Database : SQLite 
1. There is some javascript, css features added to give the site complete feel.
2. For User authentication different validators are used:
'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
'django.contrib.auth.password_validation.MinimumLengthValidator'
'django.contrib.auth.password_validation.CommonPasswordValidator'
'django.contrib.auth.password_validation.NumericPasswordValidator'
3. Decorators(for function based views) and Mixins(for class based views) are used to automatically activate login functionality.
