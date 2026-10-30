# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

import uvicorn
import os
from fastapi import FastAPI
from fastapi middleware.cors import CORSMiddleware 

app = FastAPI()

# CORS SETUP (for the React Frontend to comunicate to and from backend)
app.add_middleware(
  CORSMiddleware,
  allow_origins= ["http://localhost:3000"],    #the localhost port fr React.js
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
  

# Connect the Routers
app.include_router(auth.router, prefix="/auth", tags=["Authenticattion"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

@app.get("/")
async def root():
  return{"message": "Welcome to Secure Customer API"}


if __name__ = "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True )


