from fastapi import FastAPI

api = FastAPI()


@api.get("/docs")
def hello():
  """
  Hello World App Function
  """
  return {"hello" : "World"}