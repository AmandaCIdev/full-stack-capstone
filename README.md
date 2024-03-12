<h1 align="center">iCreate</h1>                                      


<p align="center">
<img src="static/images/Default.jpeg" width="600" height="100%">
</p>




This project utilises a full-stack framework, incorporating Django, Python, JavaScript, HTML, and CSS. My objective is to develop a responsive website that enables users to perform CRUD operations, as well as post, comment, and interact with events by liking or unliking them. It's important to note that this project has been created solely for educational purposes.



**[Visit my website](https://8000-amandacidev-lovewellnes-rpx3pkiwlem.ws-eu108.gitpod.io/)**

# Overview

The website targets youth, offering a platform for lifelong skill development similar to Boys and Girls Scouts. Our mission is to expand events into an online hub where participants earn badges by mastering skills, fostering interaction, and applying abilities to life challenges. Youth aged 6-18 can transition and grow in a safe space.


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


# User Experience (UX)

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

## A. User Stories
1. As a site user, I want to explore various wellness events to stay informed about the latest offerings and activities.

2. As a site user, I need to find information about the dates, times, and locations of wellness events to attend them in person.

3. As a site user, I expect to have easy access to contact details to inquire about participating in or purchasing tickets for wellness events.

4. As a site user, I desire intuitive navigation throughout the website to enhance my user experience and find relevant information effortlessly.

5. As a student user, I want to easily access information about upcoming wellness events on campus, including workshops, seminars, and classes, so that I can participate in activities that promote my physical and mental well-being.

6. As a student user, I want to have the option to book consultations with wellness professionals, such as nutritionists or counselors, directly through the website, to easily access support and guidance for my health concerns.

7. As a student user, I would like to be able to leave reviews and feedback on wellness services and events that I have attended, to share my experiences with others and help improve the offerings on campus.

8. As a student user, I want the website to provide resources and information about maintaining a healthy lifestyle, including articles, videos, and tips, to support my overall well-being during my time at college.

9. As a site user, I expect to find comprehensive information about available wellness services, including descriptions, schedules, and pricing, to make informed decisions about my health and well-being options on campus.

10. As a site user, I hope to discover a variety of wellness resources, such as articles, videos, and podcasts, curated to address various aspects of mental and physical health, supporting my holistic well-being journey as a college student.


### B. Owner of Site Goals
1. As the owner of the site, I want to integrate social media features to share wellness events and resources on platforms like Instagram and Facebook, enabling students to engage with our content and reach a wider audience.

2. As the administrator, I aim to create a dedicated section for therapist and instructor profiles, allowing students to learn more about the professionals offering services on campus and fostering a sense of trust and connection.

3. As the site owner, I prioritize implementing measures to safeguard student data and ensure compliance with privacy regulations, demonstrating our commitment to protecting user information and building trust within the community.

4. As a site owner, my aim is to establish a seamless booking system for students, allowing them to effortlessly schedule sessions with therapists, instructors, or wellness services. This will facilitate convenient access to support and resources whenever needed.

5. As the site owner, I aim to establish partnerships with local vendors offering healthy food options, allowing students to explore and access nutritious dining choices conveniently through our platform.

6. As a site owner, I aim to create an interactive forum or community space where students can share their wellness journey, exchange tips, and support one another, fostering a sense of belonging and camaraderie within the campus community.

7. As a site owner, I prioritize the inclusion of diverse and inclusive content on the website, ensuring that resources, events, and services cater to the varied needs and backgrounds of our student population, promoting accessibility and equity.

8. As a site owner, I strive to continuously gather feedback from students through surveys, polls, and reviews, allowing us to adapt and improve our offerings based on user input, enhancing the overall experience and effectiveness of the platform.

9. As a site owner, I aim to streamline the registration process for students, making it easy and intuitive to sign up for our wellness services, events, and resources, thereby increasing user engagement and participation.

10. As a site owner, I seek to establish partnerships with local wellness practitioners, therapists, and vendors to expand the range of services and resources available to students on our platform, enriching the overall wellness experience and promoting collaboration within the campus community.

## Features

### Existing Features

1. **Navigation Bar**
   - The navigation bar appears on every page so users can easily navigate through the site
   - Navigation bar has links for 'Home', 'About' and 'Login/Register' more links will be shown to logged in users
   - If the user is logged in then the left side of the menu shows links for pages that only authorized users can visit 
   - The user name will also appear on the bar, indicating which user is logged in
   - The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

   <p align="center">
<img src="static/images/Default.jpeg" width="100%" height="100%">
</p>

2. **Landing Page Image - wellness**
   - The landing area includes a photograph and text below that clearly identify the purpose of the business and the type of product and service it offers. 

3. **Footer**
   - The footer is featured on all four pages and contains two sections: social media links and website creators.

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
- The design layout features a clean and minimalistic structure with a simple background, providing a visually uncluttered canvas. Imagery is elegantly incorporated with prominent wellness photos, enhancing the aesthetic appeal.

### Typography
- Google Fonts were used to import the Julius font into styles.css. Chosen for it's simple, unembellished, minimalistic feel that is easy to read.

### Wireframes
- [Main Page Wireframes](#) 
- [Gallery Page Wireframes](#) 
- [Contact Page Wireframes](#)

## Technologies Used

### Languages Used
- HTML
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs Used
- Google Fonts
- Font Awesome
- Git
- GitHub
- Balsamiq
- Adobe Stock
- Quora
- Google
- Django
- Bootstrap
- Heroku
- ElephantSQL

## Testing

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
- Correction to add: 
- A 

### Known Bugs
1. 
2. The submit button on the form was not responding.

## Deployment

### How this site was deployed
1. In the GitHub repository, navigate to the Settings tab, then choose Pages from the left-hand menu.
2. From the source section drop-down menu, select the Master Branch.
3. Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
4. Any changes pushed to the master branch will take effect on the live project.
5. The live link can be found [https://github.com/AmandaCIdev/love_wellness](#).

### How to clone the repository
1. Go to the GitHub repository on GitHub.
2. Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
3. Open a GitBash terminal and navigate to the directory where you want to locate the clone.
4. On the command line, type "git clone" then paste in the copied URL and press the Enter key to begin the clone process.

## Credits

### Content
- All other content was written by the developer.

### Media
- The icons in the footer were taken from Font Awesome.
- The fonts used were imported from Google Fonts.
- Favicon: AI-DALL-E 3.

### Acknowledgments
- To be added.
