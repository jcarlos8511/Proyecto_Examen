from fastapi import FastAPI


app = FastAPI()

@app.post("https://your-app-url-onrender-com.com")

def process_order():
    return{'order':[
        {"id":1, "item":"Laptop", "quantity":1, "price":999.99, "status":"completed"},
        {"id":2, "item":"Smartphone", "quantity":2,"price":499.95, "status":"pending"},
        {"id":3, "item":"Headphones", "quantity":3,"price":99.90, "status":"completed"},
        {"id":4, "item":"Mause", "quantity":4,"price":24.99, "status":"canceled"}
        ], 
        "criterion":"completed"
    }

    