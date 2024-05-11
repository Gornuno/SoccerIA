from django.shortcuts import render
from .src.iaconfig import generate_text_with_google_api

import markdown

def index(request):
    return render(request, 'index.html')

def get_news(request):
    result = None
    prompt = request.POST.get('prompt')
    error_message = None
    if request.method == 'POST' and prompt:
        prompt = request.POST.get('prompt')
        text_result = generate_text_with_google_api(prompt)
        result = markdown.markdown(text_result)
    return render(request, 'index.html', {'prompt': prompt,
                                          'result': result,
                                          'error_message': error_message})
    
