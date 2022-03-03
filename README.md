# API documentation


### NB! For a more beautiful output of the JSON, you can install this extension https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=ru

### Entity relationship diagram

![Screenshot 2022-03-04 001946](https://user-images.githubusercontent.com/73361292/156662675-3cc1f06a-e367-4673-9025-c579bf7cd5d0.png)



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
