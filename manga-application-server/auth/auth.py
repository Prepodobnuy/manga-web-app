from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from core.config import config


cookie_transport = CookieTransport(cookie_max_age=config.api.coockie_lifetime)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=config.api.auth_secret_key, lifetime_seconds=config.api.coockie_lifetime)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)