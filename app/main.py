from fastapi import FastAPI
from app.utils.swagger_params import VERSION, DESCRIPTION, CONTACTS

app = FastAPI(
    title="Joke API",
    description=DESCRIPTION,
    version=VERSION,
    contact=CONTACTS,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
