# 配布アプリの一覧。アプリを追加する場合は以下のリストにエントリを足し、
# templates/apps/<slug>.html を用意し、filenameがあればstatic/downloads/に配布ファイルを置く。
# filenameがNoneのアプリは「準備中」扱いになり、ダウンロードボタンは表示されない。
APPS = [
    {
        "slug": "aquafox-ja",
        "name": "Aquafox 日本語化パック",
        "tagline": "PowerPC Mac 向けブラウザ「Aquafox」を日本語表示にする言語パック",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": "aquafox-ja.xpi",
    },
    {
        "slug": "aquafinder",
        "name": "AquaFinder",
        "tagline": "Mac OS X Tiger〜Snow Leopard時代のFinderを現行Macで再現したファイラー",
        "platform": "現行macOS (Catalina以降 / Intel・Apple Silicon) 向け",
        "filename": "AquaFinder.dmg",
    },
    {
        "slug": "aqualink",
        "name": "AquaLink",
        "tagline": "PowerPC Mac G4をNAS化する、SMB3対応ファイルブラウザ",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": None,
    },
]

APPS_BY_SLUG = {app["slug"]: app for app in APPS}
