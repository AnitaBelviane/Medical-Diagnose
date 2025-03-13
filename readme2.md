# MEDICAl_DIAGNOSE

# Description de la procedure a suivre 

#### PRESENTATION OF DATABASE
1. User Table
2. Admin  Table
3. Brand Table
4. Product Table
5. Categories Table
6. Review Table
7. Order Table
8. OrderDetail Table

#### PACKAGES INSTALL
1. pip require
2. django require
3. create a virtual environement `$ python3 -m venv <name of virtual env>`
4. activate the virtual env `$ source <name of virtual env> / bin / activate `
5. verified the install pack in virtual env `$ pip freeze`
6. create project `$ django-admin startprojet <project_name> .`
7. create an application`$ python manage.py startapp <app_name>`


#### HOW TO RUN THE APP
1. Clone the repository from github 
2. Install all the necessary packages by: `$ pip install Django` 
3. Create the .env file by typing the command:`$ cp  .env`
4. Generate Application key with: ` `
5. Run the migration (create the database): `$ python manage.py migrate`
6. Insert dummy data: `$ `
7. Run the app: `$ python manage.py runserver` for django  launch your browser on the url from your local machine
8. Enjoy !!!

#### SOME COMMAND

1. for create controller => `php artisan make:controller Jeu\UserController`
2. for create model and migration => `php artisan make:model DOc -m`
3. for create a seeder => `php artisan make:seeder UsersTableSeeder`
4. for apply seeder in database => `php artisan migrate:fresh --seed`
5. for fresh all route and clear cash => `php artisan optimize`
6. for create a middleware => `php artisan make:middleware AdminMiddleware`
7. for create model => `php artisan make:model contact`
8. for make seed => `php artisan migrate:fresh --seed`
9. for specific seed => `php artisan migrate:fresh --seed --seeder=UserSeeder`

22. for create model and her migrations: `php artisan make:model Admin -m`


23. 

#### How to Downlaod DATABASE
mysqldump -u username -p database_name > medical_app.sql

#### HOW to GIT



#### HOW TO CONTRIBUATE




garder la cle openai secrete en utilisant dotenv: pip install python-dotenv

