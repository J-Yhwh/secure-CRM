# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

from fastapi import APIRouter, Depends, HTTPException
from ..core.security import role_required, get_current_user
from ..db import models, session  

# Rout to amalgamate customer UI to backend / server logic
router = APIRouter()

# ---- MAKER ACTIONS (Create/Modify) ----

@router.post("/requests", dependencies=[Depends(role_required(["Maker", "Admin"]))])
async def submit_customer_request, payload: Customer_schema, user=Depends(get_current_user):
  return {"message": "Request submitted for approval"}

# ---- CHECKER ACTIONS : APPROVING/REJECTING ----
@router.post("/requests/{request_id}/approve", dependencies=[Depends(role_required(["Checker", "Admin"]))])
async def approve_customer_request(request_id: int, user=Depends(get_current_user)):
    # TODO: look up the request, check it exists and is pending, then mark it approved
    return {"message": "Request approved", "request_id": request_id}

@router.post("/requests/{request_id}/reject", dependencies=[Depends(role_required(["Checker", "Admin"]))])
async def reject_customer_request(request_id: int, user=Depends(get_current_user)):
    # TODO: look up the request, check it exists and is pending, then mark it rejected
    return {"message": "Request rejected", "request_id": request_id}


 
