from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .auth import get_current_user
from .models import User

router = APIRouter(prefix="/security", tags=["security"])

# Global Kill Switch State (In-Memory for now, should be DB/Redis)
kill_switch_active = False

@router.post("/verify-action")
async def verify_action(action_data: dict, current_user: User = Depends(get_current_user)):
    """
    Assess the risk of an action and determine if 'Modo Paranoico' is required.
    """
    risk_level = assess_risk(action_data.get("command", ""))
    
    if risk_level == "critical":
        return {
            "status": "requires_confirmation",
            "message": "This action is critical. Please confirm with the explicit phrase.",
            "required_phrase": "Confirmo la eliminación permanente"
        }
    
    return {"status": "safe", "message": "Action approved"}

def assess_risk(command: str) -> str:
    critical_keywords = ["rm ", "format", "del /s", "drop table", "registry delete"]
    if any(kw in command.lower() for kw in critical_keywords):
        return "critical"
    return "low"
