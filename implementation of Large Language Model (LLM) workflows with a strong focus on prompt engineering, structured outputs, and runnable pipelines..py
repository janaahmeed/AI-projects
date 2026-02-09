from typing import List
from collections import Counter

from pydantic import BaseModel, Field

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda

with open('data/emails.json', 'r') as f:
    emails = json.load(f)

    
class Email(BaseModel):
    email: str = Field(description="email content")
    customer_sentiment: str = Field(
        description="customer sentiment of email (positive or negative)"
    )
    product_category: str = Field(
        description="general product category (e.g. Furniture, Electronics)"
    )
    location: str = Field(
        description="store or customer location"
    )


class GroupResults(BaseModel):
    emails: List[Email]



template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an AI that generates JSON only, following the provided schema exactly."
    ),
    (
        "human",
        "Generate JSON from the input text.\n"
        "Input: {input}\n"
        "Format instructions: {format_instructions}"
    )
])


parser = JsonOutputParser(pydantic_object=GroupResults)

format_instructions = parser.get_format_instructions()

def complaints(parsed_output: dict):
    email_list = parsed_output.get("emails", [])

    negative_emails = [
        e for e in email_list
        if e.get("customer_sentiment", "").lower() == "negative"
    ]

    if not negative_emails:
        return "No negative sentiment detected."

    category_counts = Counter(
        e.get("product_category", "Unknown") for e in negative_emails
    )
    location_counts = Counter(
        e.get("location", "Unknown") for e in negative_emails
    )

    return {
        "product_with_most_negative_sentiment":
            category_counts.most_common(1)[0][1],
        "location_with_most_negative_sentiment":
            location_counts.most_common(1)[0][1],
    }

negative_email_tool = RunnableLambda(complaints)
mock_chain = (
    template
    .partial(format_instructions=format_instructions)
    | parser
    | negative_email_tool
)

mock_chain,invoke({"input": emails})




negative_email_tool = RunnableLambda(complaints)
