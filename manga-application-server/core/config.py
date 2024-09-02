from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080

class Prefix(BaseModel):
    default: str = ''
    user: str = '/user'
    title: str = '/title'
    auth: str = '/auth/jwt'
    register: str = '/auth'
    tags: str = '/tag'
    jenres: str = '/jenre'
    comment: str = '/comment'

class Api(BaseModel):
    prefix: Prefix = Prefix()
    auth_secret_key: str = 'YASOSUfgoiuewggfget97832ygudsgdsghfliwugt297gwekjhfg'
    reset_password_token_secret: str = 'TISOSIsdiojvh23p98gykjwhfa8oy08yg34iu4vhgo34itqw9838'
    verification_token_secret: str = 'MYSOSEmdviuyg9348gtaiofyg3487fg2q837gf8e7ragf0834gow'
    coockie_lifetime: int = 1900800

class App(BaseModel):
    title: str = 'Manga web-app'
    version: str = '0.0.1'

class Config(BaseSettings):
    run: RunConfig = RunConfig()
    api: Api = Api()
    app: App = App()

config = Config()