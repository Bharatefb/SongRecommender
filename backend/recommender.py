SONG_CATALOG = [
    {
        "title": "Ilahi",
        "artist": "Arijit Singh",
        "moods": ["happy", "energetic", "motivational"],
        "energy": "high",
        "styles": ["bollywood"]
    },
    {
        "title": "Love You Zindagi",
        "artist": "Amit Trivedi",
        "moods": ["happy", "relaxed", "motivational"],
        "energy": "medium",
        "styles": ["bollywood"]
    },
    {
        "title": "Kasoor",
        "artist": "Prateek Kuhad",
        "moods": ["sad", "relaxed", "calm", "romantic"],
        "energy": "low",
        "styles": ["acoustic", "indie"]
    },
    {
        "title": "Kho Gaye Hum Kahan",
        "artist": "Jasleen Royal",
        "moods": ["sad", "nostalgic", "calm"],
        "energy": "low",
        "styles": ["indie", "acoustic"]
    },
    {
        "title": "Iktara",
        "artist": "Kavita Seth",
        "moods": ["romantic", "calm", "nostalgic"],
        "energy": "low",
        "styles": ["bollywood", "acoustic"]
    },
    {
        "title": "Agar Tum Saath Ho",
        "artist": "Alka Yagnik & Arijit Singh",
        "moods": ["sad", "romantic", "nostalgic"],
        "energy": "low",
        "styles": ["bollywood"]
    },
    {
        "title": "Believer",
        "artist": "Imagine Dragons",
        "moods": ["energetic", "angry", "motivational"],
        "energy": "high",
        "styles": ["rock"]
    },
    {
        "title": "On Top of the World",
        "artist": "Imagine Dragons",
        "moods": ["happy", "energetic", "motivational"],
        "energy": "high",
        "styles": ["rock", "pop"]
    },
    {
        "title": "Perfect",
        "artist": "Ed Sheeran",
        "moods": ["romantic", "calm"],
        "energy": "low",
        "styles": ["pop", "acoustic"]
    },
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "moods": ["energetic", "happy"],
        "energy": "high",
        "styles": ["pop", "rnb"]
    },
    {
        "title": "Until I Found You",
        "artist": "Stephen Sanchez",
        "moods": ["romantic", "nostalgic", "calm"],
        "energy": "low",
        "styles": ["pop", "acoustic"]
    },
    {
        "title": "The Night We Met",
        "artist": "Lord Huron",
        "moods": ["sad", "nostalgic"],
        "energy": "low",
        "styles": ["indie"]
    }
]


def recommend_songs(mood_data):

    mood = mood_data["mood"].lower()
    energy = mood_data["energy"].lower()
    style = mood_data["music_style"].lower()

    scored_songs = []

    for song in SONG_CATALOG:

        score = 0

        if mood in song["moods"]:
            score += 5

        if energy == song["energy"]:
            score += 3

        if style in song["styles"]:
            score += 2

        if score > 0:
            scored_songs.append({
                **song,
                "score": score
            })

    scored_songs.sort(
        key=lambda song: song["score"],
        reverse=True
    )

    recommendations = []

    for song in scored_songs[:5]:

        recommendations.append({
            "title": song["title"],
            "artist": song["artist"],
            "reason": (
                f"This song matches your {mood} mood "
                f"and has a {song['energy']} energy level."
            )
        })

    return recommendations
