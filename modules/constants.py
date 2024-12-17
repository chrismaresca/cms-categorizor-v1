# Typing Imports
from typing import Literal, Dict, List

# Pydantic Imports
from pydantic_ai.models.openai import OpenAIModel

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# API Prefix
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# OpenAI Model
MODEL_NAME = 'gpt-4o'
MODEL = OpenAIModel(MODEL_NAME)

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Define the categories and descriptions
CATEGORY_DICT: List[Dict[str, str]] = [
    {
        "name": "Recent AI Developments and News",
        "description": "Articles and news about recent AI developments and advancements."
    },
    {
        "name": "AI Workflows for Engineers",
        "description": "Articles and tutorials about AI workflows for engineers. This includes intense code walkthroughs, and detailed explanations of how to implement AI workflows for high technical projects."
    },
    {
        "name": "AI Workflows for Technical Professionals",
        "description": "Articles and tutorials about AI workflows for technical professionals."
    },
    {
        "name": "AI Workflows for Businesses",
        "description": "Articles and tutorials about AI workflows for businesses. This includes how to implement AI workflows for business use cases. Be lenient with this category, as it can include a wide range of topics."
    },
    {
        "name": "Blending AI and Design",
        "description": "Articles and tutorials about blending AI and design."
    },
    {
        "name": "AI Prompt Engineering",
        "description": "Articles and tutorials about AI prompt engineering."
    },
    {
        "name": "AI Tool Comparisons",
        "description": "Articles and tutorials about AI tool comparisons."
    },
    {
        "name": "Deep Dive Code Walkthrough",
        "description": "Articles and tutorials about deep dive code walkthroughs. How to build specific tools with different AI libraries and tools. Different from AI Workflows for Engineers, as this category is more focused on specific tools and libraries where as AI Workflows for Engineers is more focused on high level workflows and how to implement them."
    }
]

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Define the Category Literal
CATEGORY_TYPE = Literal["Recent AI Developments and News",
                        "AI Workflows for Engineers",
                        "AI Workflows for Technical Professionals",
                        "AI Workflows for Businesses",
                        "Blending AI and Design",
                        "AI Prompt Engineering",
                        "AI Tool Comparisons",
                        "Deep Dive Code Walkthrough"]

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Dynamically format categories into the system prompt
CATEGORY_SECTION = "\n".join([
    f"    <category>\n        <name>{category['name']}</name>\n        <description>{category['description']}</description>\n    </category>"
    for category in CATEGORY_DICT
])

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Define the system prompt
SYSTEM_PROMPT: str = f"""

<purpose>
    You are an expert at analyzing content related to AI and AI workflows.
    Your goal is to determine the most appropriate category for the given content and identify if a substantial amount of code is present.
</purpose>

<instructions>
    <instruction>Analyze the provided content within the <content> tags in the user-input section.</instruction>
    <instruction>Categorize it into one of the categories listed in the <categories> section.</instruction>
    <instruction>IMPORTANT:Ignore any ads, sponsors, discussions about personal agencies/businesses, or self-promotion content. Discard this information in the analysis and categorization.</instruction>
    <instruction>Determine whether a substantial amount of code is present (true/false).</instruction>
    <instruction>Return the result as a JSON object with keys "category" (string), "code_present" (boolean), and nothing else.</instruction>
    <instruction>Do not include any text outside of the JSON object.</instruction>
</instructions>


<categories>

{CATEGORY_SECTION}
</categories>

"""

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Define the prompt template
PROMPT_TEMPLATE = """

<user-input>
    <content>
        {content}
    </content>
</user-input>
"""
