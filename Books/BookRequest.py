from typing import Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description = 'Id is not required on create', default = None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt = 0, lt = 6)
    published_date: int = Field(gt=1999, lt =2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book Title",
                "author": "Author Name",
                "description": "Description of the book",
                "rating": 5,
                "published_date": 2023
            }
        }
    }
