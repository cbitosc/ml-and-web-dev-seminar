# A Template to create your own Flask Application with MVC architecture


## What does MVC stand for?

**M(Models),V(Views) and C(Controllers)**. This might not mean much at a first glance but this form of application structuring is used extensively by major companies. **Models**, is the **ORM(Object Relational Mapping)** that is essentially the view of your database.

**Views**, is essentially what the user sees; In case of web apps, views are the html and css pages that provide an interface for the client side users. 

**Controllers** are generally links between the views and controllers,authentication modules, api generators and propogators; In the structure shown below, the views and controllers are combined together in one file. This is due to Flask's ability to let you add functionality on the go. This way, you dont have to go through the hastle of implementing functionality in another file and integrating those functions with the views in yet another file. 



## Why MVC?

When projects get larger, so does the code base. If all the code base for a given project was written in one file, it would not be readable and eventually become a tedious task for the developer to handle. Hence, the concept of structuring came into picture. MVC is one of the many structures followed in architecting the code repository. Other popular architectures are MVVM, MDA,etc. 


### Now that the conceptual part is out of the way, lets start coding!

 Create the following files and folders in the structure shown(or fork/clone [this](https://github.com/revannth/flaskMVC_template) repository) :

```
~/Application_Name
    |-- run.py
    |-- config.py
    |__ /env             # Virtual Environment
    |__ /app             # Our Application Module
         |-- __init__.py
         |-- models.py 
         |-- views.py
         |-- /static    
         |__ /templates
             |__ hello.html
         |__ ..
         |__ .
    |__ ..
   |__ . 
```
Use this to structure your old flask applications that were written in a single file. To run the web application, all you have to do is while your commandline is pointing to the Application_Name directory :


```  
  python run.py
```
