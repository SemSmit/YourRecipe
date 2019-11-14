# Your Recipe

In this project I tested my Data Centric Development skills to build a Recipe site named "Your Recipe". 
Your Recipe is a site where users can Create, Read, Update and Delete recipes.
Users come to this site to see eachothers recipes and hopefully find something to make in the near future.
 
## UX
 
The site is built for people who want to see recipes from other people or share their own recipes.

- When making the site I focused on making it very easy to use, yet very practical.
  The smooth and stylish design helps the user to find their way easily through the site.
- The user knows what to do with reading/instructions because of the design.
  With enough testing and implementing I made it so that nothing can go wrong when normally using the site.

1. User Story: On entering I'm shown three options, each of them are clear to me.
2. User Story: After choosing the option "all recipes" all recipes are shown and when clicking on the readmore/image of it, I get to see more about that recipe.
3. User Story: After choosing the second option "Add your own recipe" an easy to use, clear form is shown which I can fill in.
4. User Story: Once submitted, I'm redirected to the page with all the recipes and I can see mine at the top.
5. User Story: When clicking "random recipe" I'm immediately redirected to a random recipe, with the back button built on the page I could go back if wanted.
6. User Story: When viewing a recipe on it's own page there is an "edit recipe" button. Once clicked; it shows a pre-filled form, which I can edit.
7. User Story: Once finished I can press "EDIT" and I'm redirected to the recipes page, where I can now see my edited recipe.
8. User Story: I also see a "delete" button on the bottom of the edit-page. When I click that I get to a confirm page: when I then click: "no don't delete" it brings me back to the previous page, with the filled in forms, in case I misclicked.
9. User Story: Ofcourse, when delete is then clicked on the confirm page: the recipe is deleted.


My wireframes are located in */YourRecipe/wireframes/........*


## Features

 
### Existing Features
- Creating recipes
- Reading recipes
- Updating recipes
- Deleting recipes

- And there's a function which takes you to a random recipe.

## Technologies Used

- [HTML5]
	- The project uses **HTML5** to build the structure of the website

- [CSS3]
	- The project uses **CSS3** to style the HTML5/structure of the website.

- [Python](https://www.python.org/)
	- The project uses **Python** to create and import functions for running the whole site.

- [Flask](https://www.palletsprojects.com/p/flask/)
	- The project uses **Flask** to link pages and functions with eachother, connecting to other files/urls with dynamic urls, and easy working with MongoDB and Flask_PyMongo.

- [Javascript](https://www.javascript.com/)
	- The project uses **Javascript** to make the project interactive.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [MongoDB](https://www.mongodb.com/)
  - The project uses **MongoDB** for storing data.

- [Google Fonts](https://fonts.google.com/)
	- The project uses **Google Fonts** to use fonts which aren't included in the browser.

- [Materialize CSS](http://materializecss.com/)
	- The project uses **Materialize CSS** to use icons and some pre-built forms/menu's for a more pleasant user experience.




## Testing

The most testing was done through building the site.
Tested a lot of unusual actions to try and "break" the site, and then fix it if needed.
Tested it on a small laptop, a large monitor, multiple phones and ofcourse used the browser's function to show the project on various screen sizes.
And also tested it on various browsers.


## Deployment

The changes made were commited through git and then later pushed to (https://github.com/SemSmit/YourRecipe).
Heroku automatically retrieves these files when pushed and then builds the app on heroku.
The MONGO_URI, MONGO_DBNAME and SECRET_KEY are stored in "env.py".
"env.py" is ignorded by GIT and won't be pushed/shown to the public.
In Heroku I set these values in the config vars, so it can run properly.

I deployed the site using Heroku.
The site can be found on: (https://yourrecipe.herokuapp.com/)

###Local Deployment
Install Python version 3 or higher.
Create a virtual environment using "python3 -m venv path/to/virtual/env"
to run, go to your local virtual environment in your terminal and type 'env\Scripts\activate', then go to ......./YourRecipe 
then use "pip3 install -r requirements.txt" to install the python packages for this project.
Then type 'flask run' to build&run the app.

The link where you can see your app is shown in your terminal.


## Credits

  Thanks to the StackOverflow and the tutors of CodeInstitute for helping me out a few times

  And to my mentor Ignatius Ukwuoma for giving me tips throughout the project

### Media
- The three icons on the homepage are made by my colleague Romy Bond.
- I got the recipes from Jamie Oliver's recipe site. (https://www.jamieoliver.com/)
