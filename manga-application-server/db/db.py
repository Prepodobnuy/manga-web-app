import os.path
import time
import datetime

from sqlalchemy import func

from db.session import get_session_engine
from db.entities import *
from db.logger import Logger


#logger = Logger(log_file_path='logs/test', log_to_term=False, log_to_file=False, displayed_log_level=999)
session, engine = get_session_engine()
Base.metadata.create_all(bind=engine)


def commit_after(func):
    def wrapper(*args, **kwargs):
        #func_name = f"{func.__qualname__}{args}"
        try:
            result = func(*args, **kwargs)
            session.commit()
            #logger.log(
            #    "Commited changes after executing",        
            #    os.path.relpath(func.__code__.co_filename),
            #    func_name,
            #    log_level=1
            #    )
            return result
        except Exception as e:
            print(e)
            session.rollback()
            #logger.log(
            #    "Failed to commit changes after executing",        
            #    os.path.relpath(func.__code__.co_filename),
            #    func_name,
            #    log_level=3
            #    )
    return wrapper

#region role CRED
@commit_after
def role_create(ru_name: str, en_name: str, ru_desc: str, en_desc: str):
    try:
        id = session.query(func.max(Role.id)).scalar() + 1
    except Exception:
        id = 0
    role = Role(id, ru_name, en_name, ru_desc, en_desc)
    session.add(role)
#endregion

#region privillage CRED
@commit_after
def privillage_create(name: str):
    try:
        id = session.query(func.max(Privilege.id)).scalar() + 1
    except Exception:
        id = 0
    privillage = Privilege(id, name)
    session.add(privillage)
#endregion

#region roleprivillage CRED
@commit_after
def roleprivillage_create(role_id: int, privillage_id: int):
    try:
        id = session.query(func.max(RolePrivilege.id)).scalar() + 1
    except Exception:
        id = 0
    roleprivillage = RolePrivilege(id, role_id, privillage_id)
    session.add(roleprivillage)
#endregion

#region user CRED
def user_read(id: int):
    user = session.query(User).filter_by(id=id).first()
    return user

def user_read_all():
    users = session.query(User).all()
    return users

@commit_after
def user_edit(id: int, data: dict):
    user = session.query(User).filter_by(id=id).first()
    for key, value in data.items():
        setattr(user, key, value)

@commit_after
def user_delete(id: int):
    user = session.query(User).filter_by(id=id).first()
    session.delete(user)

def user_email_taken(email: str) -> bool:
    user = session.query(User).filter_by(email=email).first()
    return user is not None

def user_username_taken(username: str) -> bool:
    user = session.query(User).filter_by(secure_name=username).first()
    return user is not None
#endregion

#region tag CRED
@commit_after
def tag_create(ru_name: str, en_name: str):
    try:
        id = session.query(func.max(Tag.id)).scalar() + 1
    except Exception:
        id = 0
    tag = Tag(id, ru_name, en_name)
    session.add(tag)

@commit_after
def tag_delete(id: int):
    tag = session.query(Tag).filter_by(id=id).first()
    session.delete(tag)

@commit_after
def tags_delete_ALL(): #please dont use this without a good reason
    tags = session.query(Tag).all()
    for tag in tags:
        session.delete(tag) 

def read_tag(id: int):
    tag = session.query(Tag).filter_by(id=id).first()
    return tag

def read_tags() -> list:
    tags = session.query(Tag).all()
    return tags
#endregion

#region jenre CRED
@commit_after
def jenre_create(ru_name: str, en_name: str):
    try:
        id = session.query(func.max(Jenre.id)).scalar() + 1
    except Exception:
        id = 0
    jenre = Jenre(id, ru_name, en_name)
    session.add(jenre)
@commit_after
def jenre_delete(id: int):
    jenre = session.query(Jenre).filter_by(id=id).first()
    session.delete(jenre)

@commit_after
def jenres_delete_ALL(): #please dont use this without a good reason
    jenres = session.query(Jenre).all()
    for jenre in jenres:
        session.delete(jenre) 

def read_jenre(id: int):
    jenre = session.query(Jenre).filter_by(id=id).first()
    return jenre

def read_jenres() -> list:
    jenres = session.query(Jenre).all()
    return jenres
#endregion

#region notification CRED
@commit_after
def notification_create(title: str, type: str, caption: str, user_id: int):
    try:
        id = session.query(func.max(Notification.id)).scalar() + 1
    except Exception:
        id = 0
    unix_time_stamp = int(time.time())
    notification = Notification(id, unix_time_stamp, title, type, caption, user_id)
    session.add(notification)

def notification_read_by_user_id(user_id: int):
    notifications = session.query(Notification).filter_by(user_id=user_id).all()
    return notifications

@commit_after
def notification_delete(id: int):
    notification = session.query(Notification).filter_by(id=id).first()
    session.delete(notification)

def notifications_check_time_stamp():
    unix_time_stamp = int(time.time())
    notifications = session.query(Notification).all()
    for notification in notifications:
        if unix_time_stamp - notification.unix_time_stamp >= 604800:
            notification_delete(notification.id)
#endregion

#region title CRED
@commit_after
def title_create(age_rating: str = "0+", ru_name: str = "String", en_name: str = "String", alternative_names: str = "String/String",
                 release_year: str = "2024", description: str = "String", status: str = "String", approve_status: int = 0, translate_status: str = "String",
                 franchise: str = "String", author: str = "String", artist: str = "String", publisher: str = "String", preview_picture_path: str|None = None):
    try:
        id = session.query(func.max(Title.id)).scalar() + 1
    except Exception:
        id = 0
    title = Title(
                id=id,
                age_rating=age_rating,
                ru_name=ru_name,
                en_name=en_name,
                alternative_names=alternative_names,
                release_year=release_year,
                description=description,
                status=status,
                approve_status=approve_status,
                translate_status=translate_status,
                franchise=franchise,
                author=author,    
                artist=artist,
                publisher=publisher,
                preview_picture_path=preview_picture_path
            )
        
    session.add(title)
    return id

def title_read(id: int):
    title = session.query(Title).filter_by(id=id).first()
    return title

#endregion

#region comment CRED
@commit_after
def comment_create(caption: str, publisher_id: int, parent_comment_id: int|None=None, title_id: int|None = None, page: int|None = None):
    try:
        id = session.query(func.max(User.id)).scalar() + 1
    except Exception:
        id = 0
    comment = Comment(
        id=id,
        caption=caption,
        publish_date=datetime.now().date(),
        rating=0,
        publisher_id=publisher_id,
        parent_comment_id=parent_comment_id,
        title_id=title_id,
        page=page
    )
    session.add(comment)

def comment_read(id: int):
    comment = session.query(Comment).filter_by(id=id).first()
    return comment

@commit_after
def comment_delete(id: int):
    comment = session.query(Comment).filter_by(id=id).first()
    session.delete(comment)

#endregion
