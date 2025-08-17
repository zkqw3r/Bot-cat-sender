__all__ = ('routers', )

from aiogram import Router
from base_commands import router as base_cmd_router
from other_handlers import router as other_handlers_router
from main_handlers import router as main_handlers_router

router = Router(name=__name__)

router.include_routers(base_cmd_router,
                       other_handlers_router,
                       main_handlers_router)