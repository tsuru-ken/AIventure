from django.db import models

class Partners(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    address = models.CharField(max_length=255)
    url = models.URLField()
    established = models.DateField()
    service = models.TextField()
    engineer = models.IntegerField()
    provision = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    service_content = models.ManyToManyField('ServiceContent',blank=True)
    ai_category = models.ManyToManyField('AiCategory',blank=True)
    cost = models.ManyToManyField('Cost',blank=True)
    product_info = models.ManyToManyField('ProductInfo',blank=True)
    case_study = models.ManyToManyField('CaseStudy',blank=True)


    def __str__(self):
        return self.name

class ServiceContent(models.Model):
    division = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.division

class AiCategory(models.Model):
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre

class Cost(models.Model):
    breakdown = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.breakdown

class PartnerServiceContentLabel(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    service_content = models.ForeignKey(ServiceContent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.partner.name} - {self.service_content.division}'

class PartnerAicategoryLabel(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    ai_category = models.ForeignKey(AiCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.partner.name} - {self.ai_category.genre}'

class PartnerCostLabel(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.partner.name} - {self.cost.breakdown}'

class CaseStudy(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='case_studies/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# # ManyToManyFieldの定義をPartnersモデルに追加
# Partners.add_to_class('service_content', models.ManyToManyField(ServiceContent, blank=True))
# Partners.add_to_class('ai_category', models.ManyToManyField(AiCategory, blank=True))
# Partners.add_to_class('cost', models.ManyToManyField(Cost, blank=True))
# Partners.add_to_class('product_info', models.ManyToManyField(ProductInfo, blank=True))
# Partners.add_to_class('case_study', models.ManyToManyField(CaseStudy, blank=True))




