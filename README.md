# BurgerBar

The BurgerBar website is designed to be responsive website allowing visitors to view on a range of devices. It allows visitors to find out about the bar, view rewiews, view availability of tables and book or manage your reservations..

[amiresponsive](https://res.cloudinary.com/dzwpkjbhq/image/upload/v1689780907/static/summernote/AmIResponsive_i8emzh.png)

## User Experience (UX)

### Initial Discussion

Burger Bar is a web application that allows customers to explore and review burgers offered by BurgerBar. Customers can also make table reservations and manage their bookings through the app. The project aims to provide a convenient platform for customers to discover delicious burgers, share their experiences, and plan their dining experiences at the BurgerBar.

#### Key information for the site

* What are reviews on burgers of recent customers.
* Are there any availabe tables for visit.
* Book a table and make sure to have place on arival.
* Keep track of your reservations.

### User Stories

#### Client Goals

* To be able to view the site on a range of device sizes.
* To make it easy for potential members to find out what ios food like in that bar.
* To make it clear for customers what other customers think.
* To allow people to be able book a table withot beeing registerd on page.

#### First Time Visitor Goals

* I want to find out what burger our bar makes and do customers like it.
* I want to be able to navigate the site easily to find information.
* I want to be able to find their Instagram, Facebook, Titter, Youtube profile.

#### Returning Visitor Goals

* I want to find up-to-date information on which tables are free and which tables are occupied every day.
* I want to be able to easily book a table if is free on wished date.

#### Frequent Visitor Goals

* I want to be able to recommend this place if i like it.

## Design

I wanted to choose colours that reflected the environment, so I have chosen a black and some dark pictures because mostly expensive burger bars have that same style, mostly black industrial style. [Homepage](https://res.cloudinary.com/dzwpkjbhq/image/upload/v1689782290/static/summernote/burger_juhqul.jpg)

### Wireframes

Wireframes were created for mobile, tablet and desktop using Balsamiq.


My homepage [Homepage](https://res.cloudinary.com/dzwpkjbhq/image/upload/v1689783744/static/summernote/Homepage_laa3o8.jpg),

Book a table page [Booking](https://res.cloudinary.com/dzwpkjbhq/image/upload/v1689783744/static/summernote/Book_a_table_x78bfv.jpg), 

Booking form [Form](https://res.cloudinary.com/dzwpkjbhq/image/upload/v1689783743/static/summernote/Bookatableform_mvejwa.jpg),

## Features

* Customer Reviews: Users can read reviews left by other customers, helping them make informed decisions about their burger choices. They can also leave their own reviews to share their experiences and recommendations.

* Table Reservations: Customers can make table reservations for their preferred date and time. Reservation details include the selected table, date, customer name, email, and an optional comment.

* Table Availability: Customers can browse dates and check the occupancy of tables for each specific date. This feature allows them to plan their dining experience in advance and choose the desired date based on table availability.

* Reservation Management: Registered users have the added advantage of managing their reservations. They can edit or delete their existing reservations, providing flexibility and convenience in case of any changes. Upon successful registration, users receive an automatic email confirmation.

* User Registration: Customers can create an account by registering with their email. 


### General features on each page

The homepage of my website is designed primarily for browsing reviews and comments on various products. However, main feature revolves around an intuitive table booking system. User has the freedom to choose any desired date and instantly view the availability of tables. Should he wish to secure a table, he can conveniently make a reservation online.

If user is not registered on my website, he'll have to provide an email address. Once he does so, an automatic confirmation will be sent to his email upon successful booking. On the other hand, if user is a registered, he will find his pending reservations displayed beneath the restaurant image. This grants him the ability to modify or cancel his bookings effortlessly.

My aim is to ensure a seamless and enjoyable dining experience for all my users, combining the convenience of online booking with easy management of reservations.

### Future Implementations

One of the key additions will be the inclusion of captivating pictures and videos showcasing our delectable burgers. I believe that visual elements play a crucial role in enticing users and creating an immersive experience.

To further engage my users, I plan to incorporate a rating system for each burger item displayed on the website. This will enable users to express their satisfaction and provide valuable feedback. I look forward to reading the comments that users will leave under each picture or video, as it will help us understand their preferences and improve our offerings.

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. I have achieved this by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text - such as the review ratings for books & footer icons.
* Ensuring that there is a sufficient colour contrast throughout the site.
* Ensuring menus are accessible by marking the current page as current for screen readers.

- - -

## Technologies Used

### Languages Used

HTML and CSS were used to create this website.

### Frameworks, Libraries & Programs Used

Balsamiq - Used to create wireframes.

Git - For version control.

Github - To save and store the files for the website.

Bootstrap Version 4.6 - The framework for the website. Code for the navigation bar, carousel, cards and form were used and modified. Additional CSS styling was also implemented in style.css.

Google Fonts - To import the fonts used on the website.

Font Awesome - For the iconography on the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

[Favicon.io](https://favicon.io/) To create favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.


## Deployment & Local Development

### Deployment

Github Pages was used to deploy the live website. The instructions to achieve this are below:

1. Log in (or sign up) to Github.
2. Find the repository for this project, restaurant-reservations.
3. Click on the Settings link.
4. Click on the Pages link in the left hand side navigation bar.
5. In the Source section, choose main from the drop down select branch menu. Select Root from the drop down select folder menu.
6. Click Save. Your live Github Pages site is now deployed at the URL shown.

### Local Development

#### How to Fork

To fork the restaurant-reservations repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, Wulle91/restaurant-reservations.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the restaurant-reservations repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Wulle91/restaurant-reservations.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

- - -
## Testing


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| BurgerBar Logo & Title | When clicked the user will be redirected to the home page. | Clicked Logo and title | Redirected to the home page. | Pass |
| Home Page Link | When clicked the user will be redirected to the home page.| Clicked link | Redirected to the home page. | Pass |
| BookaTable Link | When clicked the user will be redirected to the book a table page. | Clicked link | Redirected to the bookshelves page | Pass |
| Log in Link (Only shown if user not in session) | When clicked the user will be redirected to the log in page. | Clicked link | Redirected to the log in page | Pass |
| Register Link (Only shown if user not in session) | When clicked the user will be redirected to the register page. | Clicked link | Redirected to the register page  | Pass |
| Log out Link (Logged in users only) | When clicked the user will be redirected to the home page and a flash message displayed to let the user know they have been logged out successfully. | Clicked link |Redirected to the home page and a flash message displayed to let me know I have been logged out | Pass |
| `Footer` |
|  |  |  |  |  |
| Socialaccoutn linka | When clicked the user will be redirected to socialaccount profile. | Clicked Logo and title | Redirected to page. | Pass |
| `Home Page` |
|   |   |   |   |
| Review Field | Any information entered should be saved to the database and displayed on homepage | Text entered | Text saved to the database | Pass |
| Delete Review | Previously saved review should display here. Any information entered should be deleted from database and homepage | Deleted review.| Review not showing on homepage | Pass |
| `Log in Page` |
| Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
| Password input empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | tooltip tells me this field is required |  Pass |
| log in button | Saves the user to session and redirects to the home page. Title message shown welcoming the user | Submitted form | Redirected to the profile page and flash message shown | Pass |
| Incorrect username or password used | A flash message should display saying username/password incorrect - this is defensive programming - not letting user know which input is incorrect | Incorrect username/password entered | Message flashes to let the user know they have entered an incorrect username/password | Pass |
| Link to register page |  This should redirect the user to the register page | Clicked link | Redirected to the register page | Pass |
| `Register Page` |
| | | | | | |
| Username input | The username should be 5 characters minimum | Entered username less than 5 characters long | tooltip lets the user know they have not entered enough characters | Pass |
| Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Username input | If username is in use, message should flash to user | entered an in use username | Message flashed to say username already in use | Pass|
| Email input | The email input should include an email address  | Entered plain text | Tooltip tells user to use an email address here | Pass |
| Email input - empty | The email is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Password input | This field should be at least 8 characters long, letters and numbers | Entered password less than 8 characters long | Tooltip tells user the password should be at least 8 characters long | Pass |
| Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Register button | Should redirect user to the log in page and a registration successful message flashed | Created new user and submitted form | Redirected to the log in page and message flashed | Pass |
| `Book a Table Page` |
|   |   |   |   |  |
| Search date feature | A search is performed when the user choses a date | Date chosen | The search returns available tables on that date | Pass |
| Search feature. - Error | If you click table before choosing date | Clicked on table first | Get the message to choose a date fiste | Pass |
| Table feature. - Error Occupied | You cant click on the red tables | Clicked on red table | Get the message that table is occupied | Pass |
| Table selection | Click on the tables opens reservation form window | Clicked on table | Form pops up | Pass |
| Table booking -non registered users | Fill the form and submit, should get confirmation email | Form submited | Got confirtmation email | Pass |
| Table selection - registered users | Fill the form and submit, should get confirmation email and date displayed under restauran image | form submited | Got confirtmation email and my date is displayed under restaurant image | Pass |
| Edit reservation form | Click on edit button next to reservation form should pop up| Clicked on edit | Form opend | Pass |
| Edit reservation| Form is populated with existing data, user should be able to change his pohone number or aditional comment to reservation | Changed phone number | Number changed| Pass |
| Delete reservation| Delete reservation deletes it form database adn my list of reservations | Deleted reservation | Reservation not displayed | Pass |

## Bugs

- In my initial attempt to create a reservation system, I made the decision to develop two separate models for dates and reservation details. It was my first time working on such a project, and I wasn't certain about the best approach. My main objective was to allow users to filter only occupied tables based on selected dates, hence the separate model.

However, as i beggan to manipulate data, I realized that it would have been more efficient and streamlined to have a single model handling both the dates and reservation details. The use of two models caused complications, particularly with different id numbers, which led to unnecessary complexities.

Overall, this experience has taught me the importance of carefully considering the project requirements and choosing the most appropriate approach from the beginning. By learning from this setback, I am confident that I will be able to create a more cohesive and effective reservation system in the future.

- After reviewing the issue, I discovered that upon refreshing the page, the same action was being performed again. To address this problem, I implemented a redirect in the view function after the creation process. This simple addition resolved the issue and ensured that duplicate actions were not performed upon page refresh.

- I encountered an issue with the CSS not being applied to my deployed page on Heroku. It resulted in the page appearing without any styling. After investigating the problem, I discovered that I had mistakenly misplaced the static folder. Instead of placing it in the top directory, it was located inside one of the app folders. Once I made this adjustment, everything worked as expected, and the CSS styles were successfully applied to the deployed page.

## Credits

- Stack Overflow (www.stackoverflow.com)
- YouTube tutorials (mention specific channels or creators)
- Various websites and online resources (mention specific websites or resources)

### Code Used

I used our walktrought project as a template, I changed all the moels and adjusted it to my needs. I look for ideas on StackOverflow, how they solved various problems i encounterd in my project.


