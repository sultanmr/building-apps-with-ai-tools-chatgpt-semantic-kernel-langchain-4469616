from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    PromptTemplate
)
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Furniture (BaseModel):
    type: str = Field(description="The type of furniture item")
    style: str = Field(description="The style of the furniture item")
    color: str = Field(description="The color of the furniture item")

furniture_request = "i would like a blue mid century modern chair"
parser = PydanticOutputParser(pydantic_object=Furniture)
# prompt = PromptTemplate(
#     input_variables=["furniture_request"],
#     template="Extract the type, style, and color of the furniture from the request: {furniture_request}"
# )

prompt = PromptTemplate(template="Answer the user query:\n{format_instructions}\n{query}\n",
                        input_variables=["query"],
                        partial_variables={"format_instructions": parser.get_format_instructions()})
_input = prompt.format(query=furniture_request)
print (_input)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
output = model.predict(_input)
parsed = parser.parse(output)
print(parsed)
print (parsed.color)
