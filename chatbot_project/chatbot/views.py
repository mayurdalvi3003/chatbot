from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import load_json_data
from django.shortcuts import render

DATA = load_json_data()

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        try:
            input_data = json.loads(request.body)
            query = input_data.get('query', '').lower()
            response = {}

            # Check if the query matches any of the categories
            for category, records in DATA.items():
                matched_records = [record for record in records if query in json.dumps(record).lower()]
                if matched_records:
                    response[category] = matched_records

            if response:
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'response': 'No match found. Please try again with different keywords.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

    # This view will render the chatbot interface
def chatbot_page(request):
    return render(request, 'chatbot/chatbot.html')
