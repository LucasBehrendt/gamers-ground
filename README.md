# Gamers Ground

Gamers Ground is a B2C e-commerce website for people interested in pc gaming. If you're a hardcore gamer that needs the best gear on the market, we got you covered! Looking for a more affordable option? We have what you need! We will continue to add new products as our stock will grow, so check in regularly to find your favourite gear.

*This project is a fictional e-commerce store that does not generate any revenue or take real orders. To place a mock order, please use the following card number: 4242 4242 4242 4242, with any expiration date in the future. To learn more about how to test the payment system, please visit [Stripe](https://stripe.com/docs/testing)*

[Find the live website here!](https://gamers-ground.herokuapp.com/)

![Responsive Image](static/images/readme-images/responsive-img.png)

# Table of Contents

# User Experience (UX)

The five planes of UX Design was implemented during the planning stage of the project. A summary of each stage is presented below.

## Strategy

### Target audience:

- Younger men and women interested in tech

- People with an interest in pc:s and gaming

- Friends and family looking for gifts to purchase

### User goals:

- Be able to browse through products in an intuitive and easy way

- Find valuable and understandable info about products

- Add multiple products to cart so I can buy more than one product at a time

- Purchase a product with minimal friction and receive confirmation

- Become a member and save my information for future purchases

- See previous orders as a member

- Leave ratings / reviews on products I have purchased

- View other customers ratings / reviews to help make an informed decision on purchasing a product

### Site admin goals:

- Have an easily manageable and trustworthy site

- Be able to add, edit and delete products from the stock

- Be able to edit / delete objectionable reviews left by site users

- If a user breaks site policy and behaves in an ill-mannered way, be able to remove their account

- Have an emailing list set up to promote my site with news and sales etc.

### User Stories

The user stories were implemented in an agile approach when creating the application, developed in order of importance. They were broken up into the following Epics to help with project management.

- #### EPIC: User Authentication / Accounts

  - As a Site User I can register an account so that I can sign in / out when revisiting the site.

  - As a Signed In User I can view and update my information so that I can make sure the correct info is stored on me.

  - As a Signed In User I can delete my account so that no information is stored on me.

  - As a Signed In User I can view previous order information so that I can see the details and make sure the orders are correct.

  - As a Signed In User I can save my info or have my information prefilled at checkout if it's already saved so that my saved info is used, and I don't have to fill it out.

  - As a Signed In User I can reset my password using my email so that I can gain access to my account if I forget my password.

- #### EPIC: User Site Navigation

  - As a Site User I can easily find and view products available so that I can browse products I may want to buy.

  - As a Site User I can click a product and view all info so that I can learn more about the product and see if I want to purchase it.

  - As a Site User I can search for products using keywords so that I can find a specific product I have in mind.

  - As a Site User I can add a filter to the products so that I can find specific products I am looking for.

  - As a Site User I can sort products by name, price, category etc. so that I can find certain / similar products easier.

  - As a Site User I can click on the cart so that I can view the products I have saved for purchase and my total cost.

  - As a Site User I can read other users reviews on products so that I can gain understanding of a products customer satisfaction.

- #### EPIC: User Site Interaction

  - As a Site User I can add products to a cart so that I can save it and purchase more than one product at a time.

  - As a Site User I can see the number of items OR the total cost by the cart icon in the upper right corner when editing my cart so that I know how many items I have added / how much my total is.

  - As a Site User I can edit my saved items on the cart page so that I can change my cart content as I wish.

  - As a Site User I can delete saved items on the cart page so that I can change my cart content as I wish.

  - As a Site User I can expect confirmation on my interactions with the site so that my actions get confirmed.

  - As a Site User I can rate / review products I have purchased so that I can share my product experience with other customers.

  - As a site user I can delete my own review so that I can decide which of my own content is visible, and I can write a new review if I wish.

- #### EPIC: User Checkout

  - As a Site User I can checkout and pay for the products in my cart so that I can buy and receive my newly purchased products.

  - As a Site User I can view details of my order on the checkout page so that I can make sure everything is correct before placing my order.

  - As a Site User I can have my order confirmed after a purchase so that I can be certain my payment was processed successfully.

- #### EPIC: Site Admin

  - As a Site admin I can add products to the site so that I can control the selection of products being sold.

  - As a Site admin I can ** edit products on the site** so that I can make sure the products being sold are correctly represented.

  - As a Site admin I can delete products on the site so that I can control the selection of products being sold.

  - As a Site Admin I can manage reviews posted by customers so that I can make sure no objectionable content is present.

## Scope

The scope of the project was determined by prioritizing to get a Minimum Viable Product deployed, and if time permits, add on additional features. A basic MoSCoW method was implemented on user stories where each user story received a label defining it as either 'Must Have', 'Should Have' or 'Could Have'. They were broken up into epics to gain better project overview and help plan the development process. Both tasks and acceptance criteria were given to each user story to assure that the intended feature was implemented correctly. For further details of tasks and acceptance criteria, and a list of all user stories, see this projects [GitHub Issues Tab](https://github.com/LucasBehrendt/gamers-ground/issues) In general, the higher priority user stories were implemented earlier.

### Core features

-	An inviting landing page that incentivizes the user to explore the site further

-	Products listings where users can search, filter and sort products in a relevant way

-	Products are visually inviting and professionally presented

-	Cart functionality to save multiple items for purchasing before proceeding to checkout

-	Checkout system that gives users a professional and trustworthy feel with confirmation email sent after a placed order

-	Authentication system for site users, where they can save their info and view previous orders

-	User feedback on all interactions with the site, such as adding to cart, signing up, updating cart etc

-	Site admin have full CRUD functionality over products and can control the selection of products entirely (Through site UI)

-	Ratings / review system for customers who wants to give feedback on purchased products

-	Site admin have full CRUD functionality over written reviews and can remove objectionable ones (Through Django Admin panel)

## Structure

The website is structured with simplicity and accessibility in mind, where both shoppers and site admins can intuitively navigate the site. Consistency in structure and layout is evident, to allow site users to gain a recognizable feel of the Gamers Ground brand. Combined with predictable behaviour and layout through all site pages, navigation through the site is a pleasing and positive experience.

### Business Model

The business model is centered around Business-to-Consumer (B2C), where emphasis has been put on provoking a positive response and an easy to use e-commerce platform. Where business customers usually do a lot of research and require large amounts of information about products, often the opposite is true for consumers. The shopping experience is often impulsive and emotionally driven, and a purchase should be as easy and frictionless as possible. To achieve this, a number of interaction designs were kept in mind when structuring the site. The flow of information is kept at a pleasing level to prevent cognitive overload with users. The review system uses a user-friendly star rating system to incentivize users to leave reviews on products. The checkout and payment process have been implemented with minimal friction in mind, and short clicking distances coupled with intuitive navigation are key in creating a frictionless and pleasing shopping experience. The site is fully resposive so users can choose to do their shopping from a device of their own choosing.

### Information Architecture

To facilitate an intuitive and easily navigated site, Information Architecture was considered when structuring the pages throughout the website. Features that help users understand where they are, and where certain information can be found were implemented. Examples of these features include user-friendly urls, that show both the category and the product name when viewing a specific product, a breadcrumb navigation on product list and detail pages for ease of access to other related products, and clear confirmations on all user interactions.

To help facilitate a logical flow of the application during the development process, a simple flowchart / site map was created using [LucidChart](https://www.lucidchart.com/pages/).

<details>

<summary>Flowchart / Site Map</summary>

![Flowchart](static/images/readme-images/flowchart.png)

</details>

## Skeleton

The structure and layout defined above was expressed with the help of wireframes in the planning process. These mock-ups are intended to show the overall layout of all pages within the website. While the wireframes are similar to the finished project, some changes were made during development to better suit content, information architecture, and overall structure.

The authentications system / templates with sign in, sign out, registration, email verification etc. was provided by Allauth. The templates used have only been slightly styled to fit the rest of the site, and therefore no wireframes were made of those pages.

### Wireframes

[Balsamiq](https://balsamiq.com/) was utilized when creating the wireframes below.

<details>

<summary>Desktop wireframes</summary>

Home Page<br>
![Desktop wireframe home](static/images/readme-images/wireframes/Desktop-home.png)

Products Page<br>
![Desktop wireframe products](static/images/readme-images/wireframes/Desktop-products.png)

Product Detail Page<br>
![Desktop wireframe product detail](static/images/readme-images/wireframes/Desktop-product-detail.png)

Cart Page<br>
![Desktop wireframe cart](static/images/readme-images/wireframes/Desktop-cart.png)

Checkout Page<br>
![Desktop wireframe checkout](static/images/readme-images/wireframes/Desktop-checkout.png)

Checkout Success Page<br>
![Desktop wireframe checkout success](static/images/readme-images/wireframes/Desktop-checkout-success.png)

Profile Page<br>
![Desktop wireframe profile](static/images/readme-images/wireframes/Desktop-profile.png)

Add Product Page (site admins)<br>
![Desktop wireframe add product](static/images/readme-images/wireframes/Desktop-add-product.png)

</details>

<details>

<summary>Mobile wireframes</summary>

Home Page<br>
![Mobile wireframe home](static/images/readme-images/wireframes/Mobile-home.png)

Products Page<br>
![Mobile wireframe products](static/images/readme-images/wireframes/Mobile-products.png)

Product Detail Page<br>
![Mobile wireframe product detail](static/images/readme-images/wireframes/Mobile-product-detail.png)

Cart Page<br>
![Mobile wireframe cart](static/images/readme-images/wireframes/Mobile-cart.png)

Checkout Page<br>
![Mobile wireframe checkout](static/images/readme-images/wireframes/Mobile-checkout.png)

Checkout Success Page<br>
![Mobile wireframe checkout success](static/images/readme-images/wireframes/Mobile-checkout-success.png)

Profile Page<br>
![Mobile wireframe profile](static/images/readme-images/wireframes/Mobile-profile.png)

Add Product Page (site admins)<br>
![Mobile wireframe add product](static/images/readme-images/wireframes/Mobile-add-product.png)

</details>

## Surface

The websites surface is designed to be inviting and polished so as to invoke a positive response from users when they land on the home page. Several call to action buttons help incentivize the user to explore the site further. A balanced feel of simplicity and gaming themed design was prioritized, and low friction was always kept in mind during the designing phase.

### Design
- #### Colours

  The colours used on the site are meant to convey a theme of pc gaming with dark / mid grey, complemented with a popping lime / neon green colour for buttons and links. The main background colour is a mid grey colour (#33363f) that goes nicely with the theme and the palette chosen. Sections, cards and header / footer breaks off the background with a darker grey (#212228) that complements each other nicely. The green colour chosen for the buttons and links (#35C71E) help make the website feel more vibrant and catches the users attention straight upon landing on the home page. It also goes very nicely with the grey colours and give good contrast to text / elements. To help product cards and other module sized content stand out and feel more inviting, a solid black (#000) border was added in the later stages of development.

  Where necessary, a red 'danger' colour was implemented to alert users of an action where they would delete data, like a review or their account. The same goes for the site admin links / buttons where appropriate.

  <details>

  <summary>Colour Palette</summary>

  ![Colour palette](static/images/readme-images/colour-palette.png)

  </details>

- #### Imagery

  The images are an important part of mainly the landing page, where large gripping images are meant to convey a sense of gaming enthusiasm and excitement for shoppers. A bootstrap carousel at the very top of the home page shows three eye-catching images of gaming peripherals, and content hinting with a gaming desktop lies just underneath. A nicely laid out grid of categories with accompaning images is found further down, where users easily can find a quick route to their favourite category. Across the other pages, the product images are the main focus, to help keep a clean and minimalistic design. 

- #### Typography

  The font chosen for the site is Rubik, a nicely edgy and well fitting font for gaming and tech content. Both different font sizes and weights have been user throughout the site, and consistency was always kept in mind. If the font isn't imported correctly, Sans-serif will serve as fallback.

# Data Model

## Codebase

The codebase includes the following apps and folders:

- Cart app, for managing adding products to a cart.

- Checkout app, handles the payment system and orders.

- Home app, renders home page and customer service pages.

- Products app, handles creating, storing and rendering products.

- Profiles app, holds the profile model which extends user model.

- Review app, lets users leave a rating and review on products.

- Static folder, holds static files and images.

- Templates folder, holds base, error, allauth and toasts templates.

ADD MORE??

## Models

The database used for the application requires several models which will be defined below. The user authentication system is included in Django Allauth and a User model was therefore already provided. However, this model was extended with a Profile model which you'll also find below.

To get an idea of the relationships and fields required in the models, an ERD (Entity Relationship Diagram) was created using [LucidChart](https://www.lucidchart.com/pages/).

<details>

<summary>Entity Relationship Diagram</summary>

![Entity relationship diagram](static/images/readme-images/erd.png)

</details>

### User Model

- Provied by Django Allauth, users receive a unique ID which serve a FK (Foreign Key) to other models in the database.

- Upon registration, users choose a username, email and password.

- To improve user experience, registration was extended to also include users first and last name. These will then be visible on their profile, as well as pre-filled at checkout.

### UserProfile Model

- Extends User model with delivery information to allow users to save it for future purchases.

- Includes an OneToOneField to User model, which allows the UserProfile model to be created automatically when a new user registered with the help of a post_save signal.

- The remaining fields are delivery information fields, namely phone_number, street_address_1, street_address_2, postcode, city and country.

### Category Model

- Implemented with SEO-friendly urls in mind, this model has a name field and a slug field.

- The slug field is automatically generated when a category is created, and later used in the url when visiting a product / category page.

### Product Model

- Products are assigned a category through an FK to the Category model.

- This model also includes an automatically generated slug field from the name field of the product. Again this makes the url easier to follow.

- A brand and a description field lets shoppers know more about the product and gives them the chance to find products of their favourite brand.

- The product has an image field and price field, as well as a field for rating.

- The rating is updated when a review is posted on the product through a method that calculates the average rating.

### Order Model

- The Order model features a randomly generated order number, and an FK to UserProfile to assign orders to authenticated users.

- Personal info fields include first_name, last_name, email_address and phone_number. These are prefilled with authenticated users info at checkout.

- Delivery info fields include street_address_1, street_address_2, postcode, city and country. Just like the personal info, these will be prefilled with available UserProfile data.

- The fields delivery_cost, order_total and grand_total are set automatically through a method that calculates the total as products are added to the order, and for orders above a certain sum, the shipping fee is removed.

- Lastly a field to hold the Stripe payment intent ID, stripe_pid, makes sure no orders are confused with each other.

### OrderLineItem Model

- Serves as a temporary state for products added to an order, where the FK to the Order model assigns it to a specific order.

- The product field, an FK to the Product model, makes sure the correct product is represented.

- To allow shoppers to purchase more than one of a given product, a quantity field holds the number of line items to be purchased.

- To easily calculate the total cost of an item, the lineitem_total field automatically multiplies product price with the quantity defined above.

### Review Model

- Reviews are assigned a user through an FK to the User model.

- The Product model serves as FK on the product field.

- Choices from 1 to 5 are defined for the rating field to let users give products a rating.

- A review text field allow users to write some thoughts on a product along with their rating.

- The created_on field tells users when a specific review was posted.

# Agile Methodology

To better plan and understand the development process, an agile approach was taken when implementing features. GitHub Projects provides a great way of keeping track of progress made and user stories to develop. By creating a project board on a basic kanban template, the development process can be overviewed and tackled in a proficient and time-effective way. Epics were defined (as GitHub Milestones) to get a sense of the overall aim of the project. Each user story created was then assigned to an Epic and added to the project board. The board features three columns for every step of the development process, Todo, In Progress and Done. As user stories were added to the board, their status was automatically set to Todo. They were then moved to In Progress as the feature was being developed, and finally to Done when it was implemented on the application.

For each user story created, a set of acceptance criteria were defined to help clarify what a specific feature is expected to fulfill for users. Coupled with the acceptance criterias, tasks were assigned as a way of keeping track on what steps would need to be taken in order to implement any given feature. This helped keep an organized and agile mindset on how to get the best result within a reasonable timeframe.

Labels were created and assigned to each user story to help keep track of the importance. The MoSCoW method is a practical way of assigning priority to user stories and helps planning the development of the application. The labels define user stories as either 'Must Have', 'Should Have' or 'Could Have'. While all user stories were completed, this method provided a valuable way of ensuring that the most important features were implemented first.

This agile approach is especially powerful when working in teams, but still made the development process more enjoyable and easier to keep track of when developing alone. To view the project board and all user stories, see [Gamers Ground Project Board](https://github.com/users/LucasBehrendt/projects/2)

<details>

<summary>GitHub Project Board</summary>

![GitHub Project Board](static/images/readme-images/project-board.png)

</details>

# Search Engine Optimization

To help users find the website easier, Search Engine Optimization techniques were employed as part of the development process. Some of these techniques are outlined below.

## Keywords

By researching and implementing the use of keywords that search engines deem authoritative and relevant to the site, better ranking can be achieved. The process of implementing these started with doing research of general topics applicable to the content of the application.

These topics are as follows:

- **Gaming Peripherals**

- **Desktops / Laptops**

- **Brands**

To find as many keywords as possible, a brainstorming session was undertaken with the following result:

**Gaming Peripherals**

- Gaming keyboard

- Gaming mouse

- Best gaming gear

- Gaming accessories

- Best keyboard / mouse for gaming

- Gaming peripherals

- Ergonomic gaming chair

- Mechanical gaming keyboard

- Mechanical wireless keyboard

- Buy affordable gaming peripherals

- Affordable gaming peripherals

- TKL keyboard

**Desktops / Laptops**

- Best desktops for gaming

- Best laptops for gaming

- Gaming pc

- Gaming laptop

- Buy affordable gaming desktop

- Buy affordable gaming laptop

- Gaming pc with rgb

- Affordable laptops for gaming

- Buy desktop for gaming

- Laptop with rgb

- Ultimate gaming rig

- Powerful gaming laptop

- Best gaming pc

- Affordable gaming pc

- Gaming rig

- Computer for gaming

- Budget gaming pc

**Brands**

- Gaming pc brands

- Best brands for pc gaming

- Best gaming gear brand

- Steelseries peripherals

- Razer mouse / keyboard

- Logitech gaming bundle

- Logitech mechanical keyboard

- Razer gaming peripherals

- Razer blade laptop

After careful consideration, and extensive research through both manual google searches and the site [WordTracker](https://www.wordtracker.com/), the list was narrowed down and divided in to short-tail and long-tail keywords. Many of the written down keywords were either too popular and competition-heavy, or not authoritative and relevant to the content of the site. These have not been used consciously for SEO reasons, but will still be present on the site in generic text / content.

The chosen keywords:

**Short tail keywords**

- Gaming peripherals

- TKL keyboard

- Gaming pc

- Gaming laptop

- Steelseries peripherals

- RGB lighting

**Long tail keywords**

- Ergonomic gaming chair

- Mechanical gaming keyboard

- Gaming pc with RGB

- Ultimate gaming rig

- Powerful gaming laptop

- Logitech mechanical keyboard

- Razer gaming peripherals

- Razer blade laptop

These keywords were then used as part of the content in an organic way and should never disturb the flow of the site. Some keywords are present on the landing page, where semantically relevant HTML, such as h1, h2 and strong tags were used to help boost the keywords visibility while avoiding keyword stuffing. Other keywords are present directly in product names or descriptions as part of the natural flow.

An example of these implementations can be seen on the image below.

<details>

<summary>Keywords, Home page</summary>

![Keywords, Home page](static/images/readme-images/keywords-homepage.png)

</details>

## Content

When a user lands on Gamers Ground, the content of the website is meant to be relevant to what the user searched for to find the site. This means that keywords chosen for SEO, should be relevant to the content of the site, and users should expect to have their questions answered by the content. If the content is not useful to site visitors, they are more likely to exit the site as soon as they land on it.

As the user clicks through the site, the layout needs to be easily navigated and pleasing to browse. The content must also be uncluttered and easily digested, and incentivize users to explore other pages of the site. Honest and clear information about products and any additional fees is also important, and gives the site trustworthiness.

Content on the site is free of typos and grammatical errors. Some additional pages for FAQs, Terms & Conditions and Privacy Policy were added to improve the professionalism and trustworthiness of the website.

## Images and Links

To further increase search engine ranking, images used on the site are high quality, relevant and have clear motives. The `alt` attribute of images are, when applicable written with keywords in mind without stuffing or making the `alt` text irrelevant. The product images on the site include an `alt` text with the product name dynamically set. Links to other pages of the application are clear and predictable, while also being relevant to the content of the site. External links have the appropriate `rel` attribute and the only ones present are links to social media platforms. The Facebook link takes users to Gamers Grounds Facebook page created as part of this project, while the other links takes users to the home page of the platform.

## Meta Data

By adding meta tags with keywords and a description for the website, search engines have more ways of finding relevant results, improving the rating. These meta tags were added to the base template:

`
<meta name="keywords" content="gaming peripherals, ergonomic gaming chairs, mechanical gaming keyboards,
    tkl keyboards, gaming pc, gaming laptops, rgb lighting, ultimate gaming rig, powerful gaming laptop,
    steelseries peripherals, logitech mechanical keyboard, razer gaming peripherals, Razer blade laptop">
`

`
<meta name="description" content="Find your next ultimate gaming rig or the new Razer mechanical 
    keyboard at Gamers Ground, your one-stop-shop for all things PC Gaming">
`

## Sitemap.xml File

To help speed up the content discovery of search engines crawling the website, a sitemap.xml file was added to the project by generating it from [XML Sitemaps](https://www.xml-sitemaps.com/). The deployed link was used to generate a list of urls within the site.

On a live project, the sitemap would need to be registered through the Google Search Console. Since this project is for educational purposes only, and won't be deployed to a custom domain, this will not be done for this website.

<details>

<summary>XML Sitemaps</summary>

![XML Sitemaps](static/images/readme-images/xml-sitemaps.png)

</details>

## Robots.txt File

A robots.txt file tells search engine crawlers which URLs the crawler can access on your site. By adding it to the project, pages that contain sensitive information is shielded by excluding it from search engine crawling. It also helps avoid overloading the site with requests.

On a live project, the robots.txt file would need to be tested through the Google Search Console. Again, since this project is for educational purposes only, no further steps will be taken. 

<details>

<summary>Robots.txt file</summary>

![Robots.txt file](static/images/readme-images/robots.png)

</details>

# Marketing

Marketing strategies used for Gamers Ground are SEO, social media marketing, and email marketing.

### Search Engine Optimization

Several SEO marketing strategies were implemented on the site, which are all outlined [here](#search-engine-optimization).

### Social Media Marketing

A Facebook page was created for Gamers Ground to reach a wide and relevant range of potential customers. Social media marketing is free, easy to set up and reach large groups of people. This makes it ideal for a small online business, where a community can be formed and customer loyalty is rewarded. It is also a great way of promoting new products, campaigns and special offers. If there's a budget for it, paid advertisements are also a great way of reaching more consumers through social media. This will not be implemented for Gamers Ground though, since the project is educational.

Gamers Grounds Facebook page can be viewed [here](https://www.facebook.com/Gamers-Ground-111472718360772). *This link may not work as facebook regularly removes inactive business pages.*
<details>

<summary>Gamers Ground Facebook Page</summary>

![Gamers Ground Facebook Page](static/images/readme-images/facebook-gg.png)

![Gamers Ground Facebook Page about](static/images/readme-images/facebook-gg-about.png)

</details>

### Email Marketing

Another great way of marketing a small low-bugdet business is through the use of a mailing list. This is also free, or low cost if the email list grows large, and is easy to implement. Emailing lists are also advantageous for businesses, since visitors who choose to sign up are more likely converted into customers through exclusive offers or similar. Steps to ensure that users do not percieve emails as spam or obtrusive would be taken. In the footer of Gamers Ground visitors can sign up for future newsletters, campaigns and special offers. 

The marketing platform [Mailchimp](https://mailchimp.com/) was used to implement the signup form. When a user submits the form, they receive a notification and their email address is added to the mailing list.

<details>

<summary>Mailchimp</summary>

![Mailchimp Form](static/images/readme-images/mailchimp.png)

![Mailchimp Audience](static/images/readme-images/mailchimp-audience.png)

</details>




# Features
## Features Left to Implement

# Testing
## Validator Testing
## Responsive Testing
## Lighthouse Testing
## Links and Form Testing
## Fixed Bugs
## Known/Unfixed Bugs

# Technologies Used
## Languages
## Programs & Libraries

# Deployment

# Credits
## Code
## Content
## Media
## Acknowledgements



