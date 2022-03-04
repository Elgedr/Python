# API documentation

## How to deploy the application?

- Open project in IntelliJ IDEA or another IDE 
- In file application properties write your mysql login and password.(usually by default it is root)

### Firs variant via  MySQL Workbench
You can download MySQL here https://www.mysql.com/downloads/ 
- Go to the MySQL Workbench
- 1. Launch MySQL Workbench and click the + button to open the Setup New Connection wizard

![Screenshot 2022-03-04 200751](https://user-images.githubusercontent.com/73361292/156818277-42d43103-fe7e-4590-967b-e82af36c4e30.png)

- 2. Enter the name for the connection and username, then click Test Connection. Enter the password in the dialog asking for the password

![Screenshot 2022-03-04 201032](https://user-images.githubusercontent.com/73361292/156818673-9a533966-5a52-4f01-8c7f-61b43e61646f.png)

- 3. In the MySQL Workbench window that opens, click the Create a new schema in the connected server button on the main toolbar. Then enter the schema name (adcash), and click Apply

![Screenshot 2022-03-04 201322](https://user-images.githubusercontent.com/73361292/156818950-ed3d3de1-920e-4ad0-929b-3a2a794bfc67.png)

- 4. In the Apply SQL Script to Database window that opens, click Apply. Then click Finish

![Screenshot 2022-03-04 201519](https://user-images.githubusercontent.com/73361292/156819192-a6fdd066-8331-4b00-bec0-d33dc6566d66.png)

- Run project in Inteliji clicking on Run
 ![Screenshot 2022-03-04 202010](https://user-images.githubusercontent.com/73361292/156819835-77e7c25b-6163-4698-9f43-4372492460fb.png)
 
 ### Second variant via MySQL Command Line Client
- Run the client
- Enter your password
- Execute the create database command. Database name is adcash
![Screenshot 2022-03-04 202415](https://user-images.githubusercontent.com/73361292/156820421-65781bc5-66bb-4af2-b3b1-a7c808551a7a.png)


### Entity relationship diagram

![Screenshot 2022-03-04 001946](https://user-images.githubusercontent.com/73361292/156662675-3cc1f06a-e367-4673-9025-c579bf7cd5d0.png)



## You can test api using Postman. You can download it here https://www.postman.com/downloads/postman-agent/ 
### NB! For a more beautiful output of the JSON, you can install this extension https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=ru
In Postman go to Workspaces -> My Workspace -> press + . 
![Screenshot 2022-03-04 202810](https://user-images.githubusercontent.com/73361292/156820921-f107e33d-28be-4adc-9a5c-22b38f56b90e.png)

### Create a category
Firstly, you should create a category.

- Use http://localhost:8080/categories  and choose a POST method

![unnamed (1)](https://user-images.githubusercontent.com/73361292/156654179-32841d71-93aa-43e3-9eb5-f463d8487118.png)

- For creating a new category, you should write the category’s name. Press “Body” then choose “raw” and choose ‘“JSON”.

![unnamed](https://user-images.githubusercontent.com/73361292/156654271-fa11e09e-91fa-4969-9723-9d4be4271f56.png)

- Write category’s name like this 
`{
“categoryName”: “wanted category name”
}`

- Press “Send”

If you try to create the category with the existing name you will get the error “Category already exists!”
![unnamed (2)](https://user-images.githubusercontent.com/73361292/156654375-3e962f06-0e30-4260-b73a-7d8c51a60bce.png)

### Create a product
- For this, use http://localhost:8080/products and choose a POST method
- Repeat all steps from “create a category”, write parameters for a new product like that:
`{
“productName”: “wanted product name”,
“productDescription”: “wanted product description”
}`
- As every product has a category, you should give a category id the product belongs to. Choose “Params”, write under the key categoryId and tick this key. As a value write needed category Id

![unnamed (3)](https://user-images.githubusercontent.com/73361292/156654455-a36b0772-b5cf-433b-bea9-0bd9f3267590.png)




### Get all categories
- Use http://localhost:8080/categories and choose a GET method
- Press “Send”
- Or just type  http://localhost:8080/categories in the search box and you will get something similar to this

![unnamed (4)](https://user-images.githubusercontent.com/73361292/156654581-622b976a-00f5-44ec-abe9-a0bf6419d3b6.png)



### Get all products
- Use http://localhost:8080/products and choose a GET method
- Press “Send”
- Or just type  http://localhost:8080/products in the search box



### Update category’s name
- Use http://localhost:8080/categories/{id} and choose a PUT method
- Instead of {id} in the URL, write the id of the category to be updated
- In params under the “Key” write the “name”(field to be changed) and under the “Value” wanted new name value

![unnamed (7)](https://user-images.githubusercontent.com/73361292/156654760-ce325645-3495-4eec-9b54-34c09bc2edde.png)
- Press “Send”

You will get a product with a changed name


### Update product’s name

- Use http://localhost:8080/products/{id} and choose a PUT method
- Instead of {id} in the URL, write the id of the product to be updated
- In params under the “Key” write the “name”(field to be changed) and under the “Value” wanted new name value
- Press “Send”

You will get a product with a changed name


### Delete category
- Use http://localhost:8080/categories/{id} and choose a DELETE method
- Instead of {id} in the URL, write the id of the category to be deleted
- Press “Send”
You will get deleted category’s Id

![unnamed (8)](https://user-images.githubusercontent.com/73361292/156654763-fcfef683-eb60-4c2b-9939-99bf05c09aa2.png)


### Delete product
- Use http://localhost:8080/products/{id} and choose a DELETE method
- Instead of {id} in the URL, write the id of the product to be deleted
- Press “Send”
You will get deleted category’s Id

### Get products by category
- Use http://localhost:8080/products/category/{category} and choose a GET method
- Instead of {category} in the URL, write the category of the products you want to get

## Also, you can get a product or category by id using GET method and http://localhost:8080/products/{id} or http://localhost:8080/categories/{id}
