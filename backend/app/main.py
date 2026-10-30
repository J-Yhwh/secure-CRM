# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

import uvicorn
import os
from fastapi import FastAPI
from fastapi middleware.cors import CORSMiddleware 

app = FastAPI()

# Connect the Routers
app.include_router(auth.router, prefix="/auth", tags=["Authenticattion"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

@app.get("/")
async def root():
  return{"message": "Welcome to Secure Customer API"}


