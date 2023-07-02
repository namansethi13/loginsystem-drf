# loginsystem-drf


<h1>PROJECT<h1>
A User Authentication System using Django Rest framework and token based authentication
<h2>Tech stack</h2>
  django rest framework
<h2>How to run locally</h2>
<ul> 
<li>Pull the github repo</li>
<li>Install the requiremnets.txt file using pip install -r requirements.txt</li>
<li>Start the server using python manage.py runserver</li>
</ul>

<h1>API Documentation</h1>

  <h2>POST /register - Register a new user</h2>
  <p>Register a new user with the provided information.</p>
  <table>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>username</td>
      <td>string (required)</td>
      <td>The username of the user.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>string (required)</td>
      <td>The password of the user.</td>
    </tr>
    <tr>
      <td>confirm_password</td>
      <td>string (required)</td>
      <td>Confirmation of the password.</td>
    </tr>
    <tr>
      <td>email</td>
      <td>string (required)</td>
      <td>The email address of the user.</td>
    </tr>
    <tr>
      <td>first_name</td>
      <td>string</td>
      <td>The first name of the user.</td>
    </tr>
    <tr>
      <td>last_name</td>
      <td>string</td>
      <td>The last name of the user.</td>
    </tr>
  </table>
  <p><strong>Response:</strong></p>
  <pre>
  {
    "user": {
      "id": &lt;user_id&gt;,
      "username": "&lt;username&gt;",
      "email": "&lt;email&gt;",
      "first_name": "&lt;first_name&gt;",
      "last_name": "&lt;last_name&gt;"
    },
    "token": "&lt;token_value&gt;"
  }
  </pre>

  <h2>POST /login - Log in a user</h2>
  <p>Log in a user with the provided credentials.</p>
  <table>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>username</td>
      <td>string (required)</td>
      <td>The username of the user.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>string (required)</td>
      <td>The password of the user.</td>
    </tr>
  </table>
  <p><strong>Response:</strong></p>
  <pre>
  {
    "expiry": "&lt;expiry_date&gt;",
    "token": "&lt;token_value&gt;"
  }
  </pre>

  <h2>POST /logout - Log out a user</h2>
  <p>Log out the currently logged-in user.</p>
  <p><strong>Headers:</strong></p>
  <pre>
  "Authorization": "Token &lt;token_value&gt;"
  </pre>
  <p>No Response Body.</p>

  <h2>GET /profile - Get the profile of the logged-in user</h2>
  <p>Retrieve the profile information of the currently logged-in user.</p>
  <p><strong>Headers:</strong></p>
  <pre>
  "Authorization": "Token &lt;token_value&gt;"
  </pre>
  <p><strong>Response:</strong></p>
  <pre>
  {
    "id": &lt;user_id&gt;,
    "username": "&lt;username&gt;",
    "email": "&lt;email&gt;",
    "first_name": "&lt;first_name&gt;",
    "last_name": "&lt;last_name&gt;"
  }
  </pre>

  <h2>PUT /profile - Update the profile of the logged-in user</h2>
  <p>Update the profile information of the currently logged-in user.</p>
  <p><strong>Headers:</strong></p>
  <pre>
  "Authorization": "Token &lt;token_value&gt;"
  </pre>
  <p><strong>Body Parameters (optional, at least one field required):</strong></p>
  <table>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>username</td>
      <td>string</td>
      <td>The new username of the user.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>string</td>
      <td>The new password of the user.</td>
    </tr>
    <tr>
      <td>confirm_password</td>
      <td>string</td>
      <td>Confirmation of the new password.</td>
    </tr>
    <tr>
      <td>email</td>
      <td>string</td>
      <td>The new email address of the user.</td>
    </tr>
    <tr>
      <td>first_name</td>
      <td>string</td>
      <td>The new first name of the user.</td>
    </tr>
    <tr>
      <td>last_name</td>
      <td>string</td>
      <td>The new last name of the user.</td>
    </tr>
  </table>
  <p><strong>Response:</strong></p>
  <pre>
  {
    "success": "updated"
  }
  </pre>
