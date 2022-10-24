
# Photo Album

An application for sharing photos with friends in the form 
of popular Polaroids. The project was made in the Django framework.

# Login/ Register new account
The application gives us the option of logging in or registering 
a new account.

![Screenshot](screens/login.png) ![Screenshot](screens/register.png)

# Home page
You have the option of sending photos that will appear on the main page and after clicking on the description, the full image will be displayed to us. You can see in the menu all categories that have already been created. You can also filter photos by category.

![Screenshot](screens/main2.png)

# Adding photo form
When filling in the form, we give the photo a category and description. When there is no category that would best describe our photo, we can create a new one or leave the photo without categories.

![Screenshot](screens/form.png)

# Saving photos to the database
It has not been entered into the repository for practical and security reasons !!!
The photos are created in the formula and added to the S3 bucket by AWS. The whole project is connected with the appropriate bucket and we can take photos from it and save it in it.
