from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    mood: str = Field(..., min_length=1, max_length=500)


class Song(BaseModel):
    title: str
    artist: str
    reason: str


class RecommendationResponse(BaseModel):
    name: str
    mood: str
    analyzed_mood: str
    energy: str
    music_style: str
    songs: list[Song]
