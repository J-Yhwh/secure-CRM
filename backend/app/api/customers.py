

 

from FastAPI import APIRouter, Depends, HTTPExcrption
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
async def approve_custoemr_request(request_id: int, user=Depends(get_current_user): 
  return {"message": "Request rejected"}
 
