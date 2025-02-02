from tests.conftest import TEST_DATABASE_URL
import os
from src.core.config import settings

def test_categories(client):
    category_name = "jeans"

    # assert TEST_DATABASE_URL=="TEST"
    assert os.getenv("MODE")=="TEST"

    # get all categories (None)
    response = client.get("/category")
    assert response.status_code == 404
    assert response.json() == {"detail": "No objects found"} 

    # add category
    data={"name":category_name}
    response = client.post("/category", json=data)
    assert response.status_code == 201
    category_id = response.json()["id"]
    assert response.json()["name"] == category_name

    # get category
    response = client.get(f"/category/{category_id}")
    assert response.status_code == 200

    # update category
    data={"name":"shirts"}
    response = client.put(f"/category/{category_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "shirts", "id": category_id}

    # get all categories (One)
    response = client.get("/category")
    assert response.status_code == 200  
    assert len(response.json()) == 1 

    # delete category
    response = client.delete(f"/category/{category_id}")
    assert response.status_code == 200
    assert response.json() == category_id