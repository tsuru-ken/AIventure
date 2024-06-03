from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView


from .models import ImageGeneration

#JsonResponse:JSON形式のレスポンスを返す用
from django.http import JsonResponse

#request:HTTPリスクエストを送信するための標準ライブラリ
import requests

# json:JSONデータを操作するための標準ライブラリ
import json


class IndexView(ListView):

    template_name = 'index.html'

class ImageGenerationView(TemplateView):
    model = ImageGeneration
    template_name = 'image_generation.html'
    context_object_name = 'image_generation'

class ImageGenerationDetailVieView(TemplateView):
    model = ImageGeneration
    template_name = 'image_generation.html'
    context_object_name = 'image_generation'


# generate_image関数
def generate_image(request):
    # POSTリクエストの確認
    if request.method =='POST':
        # リクエストボディをJSONとして解析して、'input_text'を所得
        data = json.loads(request.body)
        input_text = data.get('input_text')

        # ここでAPI Gatewayにリクエストを送信
        # 画像生成APIのAPIのエンドポイントURL ,ヘッダー,ペイロードを準備
        api_url = "https://tmiskg4dm3.execute-api.us-east-1.amazonaws.com/dev"
        headers = {'Content-Type':'application/json'}
        payload = json.dumps({'input_text': input_text})

        # request.postを使用してAPIリクエストを送信し、レスポンスをJSONとして解析
        response = requests.post(api_url, headers=headers, data=payload)
        response_data = response.jason()
        
        # APIリクエsつろとレスポンスの内容をサーバーのコンソールに出力
        print('API Request:', payload)
        print('Response:', response_data)
        
        # 画像生成APIから受け取ったレスポンスデータをそのままJSON形式でクライアントに返す
        return JsonResponse(response_data)