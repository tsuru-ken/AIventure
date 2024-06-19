from pathlib import Path
import os

# プロジェクトのベースディレクトリを構築
BASE_DIR = Path(__file__).resolve().parent.parent

# 環境によって設定を切り替える
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')  # 環境変数 'DJANGO_ENVIRONMENT' を参照するが、デフォルトは 'development'

# 開発環境の設定
if ENVIRONMENT == 'development':
    # クイックスタート開発設定 - 本番環境には適さない
    # 詳細は https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ を参照

    # 本番環境では秘密にしておくべきシークレットキー
    SECRET_KEY = 'django-insecure-u0a)edlju*nn^%!=i-4fw$kagcsyxeh4ckh54p*9ya1upo*y5v'

    # 本番環境ではデバッグを無効にする
    DEBUG = True

    # デバッグモードが有効な場合は全てのホストを許可
    ALLOWED_HOSTS = ['*']
else:
    # 本番環境の設定
    SECRET_KEY = 'your-production-secret-key'  # 本番環境用のシークレットキーに変更
    DEBUG = False
    ALLOWED_HOSTS = ['your-domain.com', '57.181.214.237']

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'partners.apps.PartnersConfig',
    'image_generation.apps.ImageGenerationConfig',
    'ai_models.apps.AiModelsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aiventure.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aiventure.wsgi.application'

# データベース
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワード検証
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国際化設定
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# 静的ファイル (CSS, JavaScript, 画像) の設定
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
if ENVIRONMENT != 'development':
    STATIC_ROOT = BASE_DIR / "staticfiles"

# デフォルトのプライマリキーのフィールドタイプ
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# カスタムユーザーモデル
AUTH_USER_MODEL = 'users.CustomUser'

# ログイン後にリダイレクトするURLを設定します。
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# メディアファイルの設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Logging configuration
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#         'myapp': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }




