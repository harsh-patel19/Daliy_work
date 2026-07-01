from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProductDto(BaseModel):
    id: int
    title: str
    price: int
    qty: int


product = []




# Read All (GET) ...

@app.get("/product")
def get_all_product():
    return product


# Read One Product (GET) ....


@app.get("/product/{id}")
def get_one_product(id:int):
    for oneproduct in product:
        if oneproduct.get("id") == id:
            return oneproduct
    return {"message":"Product not found"}




# create...

@app.post("/create")
def create_product(data: ProductDto):
    product_data = data.model_dump()
    product.append(product_data)
    return {
        "message": "Product created successfully",
        "data": product_data
    }


# update Product ....

@app.put("/product/{id}")
def update_product(id:int,data:ProductDto):
    for index,oneproduct in enumerate(product):
        if oneproduct.get("id") == id:
            product[index] = data.model_dump()
            return {"message":"Product updated successfully","data":product[index]}

    return {"msg":"Product not found"}



# deleted product ...


@app.delete("/product/{id}")
def delete(id:int):
    for index,oneproduct in enumerate(product):
        if oneproduct.get("id") == id:
            delete = product.pop(index)
            return {"product":delete}
        
    return {"error":"error"}