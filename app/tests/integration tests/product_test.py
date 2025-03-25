import pytest

@pytest.mark.anyio
async def test_product(async_client):
    client = async_client
    
    # create category and size
    response = await client.post("/size", json={"name":"M"})
    size_id = response.json()["id"]

    response = await client.post("/category", json={"name":"shirts"})
    category_id = response.json()["id"]

    # create json data input
    data = {
        "image": "image.jpg",
        "name": "shirt",
        "description": "cool shirt",
        "price": 100,
        "rating": 5,
        "amount": 10,
        "category_id": category_id,
        "size_id": size_id
}

    # get products (None)
    response = await client.get("/product")
    assert response.status_code == 404
    assert response.json() == {"detail": "No objects found"}

    # add product
    response = await client.post("/product", json=data)
    assert response.status_code == 201
    product_id = response.json()["id"]
    assert response.json()["name"] == data["name"]

    # get product
    response = await client.get(f"/product/{product_id}")
    assert response.status_code == 200

    # update product
    data["amount"] = 9
    response = await client.put(f"/product/{product_id}", json=data)
    assert response.status_code == 200
    assert response.json()["amount"] == data["amount"]
    assert response.json()["name"] == data["name"]

    # get all categories (One)
    response = await client.get("/product")
    assert response.status_code == 200  
    assert len(response.json()) == 1 

    # delete product
    response = await client.delete(f"/product/{product_id}")
    assert response.status_code == 200
    assert response.json() == product_id

    # delete category and size
    await client.delete(f"/size/{size_id}")
    await client.delete(f"/category/{category_id}")