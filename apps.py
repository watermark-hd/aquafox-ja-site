# 配布アプリの一覧。アプリを追加する場合は以下のリストにエントリを足し、
# templates/apps/<slug>.html を用意し、static/downloads/ に配布ファイルを置く。
APPS = [
    {
        "slug": "aquafox-ja",
        "name": "Aquafox 日本語化パック",
        "tagline": "PowerPC Mac 向けブラウザ「Aquafox」を日本語表示にする言語パック",
        "filename": "aquafox-ja.xpi",
    },
]

APPS_BY_SLUG = {app["slug"]: app for app in APPS}
