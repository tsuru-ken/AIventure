from django.contrib import admin
from .models import AIModel

# デコレーターでAIModelをDjango管理サイトに登録
@admin.register(AIModel)
# AIModeladminクラスはadmin.ModelAdminクラスを継承
class AIModelAdmin(admin.ModelAdmin):
    # 管理サイトのリスト画面で表示されるフィールド
    list_display = ('user','image_generation','created_at','updated_at')
    # 管理サイトの検索ボックスで検索可能なフィールド　例　user__username:ユーザーのユーザー名で検索可能
    search_fields = ('user__username','image_generation__title')

