# EMSEC challenge solution
* ### This code is a Python script that implements a RESTful API using the Flask web framework. The API interacts with a MongoDB database, which stores data in the form of "documents." The API allows users to perform basic CRUD (create, read, update, and delete) operations on the data in the database.

* #### The API contains the following endpoints:

1. #### / - A GET request to this endpoint will retrieve all the data in the database and return it as a JSON response.

2. #### /<name> - A GET request to this endpoint with a specific name as a parameter will retrieve the data for the corresponding user with that name and return it as a JSON response.

3. #### /postData - A POST request to this endpoint will insert new data into the database. The data is passed as a JSON object in the request body.

4. #### /deleteData/<name> - A DELETE request to this endpoint with a specific name as a parameter will delete the data for the corresponding user with that name from the database.

5. #### /update/<name> - A PUT request to this endpoint with a specific name as a parameter will update the data for the corresponding user with that name in the database. The new data is passed as a JSON object in the request body.

6. #### /api/users - A GET request to this endpoint with an optional "page" parameter will retrieve a portion of the data in the database. This is an example of implementing pagination.

7. #### /api/users/export - A GET request to this endpoint will retrieve all the data in the database and convert it to a CSV file, which will be returned as a response.

* ### The code uses the PyMongo library to interact with the MongoDB database and the Flask-CORS library to handle cross-origin resource sharing (CORS) issues. The script starts by initializing a Flask application and setting up the necessary configurations, including a MongoDB URI to connect to  database and CORS headers.


 * ### The code also implements error handling and debugging, which can be enabled by setting the debug argument to True when starting the Flask application.




