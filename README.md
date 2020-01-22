<h1>Healthy Recipes Online Cookbook</h2>
<hr>
<p>This project aimed to create and build an interactive front-end and backend fully functioning site that responds to the user's actions allowing users to engage with the data of the site actively; using HTML, CSS, JavaScript, Python+Flask and MongoDB. The website will enable users to store and easily access cooking recipes, add new recipes to the site, edit them and delete them. As part of my defensive design, only users that have logged in will have access to add, edit and delete recipes. The site also allows users to locate recipes based on the recipes name, through the search bar located on the recipes page. Alongside the healthy recipes, I have also incorporated a products page showcasing healthy chemical-free cooking products with fully functioning images that users can click on to find more information about the product or to purchase that item. </p>
<h2>UX</h2>
(https://balsamiq.cloud/ssio6j2/pv0hnv0)
<p>The goal for this design was to make it as easy as possible to access information on the site, using a simple, clearly structured layout; that is easy to navigate and use. The colour palette strives for simplicity and consistency. All pages have the same header throughout the site which I made using an image of spices with an overlay that dims the picture slightly, so it doesn't overpower the page and some additional text informing the user of the ability to add recipes. The remaining of the page is white so that the black text and images in the recipes standout.</p>
<ul>The following goals are what I wanted to achieve for this website:
<li>I wanted it to be clear and simple, so users can easily navigate through</li>
<li>I wanted there to be multiple recipes for users to choose from </li>
<li>I wanted a search bar that would help browse through recipes</li>
<li>I wanted my products page to have images that link directly to a purchase page </li>
<li>I wanted only users that are logged in to be able to add, edit or delete recipes so that I knew how many people were logging on and as an added layer of defence so that not just anyone would be able to remove recipes from the site </li>
<li>I wanted users to be able to view all recipes and products without having to log in or register </li>
<li>I want users to be able to use the site on different screen sizes</li>
</ul>
<h2>FEATURES</h2>
<ul>
<li>Recipes page - You can see a brief outline of all the recipes without having to click on them in the recipes page. You can see the title, how long it will take to make, how many people it will serve how difficult it is to make and a brief description of that recipe. If you want the full recipe, click on the title which when hoovered goes blue and is underlined.</li>
<li>Log in- once logged in users can add their own recipes to the recipe collection</li>
<li>Edit & Delete Recipe - Once logged in, users can click on any of the recipes on the recipe page to edit or delete them.</li>
<li>Search bar- Users can use the search bar to search a specific recipe they would like to see</li>
<li>Products- Users can click on any product and be taken to a new page where they can find out more information about that product and purchase if they wish.</li>
<li>Forms- The Add recipe and Edit recipe has required fields, so users have to fill in all the information excluding all the methods but method one to submit (Incase a recipe is short, they may only have one method they want to provide)</li>
<li>Log in- log in has user authentication </li>
<li>Log out- Users can log out and return to the standard view of the site.</li>
</ul>
<h2>FEATURES LEFT TO IMPLEMENT</h2>
<ul>
<li>Pagination- My recipe page would have looked a lot better with pagination.</li>
<li>Reviews section- It would be amazing to have a reviews section on the recipes so other users can have some more insight into the recipe and how others got along.</li>
<li>This project wasn't focused on the user login; it was just added as an extra layer of defence. But I would have liked to spend more time on that and maybe have a page where users can see all the recipes they've created, possibly be able to save ones they want to use in the future and a button to invite friends to the page. </li>
<li>A liked button- which users can use to like recipes</li>
<li>As it is orientated around health, it would be nice to have exact details about the number of calories, sugar, fat and protein in the recipe.</li>
<h2>TECHNOLOGIES USED</h2>
<ul>
<li>HTML</li>
<li>CSS</li>
<li>JAVASCRIPT</li>
<li>PYTHON</li>
<li>FLASK</li>
<li>MONGO DB</li>
<li>SLUGIFY</li>
<li>BOOTSTRAP</li>
<li>MATERLIAZE</li>
<li>AWS CLOUD 9 (Used to write code in)</li>
<li>Balsamiq (Used to create wireframe)</li>
<li>START BOOTSTRAP (Clean Blog Template)</li>
<li>Git</li>
<li>Github</li>
<li>Heroku</li>
</ul>
<h2>TESTING<h2> 
<ul>The site was tested across multiple browsers:
<li>Google Chrome </li>
<li>Internet explorer</li>
<li>Safari </li>
<li>Google</li>
</ul>
<ul>Also, on multiple devices:
<li>iPhone 5-8</li>
<li>iPhone X</li>
<li>Ipad</li>
<li>IPad Pro</li>
<li>Galaxy S5 </li>
<li>Pixel 2</li>
<li>Pixel 2 XL</li>
<li>Mac </li>
<li>Microsoft Surface Pro</li> 
<li>Desktop Computers</li>
</ul>
<p>To ensure compatibility and responsiveness, I also asked friends and family to test it across their devices to make sure it worked properly and was easy to use.</p>

<ul>During Testing stages, I came across a few problems with my code
<li>Navigation - The template was supposed to come with the navbar fully implemented and working as soon as its added to my code. However, when the site was viewed on smaller screens the navbar did not collapse as its supposed to. When you pressed the button you weren't able to see the anything and the button wasn't centered, it had a green colour to the button as well which did not look good. So i changed the css to make it look presentable and fixed all the problems it was having.</li>
<li>Images that users had been adding were being added as the size there image was which made the page look messy and poorly structured. So i implemented a size into css that all images will show up as to stop that from occuring.</li>
</ul>
<h2>DEPLOYMENT</h2>
<p>This project was developed using AWS cloud9, committed to git and pushed to GitHub using the built-in function within cloud 9. My GitHub is linked with Heroku, so anything I pushed to GitHub automatically got deployed to Heroku. I configured my vars in Heroku with ip 0.0.0.0 and port 5000. There are two branches on my Github, so when I pushed my code from git to GitHub i did so by writing git push origin master, so it went straight to the master branch. 
<ul>To run my code locally:
<li>Log into GitHub</li>
<li>Type in the search bar saffiya/cookbook</li>
<li>Next to the find file button, click "Clone or download"</li>
<li>In the Clone with HTTP's section, copy the clone URL for the repository</li>
<li>In your local IDE open Git Bash</li>
<li>Change the current working directory to the location where you want the cloned directory to be made</li>
<li>Type git clone and then paste the URL you copied from the clone with HTTP's section </li>
<li>Press enter and your local clone will be created</li>
</ul>

 </p>
<h2>CREDITS</h2>
<ul>
<li>All recipes and images were from olive magazine</li>
<li>Products images were taken from Greenpan on amazon </li>
<li>The product description on the homepage was from Greenpan on amazon</li>
<li>Login, register, logout code was from MiroslavSvec DCD_lead GitHub code</li>
</ul>
<h2>MEDIA</h2>
<p>The spice image in the header is a purchased image that I got from adobe image</p>
<p>As credited above the recipe images were from olive magazine and the products images were from greenpan on amazon</p>
<h2>ACKNOWLEDGEMENTS</h2>
<ul>
<li>Bootstrap helped me create the search bar</li>
<li>Materialize helped me with my forms and any icons used in the project<li>
<li>StartBootstrap is where I got my template for the project from<li>
<li>I got my login, register and logout code from MiroslavSvec DCD_lead Github code. The code was slightly altered but was from his page.</li>
</ul>
