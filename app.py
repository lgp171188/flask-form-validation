import os
# We require 're' module for validating email address with regular expression
import re

# Using Flask since Python doesn't have built-in session management
# 'request' provides access to the incoming request data
# 'render_template' renders the template with the given parameters

from flask import Flask, session, request, render_template

# Create a flask app object using a unique name. In this case we are
# using the name of the current file
app = Flask(__name__)

# Generate a secret random key for the session
app.secret_key = os.urandom(24)

def is_email_address_valid(email):
    """Validate the email address using a regex."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True

# This view method responds to the URL / for the methods GET and POST
@app.route('/', methods=['GET','POST'])
def index():
    # Initialize the errors variable to empty string. We will have the error messages
    # in that variable, if any.
    errors = ''
    if request.method == "GET": # If the request is GET, render the form template.
        return render_template("index.html", errors=errors)
    else: 
        # The request is POST with some data, get POST data and validate it.
        # The form data is available in request.form dictionary. Stripping it to remove
        # leading and trailing whitespaces
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        # Since gender field is a radio button, it will not be available in the POST
        # data if no choice is selected. If we try to access it in such a scenario, we
        # will get an exception, so we are using the get() method on the 'form' dictionary
        # specify a default value if the key doesn't exist in the dictionary.
        gender = request.form.get('gender', '')
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        # Check if all the fields are non-empty and raise an error otherwise
        if not name or not email or not gender or not username or not password:
            errors = "Please enter all the fields."
        if not errors:
            # Validate the email address and raise an error if it is invalid
            if not is_email_address_valid(email):
                errors = errors + "Please enter a valid email address"
        if not errors:
            # If there are no errors, create a dictionary containing all the entered
            # data and pass it to the template to be displayed
            data = {'name' : name,
                    'email' : email,
                    'gender' : gender,
                    'username' : username,
                    'password' : password
                    }
            # Since the form data is valid, render the success template
            return render_template("success.html", data=data)
        # Render the form template with the error messages
        return render_template("index.html", errors=errors)

# This is the code that gets executed when the current python file is
# executed. 
if __name__ == '__main__':
  # Run the app on all available interfaces on port 80 which is the
  # standard port for HTTP
	app.run( 
        host="0.0.0.0",
        port=int("80")
  )