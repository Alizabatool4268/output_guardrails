from pydantic import BaseModel

class Mydataclass(BaseModel):
    is_querry_related_to_politics_or_political_figures:bool
    reason:str
    is_querry_related_to_math:bool
    reason:str