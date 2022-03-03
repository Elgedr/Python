# NB! For a more beautiful output of the JSON, you can install this extension https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=ru 



### Create a category
Firstly, you should create a category.

- Use http://localhost:8080/categories  and choose a POST method

- For creating a new category, you should write the category’s name. Press “Body” then choose “raw” and choose ‘“JSON”.


- Write category’s name like this 
`{
“categoryName”: “wanted category name”
}`

- Press “Send”

If you try to create the category with the existing name you will get the error “Category already exists!”

### Create a product
- For this, use http://localhost:8080/categories and choose a POST method
- Repeat all steps from “create a category”, write parameters for a new product like that:
`{
“productName”: “wanted product name”,
“productDescription”: “wanted product description”
}`
- As every product has a category, you should give a category id the product belongs to. Choose “Params”, write under the key categoryId and tick this key. As a value write needed category Id



### Get all categories
- Use http://localhost:8080/categories and choose a GET method
- Press “Send”
- Or just type  http://localhost:8080/categories in the search box and you will get something similar to this


### Get all products
- Use http://localhost:8080/categories and choose a GET method
- Press “Send”
- Or just type  http://localhost:8080/categories in the search box and you will get something similar to this



### Update category’s name
- Use http://localhost:8080/categories/{id} and choose a PUT method
- Instead of {id} in the URL, write the id of the category to be updated
- In params under the “Key” write the “name”(field to be changed) and under the “Value” wanted new name value
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


### Delete product
- Use http://localhost:8080/products/{id} and choose a DELETE method
- Instead of {id} in the URL, write the id of the product to be deleted
- Press “Send”
You will get deleted category’s Id
