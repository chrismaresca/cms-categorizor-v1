# Pydantic Imports
from pydantic import BaseModel, Field

# Constants
from modules.constants import CATEGORY_TYPE


# Define the request body
class ContentRequestBody(BaseModel):
    content: str = Field(description="The content of the article to categorize.")

class ContentResponseBody(BaseModel):
    category: CATEGORY_TYPE = Field(description="The category of the article.")
    code_present: bool = Field(description="Whether the article contains code.")

