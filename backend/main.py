from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import (
    RecommendationRequest,
    RecommendationResponse
)

from ai import analyze_mood
from recommender import recommend_songs


app = FastAPI(
    title="AI Song Recommender",
    description="Mood-based AI song recommendation API",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "AI Song Recommender API is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(request: RecommendationRequest):

    try:

        # Step 1: Analyze mood using Qwen
        mood_data = analyze_mood(
            request.name,
            request.mood
        )

        # Step 2: Find matching songs
        songs = recommend_songs(
            mood_data
        )

        return {
            "name": request.name,
            "mood": request.mood,
            "analyzed_mood": mood_data["mood"],
            "energy": mood_data["energy"],
            "music_style": mood_data["music_style"],
            "songs": songs
        }

    except Exception as e:

        print("ERROR:", str(e))

        raise HTTPException(
            status_code=500,
            detail="Unable to generate recommendations."
        )
