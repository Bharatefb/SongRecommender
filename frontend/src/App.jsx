import { useState } from "react";
import MoodForm from "./components/MoodForm";
import "./App.css";


function App() {

    const [recommendations, setRecommendations] = useState(null);
    const [loading, setLoading] = useState(false);


    return (

        <div className="app">

            <header>

                <h1>🎵 MoodTunes</h1>

                <p>
                    AI-powered music recommendations
                </p>

            </header>


            <main>

                <MoodForm
                    onRecommendations={setRecommendations}
                    loading={loading}
                    setLoading={setLoading}
                />


                {recommendations && (

                    <section className="results">

                        <h2>
                            Hey {recommendations.name}! 👋
                        </h2>

                        <p className="mood-description">

                            Based on your mood, we detected:

                        </p>


                        <div className="mood-tags">

                            <span>
                                Mood: {recommendations.analyzed_mood}
                            </span>

                            <span>
                                Energy: {recommendations.energy}
                            </span>

                            <span>
                                Style: {recommendations.music_style}
                            </span>

                        </div>


                        <h3>
                            🎧 Your Recommendations
                        </h3>


                        <div className="songs">

                            {recommendations.songs.map(
                                (song, index) => (

                                    <div
                                        className="song-card"
                                        key={index}
                                    >

                                        <div className="song-number">
                                            {index + 1}
                                        </div>

                                        <div>

                                            <h4>
                                                {song.title}
                                            </h4>

                                            <p>
                                                {song.artist}
                                            </p>

                                            <small>
                                                {song.reason}
                                            </small>

                                        </div>

                                    </div>

                                )
                            )}

                        </div>

                    </section>

                )}

            </main>

        </div>

    );
}

export default App;
