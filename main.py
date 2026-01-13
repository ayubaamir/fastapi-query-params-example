from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

#Here we will create simple api for hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Here we will write a simple api for about 

@app.get("/about")
def about():
    return {"about": "This is a simple FastAPI application."}

# Here we will create api for view 

@app.get("/view")
def view():
    return {"view": "This is the view endpoint."}

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description='sort on the basis of height, weight and bmi'),
    order: str = Query('asc', description='order can be asc or desc')
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field, select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order, select between 'asc' and 'desc'")

    data = load_data()  # your function to load patients
    sort_order = True if order == 'asc' else False
    sorted_patients = sorted(data['patients'], key=lambda x: x.get(sort_by, 0), reverse=not sort_order)
    
    return sorted_patients
 