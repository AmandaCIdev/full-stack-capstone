<h1 align="center">iCreate</h1>                                      


<p align="center">
<img src="static/images/responsive-site.png" width="600" height="100%">
</p>




This project utilises a full-stack framework, incorporating Django, Python, JavaScript, HTML, and CSS. My objective is to develop a responsive website that enables users to perform CRUD operations, as well as post, comment, and interact with events by liking or unliking them. It's important to note that this project has been created solely for educational purposes.



**[Visit my website](https://amanda-ci-dev-full-stack-cap-a6484667fa4d.herokuapp.com/)**

# Overview

The website targets vulnerable and underserved youth, offering a platform for lifelong skill development similar to Boys and Girls Scouts. My mission is to expand events into an online hub where participants earn badges by mastering skills, fostering interaction, and applying abilities to life challenges. Youth aged 6-18 can transition and grow in a safe space. 
The age limit of 18 years old aligns with the legal definition of adulthood in the USA, which is why it's applicable for the websites purposes.

The name iCreate embodies the boundless potential within each individual child to shape their own reality, transcending limitations imposed by environment or resources. It stands as a powerful affirmation of personal empowerment, urging individuals to craft their unique selves without constraints.

# Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

#
# UX

Applying fundamental UX principles, I initially focused on devising a strategy by identifying the target audience and determining the features that would offer them the most value.


The target audience for 'iCreate Youth' includes:

- Youth aged 6-18 years old, aiming to engage them in constructive and educational activities.
- Individuals seeking to explore their creativity and develop new skills.
- Students looking for opportunities to participate in events and workshops relevant to their interests.
- Guardians interested in providing their children with enriching experiences and learning opportunities.

These users will be looking for:

- An engaging and interactive website tailored to their age group.
- Opportunities to explore various interests and hobbies through workshops and events.
- A platform where they can register for events and courses easily.
- Features to track their progress and achievements, such as earning badges or certificates.
- A user-friendly interface with intuitive navigation to access content and resources.
- The ability to post, comment and like events an provide feedback reviews.
- Functionality to manage their registrations, including canceling or rescheduling participation as needed.

This website will provide all of these features while ensuring a safe and supportive online environment for youth to 
learn, explore, and grow. Additionally, it will incorporate CRUD functionality to allow administrators to manage workshops, courses, registrations, and user data effectively.

## User Stories

**Epic: Admin**
- As a site Admin I can create, edit and delete events and comments so that I can manage the site content
- As a site Admin I can access the admin panel so that I can manage events and comments
- As a site Admin I can log out of the admin panel so that I can disconnect from the website
- As a site Admin I prioritise implementing measures to safeguard youth data and ensure compliance with privacy 
  regulations, demonstrating our commitment to protecting user information. 
- As a site Admin I prioritise the inclusion of diverse and inclusive content on the website, ensuring that resources, 
  events, and services cater to the varied needs and backgrounds of our youth population, promoting accessibility and equity.
- As a site Admin I seek to establish partnerships with local teachers, therapists, and licensed professionals to expand 
  the range of services and resources available to youth on our platform, enriching the overall wellness experience and promoting collaboration within the iCreate hub.


**Epic: User Interaction**
- As a logged-in User I can write comments on events so that I can leave my feedback
- As a logged-in User I can like and unlike events so that I can mark which events I like
- As a User I can view the number of likes on events so that I can see which events are the most popular
- As a User I can view comments on events so that I can read other users opinions


**Epic: User Events**
- As a logged-in User I can post a event so that other users can see them to sign up
- As a User I can delete my events so that I can remove any unwanted events that I have made
- As a User I can edit events so that I can update any changes or mistakes to my events
- As a logged-in User I can upload an image along with my event so that other users can see an image relating to the event


**Epic: Login/Register**
- As a User I can register for an account so that I can interact with the site content
- As a User I can log in/out off my account if I wish so that I can connect or disconnect from the website
- As a User I can easily see if I'm logged-in or logged-out so that I can be sure what my status is


**Epic: Navigation**
- As a young user aged 6-18, I want the navigation of the iCreate platform to be designed with my needs in mind so that I can easily find and access the content I'm interested in.
- As a young user aged 6-18, I want the navigation of the iCreate platform to work seamlessly on all devices, including smartphones and tablets, so that I can access the platform from anywhere.
- As a young user aged 6-18, I want the navigation menu of the iCreate platform to be organised into clear categories like Events, About, Resources, Login, Logout so that I can quickly navigate to the content I want to explore.
- As a young user aged 6-18, I want the navigation of the iCreate platform to use engaging visuals, icons, and colours to make it visually appealing and attractive to me.
- As a young user aged 6-18, I want the navigation elements of the iCreate platform to be consistent across different pages so that I can easily understand and navigate the website.
- As a young user aged 6-18, I want the navigation of the iCreate platform to be accessible to users with disabilities, including features like keyboard navigation and screen reader compatibility, so that all users can use the platform effectively.


<p align="center">
<img src="static/images/Kanban Project Board.png" width="100%" height="100%">
</p>


#
# Scope 

## **Features**

### **Home Page**

1. **Navigation Bar**
   - The navigation bar appears on every page so users can easily navigate through the site
   - Navigation bar has links for 'Home', 'About' and 'Login/Register' more links will be shown to logged in users
   - If the user is logged in then the left side of the menu shows links for pages that only authorized users can visit 
   - The user name will also appear on the bar, indicating which user is logged in
   - The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

   <p align="center">
<img src="static/images/iCreateNavbar.png" width="100%" height="100%">
</p>

2. **Landing Page Image - Event Flip Cards**
   - The landing area features engaging flip cards designed for children to flip 180°, revealing event details on the reverse side, effectively conveying the website's purpose and the range of services offered.

3. **Footer**
   - The footer, present on all pages, comprises two sections: one containing social media link to GitHub, and the other acknowledging the website project portfolio by name.

  <p align="center">
  <img src="static/images/Default.jpeg" width="100%" height="100%">
</p> 

4. **Home Page - ‘Home’**
   - A curated collection of high-quality images categorized by events.

5. **About Page - ‘About’**
   - Information on how to get in touch. Contact form for convenient communication.

6. **Register Page - ‘Register’**
   - The register page allows users to create a new account by providing necessary information such as username, email, password, and optional profile details.

7. **Login - ‘Login’**
   - Include username and password fields, a remember me option, error handling for incorrect credentials, a login button, links for forgot password and registration, security measures like CAPTCHA or two-factor authentication.

## Design

### Imagery
- The design layout features a clean and minimalistic structure with a simple background, providing a visually uncluttered canvas. The imagery seamlessly integrates with a striking futuristic gaming design, elevating the overall visual appeal.

### Typography
- Google Fonts were used to import the Julius font into styles.css. Chosen for it's simple, unembellished, minimalistic feel that is easy to read.


### Future Features
- Audio & Video books, music, educational tutorials tailored for children
- User Settings: Parental Permission for Safe Hub, a platform similar to Facebook but designed specifically for kids
- Blog Post for children by children
- Awards and Certificates to Print

#
# Structure

The MVP website for youth aged 6-18 is structured to be intuitive and engaging, with clear navigation and visually appealing design elements. The platform prioritizes simplicity and ease of use, ensuring that young users can easily navigate, interact with content, and participate in various activities tailored to their age group. Additionally, the website emphasizes safety and accessibility, providing a secure environment for youth to explore, learn, and engage with the platform's offerings. Simplicity helps young users to quickly and easily access the app and navigate within the app.

The website is made from one app:
- event
- about


# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Desktop](assets/documents/Desktop-wireframes)
- [Tablet](assets/documents/Tablet-wireframes)
- [Mobile](assets/documents/Mobile-wireframes)

# Database schema

<p align="center">
<img src="static/images/iCreate-Database- Schema.png" width="900" height="100%">
</p>

## Font 
- Julius, sans-serif - main font
- Lexend - for Event in Home page

## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

 ## Frameworks, Libraries & Programs Used

[GitHub](https://github.com/) - GitHub is a web-based platform for version control using Git, enabling collaborative software development and hosting of code repositories. GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - Django is a high-level web framework for building web applications rapidly with a clean and pragmatic design.

[ElephantSQL](https://api.elephantsql.com) - ElephantSQL is a hosted PostgreSQL database service that can be seamlessly integrated with Django applications, providing scalable and reliable database solutions.

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework for developing responsive and mobile-first websites quickly and efficiently.

[Cloudinary](https://cloudinary.com) - Cloudinary is a cloud-based media management platform that offers solutions for storing, optimizing, and delivering images and videos for web and mobile applications.

[Summernote](https://summernote.org/) - Summernote is a Django app that enables users to easily integrate a rich text editor into their web applications, enhancing event creation and description functionality.

[DALL-E3](https://openai.com/) - DALL-E3 is an advanced AI model developed by OpenAI that generates images from textual descriptions.

[TinyPNG](https://tinypng.com/) - TinyPNG is a website that offers image compression services to optimize image files for faster loading on webpages while maintaining visual quality.

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - Google Fonts is a collection of free, open-source fonts that can be easily integrated into websites and other digital projects to enhance typography.

[Font Awesome](https://fontawesome.com/) - Font Awesome is a library of scalable vector icons that can be easily customized and used to enhance the visual appeal of websites and applications.

[Beautify](https://www.jpkc.com/tools/beautify/) - Beautify is a code formatter tool that automatically formats code to improve readability and consistency.

[Balsamiq](https://balsamiq.com/) - Balsamiq is a wireframing tool used for creating low-fidelity mockups of user interfaces, allowing for quick and easy visualization of design ideas.

[Lucidchart](https://lucid.app) - Lucidchart is a web-based diagramming tool that allows users to create and collaborate on flowcharts, ERDs, and other visual representations of data and processes.

[Am I Responsive](http://ami.responsivedesign.is/) - Am I Responsive is a web tool that allows users to quickly preview how their website appears on various devices and screen sizes, helping to ensure responsiveness and compatibility across platforms.

[Diffchecker](https://www.diffchecker.com/text-compare/) - Diffchecker is a text comparison tool used to highlight the differences between two blocks of text, facilitating comparison and analysis.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The W3C CSS Validator is a tool used to check the validity and syntax of CSS code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - The W3C Markup Validator is a tool used to check the validity and syntax of HTML code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

[JSHint](https://jshint.com/) - JSHint is a static code analysis tool used for checking JavaScript code for errors, potential problems, and stylistic inconsistencies.

[Lighthouse](https://developer.chrome.com/docs/lighthouse) - an open-source tool used for auditing web page quality, including performance, accessibility, SEO, and cross-browser testing.



# Testing *****THIS SECTION IS STILL BEING WORKED ON*******


## User Story Testing

### **Testing Users Stories form (UX) Section**

**EPIC: Superuser / Admin**
- As a site Admin I can create, edit and delete events and comments so that I can manage the site content
- As a site Admin I can access the admin panel so that I can manage events and comments
- As a site Admin I can log out of the admin panel so that I can disconnect from the website

This was tested by accessing the Django Admin Panel. By creating a Superuser we can access the Django Admin Panel where the administrator can perform all the CRUD functionalitis

**EPIC: User Interaction**
1. As a logged-in User I can write comments on events so that I can leave my feedback

<p align="center">
<img src="assets/images/default.png" width="500" height="300">
</p>

2. As a logged-in User I can like and unlike events  so that I can mark which events I like
<p align="center">
<img src="assets/images/default.png" width="300" height="200">
</p>

3. As a User I can view the number of likes on events so that I can see which events are the most popular
<p align="center">
<img src="assets/images/default.png" width="300" height="200">
</p>

4. As a User I can view comments on events so that I can read other users opinions
<p align="center">
<img src="assets/images/default.png" width="800" height="100%">
</p>

**EPIC: User Events**
1. As a logged-in User I can post events so that other users can see them
<p align="center">
<img src="assets/images-features/add-recipe.png" width="600" height="100%">
</p>
2. As a User I can delete my event so that I can remove any unwanted events that I have made
<p align="center">
<img src="assets/images-features/delete-recipe-model.png" width="500" height="100%">
</p>
3. As a User I can edit events so that I can update any changes or mistakes to my events 
<p align="center">
<img src="assets/images-features/edit-recipe.png" width="600" height="100%">
</p>
4. As a logged-in User I can upload an image along with my event so that other users can see what the event theme looks like
<p align="center">
<img src="assets/images/upload-image.png" width="400" height="100%">
</p>


**EPIC: Login/Register**
1. As a User I can register for an account so that I can interact with the site content
<p align="center">
<img src="assets/images-features/register.png" width="600" height="100%">
</p>

2. As a User I can log in/out off my account if I wish so that I can connect or disconnect from the website
<p align="center">
<img src="assets/images/signout.png" width="600" height="100%">
</p>
3. As a User I can easily see if I'm logged-in or logged-out so that I can be sure what my status is
<p align="center">
<img src="assets/images/logged-in.png" width="1000" height="100%">
</p>
<p align="center">
<img src="assets/images/signed-out.png" width="1000" height="100%">
</p>

**EPIC: Navigation**
1. As a User I can easily navigate through the site so that I can view desired content
<p align="center">
<img src="assets/images-features/navbar.png" width="1000" height="100%">
</p>

2. As a User I can see the most loved events so that I can quickly join in 
<p align="center">
<img src="assets/images-features/most-loved-recipes.png" width="600" height="100%">
</p>

3. As a User I can see the most recent events so that I can keep up to date with my new skills
<p align="center">
<img src="assets/images-features/favourite-recipes-page.png" width="600" height="100%">
</p>


### Validator Testing

#### HTML Validator
- [Results for index.html](#)
- [Results for gallery.html](#)
- [Results for contact.html](#)

#### CSS Validator
- [Results for styles.css](#)

#### Browser Compatibility
- Chrome Version 90.0.4430.212
- Firefox Version 88.0.1
- Safari on macOS Catalina (Safari Version 14.0.3)

### Test Cases and Results
- [Test Cases](#)

### Unfixed Bugs
- 
- 

## Known Bugs
- User image uploads weren't uploading to Cloudinary. To fix this I added {% load cloudinary %} at the top of the file
- The  button on the form was not responding
- The front flip cards were not displaying the image. To fix this I included the {% load static %} at the top of the file
- The back flip cards were not displaying the text correct. To fix this I reduced the text in admin
- *****CHECK THE FIX COMMITS IN REPO*****
- 

# Deployment

## How this site was deployed
Here are the basic steps for deploying a project from Gitpod to Heroku and linking it to GitHub using manual deployment:

## Prepare Your Project:

- Ensure your project is ready for deployment and is working as expected locally.
Make sure your project includes a requirements.txt file listing all the dependencies and a Procfile to specify the command to start the web server.

## Create a GitHub Repository:

- If you haven't already, create a GitHub repository for your project.
Push your project code to this GitHub repository.

## Set Up Heroku Account:

- Sign up for a Heroku account.
Install the Heroku CLI (Command Line Interface) on your local machine.

## Create a New App on Heroku:

- Log in to your Heroku account via the terminal using the Heroku CLI.
Create a new app on Heroku using the heroku create command.

## Link Heroku App to GitHub Repository:

- Go to the "Deploy" tab of your Heroku app dashboard.
Under "Deployment method," select GitHub as the deployment method.
Search for your GitHub repository and connect it to your Heroku app.

## Enable Manual Deployment:

- Disable automatic deploys to ensure that changes pushed to your GitHub repository do not trigger automatic deployments on Heroku.
You can do this by clicking on the "Enable Automatic Deploys" button and then turning off the "Wait for CI to pass before deploy" option.

## Deploy Your App:

- Manually deploy your app by clicking the "Deploy Branch" button in the "Manual deploy" section.
Choose the branch you want to deploy from (e.g., main or master).

## Wait for Deployment:

- Wait for the deployment to finish, and check the logs for any errors.

## Test Your Deployed App:

- Once the deployment is complete, open your app using the provided Heroku URL and test that it works as expected.
By following these steps, you can manually deploy your project from Gitpod to Heroku and link it to GitHub for version control.

- Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

- Any changes pushed to the master branch will take effect on the live project.

The live link can be found [https://github.com/AmandaCIdev/iCreate](#).

## How to clone the repository
1. Go to the GitHub repository on GitHub.
2. Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
3. Open a GitBash terminal and navigate to the directory where you want to locate the clone.
4. On the command line, type "git clone" then paste in the copied URL and press the Enter key to begin the clone process.

## Django and Heroku 
- I followed the Code Institute's Coding Coach instructional video to install and set up the Django framework.

# Credits
- [Django Crispy Forms] (https://django-crispy-forms.readthedocs.io/en/latest/install.html) - Instructional Documentation help
- [Whitenoise Docs] (https://whitenoise.readthedocs.io/en/latest/django.html) - Instructional Documentation help
- [Pop. ai] (https://www.popai.ai) - Help me write the readme overview
- [Stack Overflow] (https://stackoverflow.com) - Crispy Forms instructions help
- [Django Summernote Docs] (https://github.com/summernote/django-summernote) - Instructional Documentation help
- [ChatGPT] (https://chat.openai.com) - Answering my many questions
- [DALL-E 3](https://openai.com/dall-e-3) - Created all my ideas via text and translated them into an image

## Media
- The icon in the footer were taken from Font Awesome.
- The fonts used were imported from Google Fonts.
- My favicon were created by DALL-E 3.
- My images were all created by DALL-E 3.

## Acknowledgments
- I am grateful to my mentor for providing valuable feedback.
- Coding coach Kevin, for his very helpful SME videos.
- I am grateful to my colleague Tom, who spent his time helping me fix my bugs.




