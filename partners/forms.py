from django import forms
from .models import Partners, ServiceContent, AiCategory, Cost, ProductInfo, CaseStudy

class PartnerForm(forms.ModelForm):
    # 複数選択可能なサービスコンテンツフィールド
    service_content = forms.ModelMultipleChoiceField(
        queryset=ServiceContent.objects.all(), 
        widget=forms.CheckboxSelectMultiple, required=False)
    
    # 複数選択可能なAIカテゴリフィールド
    ai_category = forms.ModelMultipleChoiceField(
        queryset=AiCategory.objects.all(), 
        widget=forms.CheckboxSelectMultiple, required=False)
    
    # 複数選択可能なコストフィールド
    cost = forms.ModelMultipleChoiceField(
        queryset=Cost.objects.all(), 
        widget=forms.CheckboxSelectMultiple, required=False)
    
    # 複数選択可能なプロダクト情報フィールド
    product_info = forms.ModelMultipleChoiceField(
        queryset=ProductInfo.objects.all(), 
        widget=forms.CheckboxSelectMultiple, required=False)
    
    # 複数選択可能なケーススタディフィールド
    case_study = forms.ModelMultipleChoiceField(
        queryset=CaseStudy.objects.all(), 
        widget=forms.CheckboxSelectMultiple, required=False)
    
    # プロダクト情報の名前フィールド
    product_info_name = forms.CharField(required=False)
    
    # プロダクト情報の内容フィールド
    product_info_content = forms.CharField(widget=forms.Textarea, required=False)
    
    # プロダクト情報の画像フィールド
    product_info_image = forms.ImageField(required=False)

    # ケーススタディの名前フィールド
    case_study_name = forms.CharField(required=False)
    
    # ケーススタディの内容フィールド
    case_study_content = forms.CharField(widget=forms.Textarea, required=False)
    
    # ケーススタディの画像フィールド
    case_study_image = forms.ImageField(required=False)
    
    # 設立日のフィールド
    established = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Partners
        fields = [
            'name', 'logo', 'address', 'url', 'established', 'service', 'engineer', 'provision', 
            'service_content', 'ai_category', 'cost', 'product_info', 'case_study',
            'product_info_name', 'product_info_content', 'product_info_image',
            'case_study_name', 'case_study_content', 'case_study_image'
        ]

    def __init__(self, *args, **kwargs):
        """
        フォームの初期化メソッド。
        モデルのフィールドに関連するクエリセットを設定する。
        """
        super().__init__(*args, **kwargs)
        self.fields['service_content'].queryset = ServiceContent.objects.all()
        self.fields['ai_category'].queryset = AiCategory.objects.all()
        self.fields['cost'].queryset = Cost.objects.all()
        self.fields['product_info'].queryset = ProductInfo.objects.all()
        self.fields['case_study'].queryset = CaseStudy.objects.all()

class PartnerSearchForm(forms.Form):
    # 検索用のサービスコンテンツフィールド
    service_content = forms.ModelChoiceField(
        queryset=ServiceContent.objects.all(),
        required=False,
        label='サービス内容'
    )
    
    # 検索用のAIカテゴリフィールド
    ai_category = forms.ModelChoiceField(
        queryset=AiCategory.objects.all(),
        required=False,
        label='AIカテゴリ'
    )
    
    # 検索用のコストフィールド
    cost = forms.ModelChoiceField(
        queryset=Cost.objects.all(),
        required=False,
        label='コスト'
    )













