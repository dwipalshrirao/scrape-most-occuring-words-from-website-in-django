# scrape-most-occuring-words-from-website-in-django

This project is for scraping top 10 most occurring words from 'webpage' which is provided by user. I used python's webframework Django for this project. Also one third-party library 'beautifulsoup' for scrapping webpage. so you need to install it.

## Feature:
 As we know that scraping complete page and finding Top most occuring words is takes little time, so this project takes url provided by user and shows Result to user and it also save Result in Database so that when user enters same url again, it gives result directly from Database.

 ## Restrictions:
 If you don't know, all websites do not allow to scrape their webpage. So in that case our project will not work properly.

 ## How project works:

 1. Download the project:
 ```
 git clone https://github.com/dwipalshrirao/scrape-most-occuring-words-from-website-in-django.git
 cd scrape-most-occuring-words-from-website-in-django
 ```

 2. download libraries:
 ```
 pip3 install django beautifulsoup4
 ```

 3. Run cammand below:

 ```
 python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```
4. go to 'http://127.0.0.1:8000/' , it will looks like:
![image](https://github.com/dwipalshrirao/scrape-most-occuring-words-from-website-in-django/blob/main/Screenshot12.png)

enter url then will redirect to 'http://127.0.0.1:8000/result' and you can see result, which will look like:
![image](https://github.com/dwipalshrirao/scrape-most-occuring-words-from-website-in-django/blob/main/Screenshot13.png)

Now if you enter same url again then it will show result with some massege which looks like:

![image](https://github.com/dwipalshrirao/scrape-most-occuring-words-from-website-in-django/blob/main/Screenshot14.png)