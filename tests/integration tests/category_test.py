import pytest

@pytest.mark.anyio
async def test_categories(async_client):
    
    client = async_client
    category_name = "jeans"

    response = await client.get("/category")
    assert response.status_code == 404
    assert response.json() == {"detail": "No objects found"} 

    # add category
    data={"name":category_name}
    response = await client.post("/category", json=data)
    assert response.status_code == 201
    category_id = response.json()["id"]
    assert response.json()["name"] == category_name

    # get category
    response = await client.get(f"/category/{category_id}")
    assert response.status_code == 200

    # update category
    data={"name":"shirts"}
    response = await client.put(f"/category/{category_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "shirts", "id": category_id}

    # get all categories (One)
    response = await client.get("/category")
    assert response.status_code == 200  
    assert len(response.json()) == 1 

    # delete category
    response = await client.delete(f"/category/{category_id}")
    assert response.status_code == 200
    assert response.json() == category_id