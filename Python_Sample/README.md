Python Sample App
===============

Works with Python 2.7.3 / 2.7.6 (not tested for Python 3)


---------------------------------


Mac setup
======
Follow these instructions to set up Python and your virtual environment on your Mac:

http://docs.python-guide.org/en/latest/starting/install/osx/

If you are running Mavericks, it comes with Python 2.7 out of the box.


To run the program
===
(Written after the $> are the commands to be typed in the terminal)

In the main application folder, create your virtual environment:

$> virtualenv env

Once created, activate your virtual environment:

$> . env/bin/activate

Then install the requirements file. This is necessary for the application to run:

$> pip install -r requirements.txt

Run the application:

$> python app.py

In your browser, point the URL to:

localhost:5000 or 127.0.0.1:5000

The application should be running in your browser. Any changes made will be reflected in the terminal -- debug mode is on to help you troubleshoot / locate errors.


---------------------------------


Windows setup
======
Follow these instructions to set up Python and your virtual environment in Windows:

http://docs.python-guide.org/en/latest/starting/install/win/


To run the program
===
(Written after the $> are the commands to be typed in the command prompt window)

In the main application folder, create your virtual environment:

$> virtualenv env

Once created, activate your virtual environment:

$> env\Scripts\activate

Then install the requirements file. This is necessary for the application to run:

$> pip install -r requirements.txt

If this does not work, install the requirements individually. Open the requirements.txt file and type the following commands in:

$> pip install Flask
$> pip install requests

Flask should come bundled with Jinja2, MarkupSafe, Pygments, Werkzeug, itsdangerous. If this does not install together, then install them individually as well:

$> pip install Jinja2
$> pip install MarkupSafe
$> pip install Pygments
$> pip install Werkzeug
$> pip install itsdangerous

Run the application:

$> python app.py

In your browser, point the URL to:

localhost:5000 or 127.0.0.1:5000

The application should be running in your browser. Any changes made will be reflected in the command window prompt -- debug mode is on to help you troubleshoot / locate errors.