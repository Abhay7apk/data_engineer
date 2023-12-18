Prerequisites
1. Install Docker desktop for windows. In case of linux, install docker and docker-compose.
2. Browser is required to test react frontend.

Tasks

1. Get Docker compose started. Fix all bugs to get the application up and running.
2. Modify app.py to create postgres table Item before the app starts and populate with two items
 - name="Corn", quantity=10
 - name="Mango", quantity=100
3. Debug code and Run frontend localhost:3000 (try 127.0.0.1:3000 if it doesn't work) so that it displays all items.
4. Modify app.py to create a POST and DELETE request which adds and removes item respectively.
5. Remove Mango and add Guava (Quantity:50) using CURL or Postman (screenshot).
6. Rerun frontend and capture screenshot.

Evaluation

1. Successful start of react frontend using docker rewards 40 points.
2. Successful implementation & execution of POST and DELETE route awards 30 points each.
3. Addition of unit tests is worth additional brownie points.