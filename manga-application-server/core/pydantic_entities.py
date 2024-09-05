from pydantic import BaseModel, Field

class Title(BaseModel):
    id: int = Field(example=0)

    original_name: str
    ru_name: str
    en_name: str
    alternative_names: str

    age_rating: str = Field(examples=['0+', '16+', '18+'])
    release_year: str
    description: str
    status: str
    translate_status: str
    franchise: str

    author: int
    artist: int
    publisher: int

    preview_picture_path: str

    readers: int
    approved: bool

class TitleTag(BaseModel):
    id: int = Field(example=0)
    title_id: int = Field(example=0)
    tag_id: int = Field(example=0)

class TitleJenre(BaseModel):
    id: int = Field(example=0)
    title_id: int = Field(example=0)
    jenre_id: int = Field(example=0)

class Rate(BaseModel):
    id: int = Field(example=0)
    rate: int = Field(examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    user_id: int = Field(example=0)
    title_id: int = Field(example=0)