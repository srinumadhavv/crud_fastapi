from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine) #-- without alembic 

app=FastAPI()

origins=["*"] #list of urls that can talk to our api if * every thing can talk to our domain
app.add_middleware(
    CORSMiddleware,
    allow_origina=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/") # path operation
async def root():
    return {"message":"Hello world !!"}





