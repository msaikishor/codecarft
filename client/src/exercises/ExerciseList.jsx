import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export default function ExerciseList() {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/exercises/")
      .then(res => setExercises(res.data))
      .catch(err => console.error("Failed to load exercises:", err));
  }, []);

  return (
    <div>
      <h2>Exercise List</h2>
      {exercises.length === 0 ? (
        <p>No exercises found.</p>
      ) : (
        <ul>
          {exercises.map((q) => (
            <li key={q.id}>
              <Link to={`/exercise/${q.id}`}>{q.title}</Link>
              {" "}({q.predicted_difficulty})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
