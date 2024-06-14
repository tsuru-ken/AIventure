from django.db import models

class Partners(models.Model):
    """
    パートナーの情報を保持するモデル。
    """
    name = models.CharField(max_length=255)  # パートナーの名前
    logo = models.ImageField(upload_to='logos/')  # ロゴ画像のファイルパス
    address = models.CharField(max_length=255)  # パートナーの住所
    url = models.URLField()  # パートナーのウェブサイトURL
    established = models.DateField()  # 設立日
    service = models.TextField()  # 提供するサービスの概要
    engineer = models.IntegerField()  # エンジニアの人数
    provision = models.TextField()  # その他の提供情報
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    service_content = models.ManyToManyField('ServiceContent', blank=True)  # 多対多のサービスコンテンツ
    ai_category = models.ManyToManyField('AiCategory', blank=True)  # 多対多のAIカテゴリ
    cost = models.ManyToManyField('Cost', blank=True)  # 多対多のコスト情報
    product_info = models.ManyToManyField('ProductInfo', blank=True)  # 多対多のプロダクト情報
    case_study = models.ManyToManyField('CaseStudy', blank=True)  # 多対多のケーススタディ

    def __str__(self):
        return self.name  # パートナーの名前を文字列として返す

class ServiceContent(models.Model):
    """
    サービスコンテンツの情報を保持するモデル。
    """
    division = models.CharField(max_length=255)  # サービスの部門名
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return self.division  # サービスの部門名を文字列として返す

class AiCategory(models.Model):
    """
    AIカテゴリの情報を保持するモデル。
    """
    genre = models.CharField(max_length=255)  # AIカテゴリのジャンル
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return self.genre  # AIカテゴリのジャンルを文字列として返す

class Cost(models.Model):
    """
    コスト情報を保持するモデル。
    """
    breakdown = models.TextField()  # コストの詳細
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return self.breakdown  # コストの詳細を文字列として返す

class PartnerServiceContentLabel(models.Model):
    """
    パートナーとサービスコンテンツの関係を示すモデル。
    """
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)  # 関連するパートナー
    service_content = models.ForeignKey(ServiceContent, on_delete=models.CASCADE)  # 関連するサービスコンテンツ
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return f'{self.partner.name} - {self.service_content.division}'  # パートナー名とサービスコンテンツの部門名を文字列として返す

class PartnerAicategoryLabel(models.Model):
    """
    パートナーとAIカテゴリの関係を示すモデル。
    """
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)  # 関連するパートナー
    ai_category = models.ForeignKey(AiCategory, on_delete=models.CASCADE)  # 関連するAIカテゴリ
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return f'{self.partner.name} - {self.ai_category.genre}'  # パートナー名とAIカテゴリのジャンルを文字列として返す

class PartnerCostLabel(models.Model):
    """
    パートナーとコスト情報の関係を示すモデル。
    """
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)  # 関連するパートナー
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)  # 関連するコスト情報
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return f'{self.partner.name} - {self.cost.breakdown}'  # パートナー名とコストの詳細を文字列として返す

class CaseStudy(models.Model):
    """
    ケーススタディの情報を保持するモデル。
    """
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)  # 関連するパートナー
    name = models.CharField(max_length=255)  # ケーススタディの名前
    content = models.TextField()  # ケーススタディの内容
    image = models.ImageField(upload_to='case_studies/')  # ケーススタディの画像のファイルパス
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return self.name  # ケーススタディの名前を文字列として返す

class ProductInfo(models.Model):
    """
    プロダクト情報を保持するモデル。
    """
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)  # 関連するパートナー
    name = models.CharField(max_length=255)  # プロダクトの名前
    content = models.TextField()  # プロダクトの内容
    image = models.ImageField(upload_to='products/')  # プロダクトの画像のファイルパス
    created_at = models.DateTimeField(auto_now_add=True)  # レコード作成日時
    updated_at = models.DateTimeField(auto_now=True)  # レコード更新日時

    def __str__(self):
        return self.name  # プロダクトの名前を文字列として返す


# # ManyToManyFieldの定義をPartnersモデルに追加
# Partners.add_to_class('service_content', models.ManyToManyField(ServiceContent, blank=True))
# Partners.add_to_class('ai_category', models.ManyToManyField(AiCategory, blank=True))
# Partners.add_to_class('cost', models.ManyToManyField(Cost, blank=True))
# Partners.add_to_class('product_info', models.ManyToManyField(ProductInfo, blank=True))
# Partners.add_to_class('case_study', models.ManyToManyField(CaseStudy, blank=True))




