from django.db import models
from users.models import CustomUser
from image_generation.models import ImageGeneration

class AIModel(models.Model):
    # CustomUserモデルと１対多
    # on_delete=models.CASCADE,関連ユーザーが削除されるとモデルも削除
    # related_name='ai_modelsはユーザーからこのモデルを参照するための名前指定。
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ai_models')
    image_generation = models.ForeignKey(ImageGeneration, on_delete=models.CASCADE, related_name='ai_models')

    # レコード作成時に、自動的に現在の日時が設定される
    created_at = models.DateTimeField(auto_now_add=True)
    # レコード更新時に、自動的に現在の日時が設定される
    updated_at = models.DateTimeField(auto_now=True)

    '''Django管理サイトでデータを表示する識別名として、f""フォーマット文字列(f-string)で、文字列に変数の値を埋め込む
    ここでは、ユーザ名と画像生成データのタイトルを返す。'''
    def __str__(self):
        return f"{self.user.username} - {self.image_generation.title}"