import React from "react";
import ExerciseList from "./exercises/ExerciseList";
import ExerciseDetail from "./exercises/ExerciseDetail";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ExerciseList />} />
        <Route path="/exercise/:id" element={<ExerciseDetail />} />
      </Routes>
    </Router>
  );
}
