# Timeless - A Passionate Community Forum Focused On Watches
## Third Project : Data-Centric Development Milestone Project
A live demo of this project can be viewed [here](https://john-p3-timeless.herokuapp.com/). 

This project is a protocol for a full website and many features are not loaded. 
Currently the project is to display CRUD functions under this website
No user login or logout feature is installed

### Disclaimer
Posts and listings populated by the various users as seen on the forum  are mainly used for the presentation of the demo.Therefore, the users that were being used are the different accounts that I have made to used to populate the forum and are not actual users of the forum. 

## UI/UX
### Strategy
#### User Stories
Watch Collectors:
1. Have meaningful discussions and share information about watches with other watch collectors
2. Make a listing and be able to sell their watches to other users

Gift Buyers:
1. Gain information on how to purchase a watch as a gift for others
2. Make deals with other users on purchasing a watch

Site Owner's Goals:
1. To provide a warm community environment for users to be able to interact with each other and exchange information
2. Provide a platform for users to sell their watches to other users

Proposed Solution:
Create a dynamic forum that would allow different types of users to be have the ability to post and market their watches online.

### Scope
#### Required Functionalities
1. **CREATE/READ/UPDATE/DELETE (CRUD) Functionality**
- Listings: Users must be able to read listings, edit their own listings,delete their own listings and create a listing.
- Posts: Users must be abe to read posts, edit their own posts, delete their own posts and create a post.
- Profile: Users must be able to see their profile information and edit their own profile information
2. **Backend Storage**
- Listings data, Posts data, User Account Data and Profile Data will all be stored using a backend database
3. **User Interaction**
- Users will be able to search for their post or listing 
- Users will be able to filter the posts and listings based on their desired requirements
4. **Presentation and Responsiveness**
- Users should be able to view the web application through different platform devices
- Posts and listings should be displayed in a clear and neat manner throughout the webpage.

### Structure
![SiteMap](readme/timeless-sitemap.jpg)

Taking inspiration from a hub-and-spoke design, the website is designed in a way that would allow all users to be able to navigate through the site easily as well as for clear organisation of website content.


### Surface
Images used in the project were related to watches or community to promote a healthy and warm community of users interested in watches.

## Features
### Current Features
-  Responsive web design for different platform devices
-  Users can view the listings by brands
-  Create/Edit/Read/Delete Listings
-  Create/Edit/Read/Delete Comments (_future developments_)
-  Filter Buttons to sort Posts for  most recent (_future developments_)
-  Filter Buttons to sort Listings for most recent (_future developments_)
-  Search bar at the navigation top bar used to search for post or listing title depending on whether is at the homepage or marketplace respectively. (_future developments_)
- User Menu Navigation for users to navigate to different parts of the website at homepage or marketplace
- Allow Users to Chat to Buy with other users in real time, therefore (_future developments_)
- Setting up reviews section for users to be able to deal with more confidence in the marketplace (_future developments_)

## Technologies Used
- HTML 
- CSS
- Javascript
- JQuery
- Flask
- Pymongo
- Flask-Login
- Jinja2
- MongoDB
- Bootstrap 
- Heroku
- Cloudinary

### Flask
The web framework used in the development of the webpage that is reponsible for the key essential features such as routing, validation of forms and implementing key functions of the webpage. 

### Backend Tools
1. Pymongo
- Used to interact with MongoDB database 
2. dnspython
- Used for establishment of connection to MongoDB database


## Programming Methodology
### Form Validation
Upon submission of a form, there will be validation in place that is handled through condition checkers. An error accumulator which is a dictionary is used to store the errors and if the error accumulator has received errors, the user will be notified through a danger toastr message of a failed form submission.

### Security Control
- Through the use of .env file, important and sensitive data such as secret keys are carefully hidden away so that they are not leaked into the publc.
- Passlib library is used to encrypt passwords when the password is saved into the database to prevent unauthorized personnel from retrieving the passwords easily upon access to the database

### Source Control
- Github is used to track and manage any changes in the development of the project



## Testing
All testing was carried out manually and the results of the testing are shown below:
| Test Number | Event                                                   | Expected Observation                      | Actual Observation             |
|-------------|---------------------------------------------------------|-------------------------------------------|--------------------------------|
| 1           | Home screen > click SHOP > <SELECTED BRAND>             | display selected watches of the <BRAND>   | *Pass*                         |
| 2           | Home screen > click SELL YOUR WATCH > <SELL MY WATCH>   | show form for user to entry and submit    | *Pass*                         |
| 3           | Home screen > click SELL YOUR WATCH > <VIEW MY LISTINGS>| show all watches                          | *Pass*                         |
| 4           | (show_post) route > click <modify>                      | show form for user to modify data & submit| *Pass*                         |
| 5           | (show_post) route > click <remove>                      | remove from databases                     | *Pass*                         |

 
### Responsiveness
Using the inspector function of Google Chrome, the following devices was used in the testing phase for mobile responsiveness:
- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- IPad
- Ipad Pro

In the testing of responsiveness to both phone and tablet devices, the webpage application is able to display and layout the correct intended design for the different
pages when tested through these different platforms.

### Bugs
- If users upload many images into the create listing or edit listing form, only the latest image will be taken into the database.

## Deployment
This website is deployed on [Heroku](https://www.heroku.com). 

To deploy on Heroku
1. Download or Clone the master branch from [github](https://github.com/l0nelyhermit/Timeless)
2. To list all the requirements in requirements.txt, run the following command in terminal:
```
pip3 freeze --local > requirements.txt
```
3. Set Debug to False
4. Procfile need to be created to run gunicorn upon deployment
5. Git push to Heroku Master after all the documents are properly set up
6. Use Your Own MongoDB account to host the database and use your own cloudinary account to host the images uploaded by users
6. All public keys and private keys for the following need to be added to in Heroku Config Vars settings:
    - MongoDB URI : Your Own MONGO_URI
    - Secret Key: Choose Your Own Secret Key
    - Upload Preset: Your Own Upload Preset
    - Cloud Name: Your Own Cloud Name 

## Credits and Acknowledgement
- Bootstrap Snippets : https://bootstrapious.com/snippets
- W3school for references
- Stack Overflow for references

### Acknowledgements
- Images used from (https://www.thewatchbox.com/)




