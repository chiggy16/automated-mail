# automated-mail
Automated mailing service to send a mail to the receiver with the current temperature of his/her city.

1. I added the home.urls in the project's urls.py to redirect to home.urls.py file if a blank url is found.
2. I also changed the admin texts using admin.site attributes.
3. In the home.urls, I just added a single url-pattern which redirects to the app's views. (named "Index" for this particular page)
4. In the views file, I added two custom functions.
5. First one is to check the emoji according to the temperature.
6. Second one is to get the temperature of a particular city by making the API call and i stored the response in variable named 'temp'.
7. Finally we have our 'index' function which will be called upon a request from the home.urls.py.
8. In that function, I first look for the request method i.e., 'POST' and then I assign the variables with the values that are coming from our page in the form of 'POST' request.
9. I also made a DB model named 'Receiver' in the homes.models.py file.
10. After assigning the variables, I pass them to the DB model and then save it as an object.
11. Then, I used the send_mail functionality that is inbuilt in the django.core.mail module and sent all the attributes to the send_mail function.
12. At last, I print a success message if the mail has been sent successfully.
13. I made two templates, one is the 'base.html' and the other is 'index.html'.
14. The 'index.html' extends the 'base.html'.
15. 'index.html' is rendered finally at the end of successful execution of our custom view i.e., 'index'.
16. I also made changes to the settings.py and registered the app and all the neccassary steps to be done for using the 'send_email' thing and handling the static files.
