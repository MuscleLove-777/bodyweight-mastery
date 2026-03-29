"""自重トレの極意 - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "自重トレの極意"
BLOG_DESCRIPTION = "自宅でできる自重トレーニング・自体重エクササイズ完全ガイド"
BLOG_URL = "https://musclelove-777.github.io/bodyweight-mastery"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/bodyweight-mastery"

TARGET_CATEGORIES = [
    "自重筋トレメニュー",
    "カリステニクス",
    "自宅トレーニング",
    "初心者ガイド",
    "上級テクニック",
]

THEME = {
    "primary": "#0891b2",
    "accent": "#06b6d4",
    "gradient_start": "#0891b2",
    "gradient_end": "#0284c7",
    "dark_bg": "#0a1520",
    "dark_surface": "#152530",
    "light_bg": "#ecfeff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [6, 18]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "トレーニング器具": [
        {"service": "Amazon 懸垂バー", "url": "https://www.amazon.co.jp", "description": "ドア取付型チンニングバー"},
        {"service": "Amazon ディップスタンド", "url": "https://www.amazon.co.jp", "description": "自重トレ用ディップススタンド"},
        {"service": "Amazon ヨガマット", "url": "https://www.amazon.co.jp", "description": "トレーニングマット"},
    ],
    "プロテイン": [
        {"service": "マイプロテイン", "url": "https://www.myprotein.jp", "description": "ホエイプロテイン"},
        {"service": "Amazon プロテイン", "url": "https://www.amazon.co.jp", "description": "プロテイン各種"},
    ],
    "書籍・DVD": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "自重トレーニング書籍"},
        {"service": "楽天ブックス", "url": "https://books.rakuten.co.jp", "description": "カリステニクス関連書籍"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080
