from django.shortcuts import render
from django.http import JsonResponse
import ollama

def index(request):
    return render(request, "chat.html")  # Make sure this template exists

def chat_response(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        try:
            response = ollama.chat(model='mistral', messages=[
                {"role": "user", "content": prompt}
            ])
            # Extract the content from the message object
            if hasattr(response, 'message') and hasattr(response.message, 'content'):
                response_text = response.message.content
            else:
                response_text = f"Error: Unexpected response structure: {response}"
        except Exception as e:
            response_text = f"Error: {str(e)}"
        return render(request, "chat_response.html", {"response": response_text})
    return JsonResponse({"error": "Only POST method allowed"}, status=400)
