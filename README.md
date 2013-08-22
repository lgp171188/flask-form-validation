Form validation in Flask
========================

This project demonstrates form validation using Flask web framework.
On loading the page with URL / a form is displayed to the user. The
form contains the fields for 'Name', 'Email', 'Gender', 'Username',
'password'. When the user enters the data and submits the data via 
POST method, it is submitted to the same URL and the server-side code
handling the POST request for the URL, extracts the form data from
the request and validates each field for valid data and raises 
appropriate error messages if the data is invalid. If the data 
entered is valid, the view renders a success template that displays
the data entered by the user. Regular expression is used to validate
the email address entered.