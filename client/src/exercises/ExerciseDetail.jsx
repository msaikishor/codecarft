import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function ExerciseDetail() {
  const { id } = useParams();
  const [exercise, setExercise] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/exercise/${id}/`)
      .then(res => setExercise(res.data))
      .catch(err => console.error("Failed to fetch exercise:", err));
  }, [id]);

  if (!exercise) return <p>Loading...</p>;

  return (
    <div>
      <h2>{exercise.title}</h2>
      <p>{exercise.description}</p>
      <p><strong>Predicted Difficulty:</strong> {exercise.predicted_difficulty}</p>
      <pre>{exercise.starter_code}</pre>
    </div>
  );
}
