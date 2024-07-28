from fastapi import APIRouter
from Configs.ControllersContainer import Controllers

router = APIRouter()
router.include_router(Controllers.statusController().router, tags=["status"], prefix="/status")
router.include_router(Controllers.modelController().router, tags=["sentiments"], prefix="/sentiment")
print("--- Routers Initialized ---")
