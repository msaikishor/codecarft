from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json
from pathlib import Path
from ai_model.predict import predict_difficulty

BASE_DIR = Path(__file__).resolve().parent.parent

def load_questions():
    with open(BASE_DIR / 'data' / 'questions.json') as f:
        return json.load(f)

def exercise_list(request):
    questions = load_questions()
    for q in questions:
        q['predicted_difficulty'] = predict_difficulty(q['description'])
    return JsonResponse(questions, safe=False)

def exercise_detail(request, id):
    questions = load_questions()
    q = next((item for item in questions if item['id'] == id), None)
    if q:
        q['predicted_difficulty'] = predict_difficulty(q['description'])
        return JsonResponse(q)
    return JsonResponse({'error': 'Exercise not found'}, status=404)
