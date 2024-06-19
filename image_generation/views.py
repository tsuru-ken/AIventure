from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import ImageGeneration
from django.http import JsonResponse
import requests
import json
import os
from django.conf import settings
from uuid import uuid4
from datetime import datetime

class IndexView(ListView):
    template_name = 'index.html'

class ImageGenerationView(TemplateView):
    model = ImageGeneration
    template_name = 'image_generation.html'
    context_object_name = 'image_generation'

class ImageGenerationDetailView(TemplateView):
    model = ImageGeneration
    template_name = 'image_generation.html'
    context_object_name = 'image_generation'

def index(request):
    return render(request, 'index.html')

def generate_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_text = data.get('input_text')

        api_url = "https://vk4vi5cnij.execute-api.us-east-1.amazonaws.com/dev"
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({'input_text': input_text})

        response = requests.post(api_url, headers=headers, data=payload)
        response_data = response.json()

        print('API Request:', payload)
        print('Response:', response_data)

        # 画像のURLを取得
        image_url = response_data.get('body').get('presigned_url')

        # 画像を保存するディレクトリ
        save_dir = os.path.join(settings.MEDIA_ROOT, 'generated_images')
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # ユニークなファイル名の生成
        unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid4().hex}.png"
        image_path = os.path.join(save_dir, unique_filename)

        # 画像をダウンロードして保存
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(image_response.content)
            print("Image saved successfully.")
        else:
            print("Failed to retrieve the image.")

        return JsonResponse({'image_path': f'/media/generated_images/{unique_filename}'})
    else:
        model_id = request.GET.get('model_id')
        context = {'model_id': model_id}
        return render(request, 'index/index.html', context)

