from fastapi import FastAPI


app = FastAPI()


@app.get("/custom/")
def read_custom_message():
    return {"message": "This is a custom message!"}


#
@app.get("/")
def read_root():
    # logger.info("Handling request to root endpoint")
    return {"message": "Hello"}
