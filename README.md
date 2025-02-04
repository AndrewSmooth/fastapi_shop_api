# FastAPI Shop API

FastAPI Shop API is FastAPI based backend api for online clothing store. It can be used to connect with frontend frameworks.The project implements a layered architecture

## Features

- CRUD operations with products, categories of products, sizes and product's additional images
- Uploading images
- Asynchronous tests

## Deploy

Follow the next steps:

### Requirements

- Install fastapi and requirements from requirements.txt
- Make `.env` and `.test.env` files with personal settings
- Connect postgres. Create work db and test db. Configure their names in `.env`s

### Steps

1. Clone repo:

   ```bash
   git clone https://github.com/AndrewSmooth/fastapi_shop_api.git
   ```

2. Go to the project directory:

   ```bash
   cd fastapi_shop_api
   ```

3. Run command:

   ```bash
   uvicorn src.main:app
   ```

4. You can test it at: [http://localhost:8000](http://localhost:8000).

5. For tests use:

    ```bash
   ENV=.test.env uvicorn src.main:app
    ```
   Then in split terminal run:

    ```bash
   ENV=.test.env pytest
    ```

## Usage Examples

### Get product with id = 1

```
GET http://localhost:8000/product/1
```

### Create product category 

```
POST http://localhost:8000/category

Request Body:
{
  "name": "shirts"
}
```

### Create product

```
GET http://localhost:8000/product

Request Body:
{
  "image": "/home/image.png",
  "name": "white shirt",
  "description": "pretty white short",
  "price": 100,
  "rating": 5,
  "amount": 30,
  "category_id": 1,
  "size_id": 2
}
```
More information about response formats / possible errors can be found in Swagger UI at:

```
GET http://localhost:8000/docs
```