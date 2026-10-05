import { useState } from "react";

function MoodForm({ onRecommendations, loading, setLoading }) {

    const [name, setName] = useState("");
    const [mood, setMood] = useState("");

    const handleSubmit = async (event) => {

        event.preventDefault();

        if (!name.trim() || !mood.trim()) {
            alert("Please enter your name and mood.");
            return;
        }

        setLoading(true);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/recommend",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        name: name,
                        mood: mood
                    })
                }
            );

            if (!response.ok) {
                throw new Error("Failed to get recommendations");
            }

            const data = await response.json();

            onRecommendations(data);

        } catch (error) {

            console.error(error);

            alert(
                "Could not connect to the recommendation server."
            );

        } finally {

            setLoading(false);

        }
    };


    return (
        <form
            className="mood-form"
            onSubmit={handleSubmit}
        >

            <label>
                Your Name
            </label>

            <input
                type="text"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />


            <label>
                How are you feeling?
            </label>

            <textarea
                placeholder="Example: I had a stressful day and want to relax..."
                value={mood}
                onChange={(e) => setMood(e.target.value)}
                rows="5"
            />


            <button
                type="submit"
                disabled={loading}
            >

                {loading
                    ? "Finding Songs..."
                    : "🎵 Recommend Songs"
                }

            </button>

        </form>
    );
}

export default MoodForm;
