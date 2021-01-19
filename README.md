a. set up the project directory:
<ol>
  <li>run <code>python3 -m venv env</li></code>
  <li>run <code>source env/bin/activate</li></code>
  <li>run <code>pip3 install -r requirements.txt</li></code>
 </ol>
b. start your mongodb server using: <br>
  <code>mongod --dbpath ./db</code>

c. run the django project: <br>
  <code>python manage.py runserver</code>
