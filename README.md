
###SHOPPERSTAR###

#Description#: It is a backend e-commerce webiste project built on Django framework.

#Key features#-1) **token authentication**
2) **user cart** - every user has a cart in which he can add/remove items. 
3) **bogo feature**- this "buy one get one free" offer is applicable on certain products. 
4) **search products feature**- it allows users to get relevant search results for products. 


Detailed desciption about apps: The project consists of 4 Django apps-"login_signup","category","cart","payment".

 **login_signup app**- It consists of 3 sections-"login","signup","profile".
                    (1) signup-user supplies information about himself and sets a username and password.
                    (2) login-user can login by supplying the username and password. On successful authentication,a token is generated                                 which has to be provided as Authorization header key before being able to access any API. 
                    (3) profile- profile information about the user is generated in JSON format. 
                    
 **category app**-It consists of 4 sections-"category", "subcategory","product" and "search"
                    (1) category,subcategory,products- it caters to three request methods-POST, DELETE, GET.
                                  POST- category/subcategory/products can be added here.
                                  DELETE- a particular category/subcategory/products can be deleted by providing their unique ids.
                                  GET- it gives a list of all categories/subcategories/products that exist in the database.
                    (2) search- it implements the "search products" feature.
                  
**cart**- It consists of 3 sections-"add","remove" and "display"
                    (1) add- Through this, user can add products to his cart. It outputs the cart details of the user,including details                         like cart total, product_id and quantity for each particular product.
                    (2) delete- User can delete products from his cart. It outputs the updated cart details.
                    (3) display- It displays the current cart status of the cart.
                    
**payment**- It consists of "payment" page. 
                    (1) payment - It displays information about payment status for the user against his cart total.
                    
**api_token_auth**- It is a built in end point that provides the unique token id to every user if Django successfully authenticates the user through his "username" and "password".

                    


#Technologies used#:

                   1) Django 2.2.3 , Django Rest Framework 3.9.4
                   
                   2)Python (Django framework uses Python) 3.7.3
                   
                   3)MySql (database used in the project) 8.0.16
                   
                   4)Postman (for API testing) 7.3.6
                   
#How to set up the project#:

1) Install Python from this link from here :https://www.python.org/downloads/
2) Install mysql from here : https://dev.mysql.com/downloads/mysql/
3) On terminal, type "pip install virtualenv" to install virtual environment.
4) Run the command "virtual my_name". After running this command, a directory named "my_name" will be created that will contain all the necessary executables to use the packages a Python project would need.
5) Activate this virtual environment using the command "./Scripts/activate". The name of your virtual environment will now appear on the left side of terminal. 
6) Install django using "pip install django==3.9.4"
7) Install django rest framework using "pip install djangorestframework==3.7.3"
8) Install mysql client using "pip install mysqlclient".
9) Create a new connection in MySql. Create a new database "com" using sql command "create database com". 
If you have set a password to the connection, then update it in "DATABASE" dict in settings.py under the key "PASSWORD".





