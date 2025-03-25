import pytest

@pytest.mark.anyio
async def test_sizes(async_client):
    client = async_client
    size_name = "M"

    # get sizes (None)
    response = await client.get("/size")
    assert response.status_code == 404
    assert response.json() == {"detail": "No objects found"} 

    # add size
    data={"name":size_name}
    response = await client.post("/size", json=data)
    assert response.status_code == 201
    size_id = response.json()["id"]
    assert response.json()["name"] == size_name

    # get size
    response = await client.get(f"/size/{size_id}")
    assert response.status_code == 200

    # update size
    data={"name":"shirts"}
    response = await client.put(f"/size/{size_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "shirts", "id": size_id}

    # get all categories (One)
    response = await client.get("/size")
    assert response.status_code == 200  
    assert len(response.json()) == 1 

    # delete size
    response = await client.delete(f"/size/{size_id}")
    assert response.status_code == 200
    assert response.json() == size_id