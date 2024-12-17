# Pydantic Imports
from pydantic_ai import Agent

# Dotenv Imports
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Constants
from modules.constants import SYSTEM_PROMPT, MODEL, PROMPT_TEMPLATE
from modules.api_types import ContentRequestBody, ContentResponseBody


# Define the agent
agent = Agent(
    model=MODEL,
    result_type=ContentResponseBody,
    system_prompt=SYSTEM_PROMPT,
)


# Define the function to categorize the content
async def categorize_content(content: ContentRequestBody) -> ContentResponseBody:
    """
    Categorize the content of an article.

    Args:
        content (ContentRequestBody): The content of the article to categorize.

    Returns:
        ContentResponseBody: The categorization model.
    """
    raw_result = await agent.run(PROMPT_TEMPLATE.format(content=content))
    return raw_result.data
