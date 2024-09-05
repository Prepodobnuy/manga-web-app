from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    nickname = Column(String)
    hashed_password = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    pfp_path = Column(String)

    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    role = relationship('Role', back_populates='user')
    title_subscribed_user = relationship('TitleSubscribedUser', back_populates='user')
    rate = relationship('Rate', back_populates='user')
    notification = relationship('Notification', back_populates='user')
    chapter = relationship('Chapter', back_populates='user')
    comment = relationship('Comment', back_populates='user')
    carma = relationship('Carma', back_populates='user')
    customlist = relationship('CustomList', back_populates='user')
    listlink = relationship('ListLink', back_populates='user')

    def __init__(self, id: int, username: str, email: str, hashed_password: str) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.privilege_level = "default"
        self.nickname = username

    def __repr__(self) -> str:
        return f"[{self.id}] {self.username}\nemail:{self.email}\nhashed_password:{self.hashed_password}\nlevel:{self.privilege_level}\nnickname:{self.nickname}"

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    ru_name = Column(String)
    en_name = Column(String)
    ru_desc = Column(String)
    en_desc = Column(String)

    user = relationship('User', back_populates='role')
    roleprivilege = relationship('RolePrivilege', back_populates='role')

    def __init__(self, id: int, ru_name: str, en_name: str, ru_desc: str, en_desc: str):
        self.id = id
        self.ru_name = ru_name
        self.en_name = en_name
        self.ru_desc = ru_desc
        self.en_desc = en_desc

class Privilege(Base):
    __tablename__ = 'privilege'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    roleprivilege = relationship('RolePrivilege', back_populates='privilege')

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class RolePrivilege(Base):
    __tablename__ = 'roleprivilege'
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    privillage_id = Column(Integer, ForeignKey('privilege.id'))

    role = relationship('Role', back_populates='roleprivilege')
    privilege = relationship('Privilege', back_populates='roleprivilege')

    def __init__(self, id: int, role_id: int, privillage_id: int):
        self.id = id
        self.role_id = role_id
        self.privillage_id = privillage_id


class Title(Base):
    __tablename__ = 'title'

    id = Column(Integer, primary_key=True)

    # names
    original_name = Column(String)
    ru_name = Column(String)
    en_name = Column(String)
    alternative_names = Column(String)
    # info
    age_rating = Column(String)
    release_year = Column(String)
    description = Column(String)
    status = Column(String)
    translate_status = Column(String)
    franchise = Column(String)

    author = Column(String)
    artist = Column(String)
    publisher = Column(String)
    
    preview_picture_path = Column(String)
    # meta
    readers = Column(Integer)
    approved = Column(Boolean) # 0 - pending 1 - released

    title_subscribed_user = relationship('TitleSubscribedUser', back_populates='title')
    title_tag = relationship('TitleTag', back_populates='title')
    title_jenre = relationship('TitleJenre', back_populates='title')
    rate = relationship('Rate', back_populates='title')
    chapter = relationship('Chapter', back_populates='title')
    comment = relationship('Comment', back_populates='title')
    listlink = relationship('ListLink', back_populates='title')

class Rate(Base):
    """
    title rating sqlalchemy table
    id Integer Primary
    rate Integer possible values 1-10
    user_id Integer
    title_id Integer
    """
    __tablename__ = 'rate'
    id = Column(Integer, primary_key=True)
    rate = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    title_id = Column(Integer, ForeignKey('title.id', ondelete='CASCADE'))

    user = relationship('User', back_populates='rate')
    title = relationship('Title', back_populates='rate')

    def __init__(self, id: int, rate: int, user_id: int, title_id: int):
        self.id = id
        self.rate = rate
        self.user_id = user_id
        self.title_id = title_id

class TitleSubscribedUser(Base):
    """
    sqlalchemy table of users subscribed to title updates
    id Integer Primary
    title_id Integer
    user_id Integer
    """
    __tablename__ = 'title_subscribed_user'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    title = relationship('Title', back_populates='title_subscribed_user')
    user = relationship('User', back_populates='title_subscribed_user')

    def __init__(self, id: int, title_id: int, user_id: int) -> None:
        self.id = id
        self.title_id = title_id
        self.user_id = user_id

    def __repr__(self) -> str:
        return f'TitleSubscribedUser\nid:{self.id}\ntitle_id:{self.title_id}\nuser_id:{self.user_id}'

class TitleTag(Base):
    """
    sqlalchemy table of tags linked to title
    id Integer Primary
    title_id Integer
    tag_id Integer
    """
    __tablename__ = 'title_tag'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))

    title = relationship('Title', back_populates='title_tag')
    tag = relationship('Tag', back_populates='title_tag')

    def __init__(self, id: int, title_id: int, tag_id: int) -> None:
        self.id = id
        self.title_id = title_id
        self.tag_id = tag_id

    def __repr__(self) -> str:
        return f"TitleTag:\nid:{self.id}\ntitle_id:{self.title_id}\ntag_id:{self.tag_id}"

class TitleJenre(Base):
    """
    sqlalchemy table of jenres linked to title
    id Integer Primary
    title_id Integer
    jenre_id Integer
    """
    __tablename__ = 'title_jenre'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    jenre_id = Column(Integer, ForeignKey('jenre.id'))

    title = relationship('Title', back_populates='title_jenre')
    jenre = relationship('Jenre', back_populates='title_jenre')

    def __init__(self, id: int, title_id: int, jenre_id: int) -> None:
        self.id = id
        self.title_id = title_id
        self.jenre_id = jenre_id

    def __repr__(self) -> str:
        return f"TitleJenre:\nid:{self.id}\ntitle_id:{self.title_id}\njenre_id:{self.jenre_id}"

class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True)
    publisher_id = Column(Integer, ForeignKey('user.id'))
    publish_date = Column(String)
    volume = Column(String)
    pages_dir = Column(String)
    title_id = Column(Integer, ForeignKey('title.id'))

    user = relationship('User', back_populates='chapter')
    title = relationship('Title', back_populates='chapter')

    def __init__(self, id: int, publisher_id: int, publish_date: str, volume: str, pages_dir: str, title_id: int) -> None:
        self.id = id
        self.publisher_id = publisher_id
        self.publish_date = publish_date
        self.volume = volume
        self.pages_dir = pages_dir
        self.title_id = title_id

    def __repr__(self) -> str:
        return f"Chapter\nid:{self.id}\npublisher_id:{self.publisher_id}\npublish_date{self.publish_date}\nvolume:{self.volume}\npages_dir:{self.pages_dir}"


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    
    publish_date = Column(String)
    caption = Column(String)
    publisher_id = Column(Integer, ForeignKey('user.id'))
    parent_comment_id = Column(Integer, ForeignKey('comment.id', ondelete='CASCADE'))
    title_id = Column(Integer, ForeignKey('title.id', ondelete='CASCADE'))
    page = Column(String)

    title = relationship('Title', back_populates='comment')
    user = relationship('User', back_populates='comment')
    carma = relationship('Carma', back_populates='comment')

    def __init__(self, id: int, publish_date: str, caption: str, rating:int = 0, publisher_id: int|None = None, parent_comment_id: int|None = None, title_id: int|None = None, page: str|None = None):
        self.id = id
        self.caption = caption
        self.rating = rating
        self.publish_date = publish_date
        self.publisher_id = publisher_id
        self.parent_comment_id = parent_comment_id
        self.title_id = title_id
        self.page = page

class Carma(Base):
    """
    comment rating sqlalchemy table
    id Integer Primary
    rate Integer possible values -1|1
    user_id Integer
    comment_id Integer
    """
    __tablename__ = 'carma'
    id = Column(Integer, primary_key=True)
    rate = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    comment_id = Column(Integer, ForeignKey('comment.id', ondelete='CASCADE'))
    
    user = relationship('User', back_populates='carma')
    comment = relationship('Comment', back_populates='carma')

    def __init__(self, id: int, rate: int, user_id: int, comment_id: int):
        self.id = id
        self.rate = rate
        self.user_id = user_id
        self.comment_id = comment_id


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    ru_name = Column(String)
    en_name = Column(String)

    title_tag = relationship('TitleTag', back_populates='tag')

    def __init__(self, id: int, ru_name: str, en_name: str) -> None:
        self.id = id
        self.ru_name = ru_name
        self.en_name = en_name

    def __repr__(self) -> str:
        return f"Tag \nid:{self.id}\nru_name:{self.ru_name}\nen_name:{self.en_name}"

class Jenre(Base):
    __tablename__ = 'jenre'
    id = Column(Integer, primary_key=True)
    ru_name = Column(String)
    en_name = Column(String)

    title_jenre = relationship('TitleJenre', back_populates='jenre')

    def __init__(self, id: int, ru_name: str, en_name: str) -> None:
        self.id = id
        self.ru_name = ru_name
        self.en_name = en_name

    def __repr__(self) -> str:
        return f"Jenre \nid:{self.id}\nru_name:{self.ru_name}\nen_name:{self.en_name}"

class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    unix_time_stamp = Column(Integer)
    title = Column(String)
    type = Column(String)  # title|comment|application|message|another 
    caption = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='notification')

    def __init__(self, id: int, unix_time_stamp: int, title: str, type: str, caption: str, user_id: int) -> None:
        self.id = id
        self.unix_time_stamp = unix_time_stamp
        self.title = title
        self.type = type
        self.caption = caption
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"Notification\nid:{self.id}\ntime_stamp:{self.unix_time_stamp}\ntitle:{self.title}\ntype:{self.type}\ncaption:{self.caption}"

class DefaultList(Base):
    __tablename__ = 'defaultlist'
    id = Column(Integer, primary_key=True)
    ru_name = Column(String)
    en_name = Column(String)

    listlink = relationship('ListLink', back_populates='defaultlist')

    def __init__(self, id: int, ru_name: str, en_name: str):
        self.id = id
        self.ru_name = ru_name
        self.en_name = en_name

class CustomList(Base):
    __tablename__ = 'customlist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='customlist')
    listlink = relationship('ListLink', back_populates='customlist')

    def __init__(self, id: int, name: str, user_id: int):
        self.id = id
        self.name = name
        self.user_id = user_id

class ListLink(Base):
    __tablename__ = 'listlink'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id')) 
    user_id = Column(Integer, ForeignKey('user.id'))
    default_list_id = Column(Integer, ForeignKey('defaultlist.id'))
    custom_list_id = Column(Integer, ForeignKey('customlist.id'))

    title = relationship('Title', back_populates='listlink')
    user = relationship('User', back_populates='listlink')
    defaultlist = relationship('DefaultList', back_populates='listlink')
    customlist = relationship('CustomList', back_populates='listlink')

    def __init__(self, id: int, title_id: int, user_id: int, default_list_id: int|None, custom_list_id: int|None):
        self.id = id
        self.title_id = title_id
        self.user_id = user_id
        self.default_list_id = default_list_id
        self.custom_list_id = custom_list_id