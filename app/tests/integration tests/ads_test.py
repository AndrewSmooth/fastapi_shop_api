import pytest

@pytest.mark.anyio
async def test_ads(async_client):
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
    
    response = await client.post("/product", json=data)
    product_id = response.json()["id"]

    # get ads (None)
    response = await client.get("/ads")
    assert response.status_code == 404
    assert response.json() == {"detail": "No objects found"}

    data = {
        "path": "image.jpg",
        "product_id": product_id,
    }

    # add ad
    response = await client.post("/ads", json=data)
    assert response.status_code == 201
    ad_id = response.json()["id"]
    assert response.json()["path"] == data["path"]
    assert response.json()["product_id"] == data["product_id"]

    # get ad
    response = await client.get(f"/ads/{ad_id}")
    assert response.status_code == 200

    # update ad
    data["path"] = "image2.jpg"
    response = await client.put(f"/ads/{data["product_id"]}", json=data)
    assert response.status_code == 200
    assert response.json()["path"] == data["path"]
    assert response.json()["product_id"] == data["product_id"]

    # get all categories (One)
    response = await client.get("/ads")
    assert response.status_code == 200  
    assert len(response.json()) == 1 

    # delete ad
    response = await client.delete(f"/ads/{ad_id}")
    assert response.status_code == 200
    assert response.json() == ad_id

    # delete product, category and size
    await client.delete(f"/product/{product_id}")
    await client.delete(f"/size/{size_id}")
    await client.delete(f"/category/{category_id}")