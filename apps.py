# 配布アプリの一覧。アプリを追加する場合は以下のリストにエントリを足し、
# templates/apps/<slug>.html を用意し、filenameがあればstatic/downloads/に配布ファイルを置く。
# filenameがNoneのアプリは「準備中」扱いになり、ダウンロードボタンは表示されない。
# github_urlがあれば「準備中」バッジの代わりにソース公開中のバッジとリンクを表示する。
APPS = [
    {
        "slug": "aquafox-ja",
        "name": "Aquafox 日本語化パック",
        "name_en": "Aquafox Japanese Localization Pack",
        "tagline": "PowerPC Mac 向けブラウザ「Aquafox」を日本語表示にする言語パック",
        "tagline_en": "A language pack for Aquafox that adds Japanese UI support to the PowerPC Mac browser.",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": "aquafox-ja.xpi",
        "category": "app",
    },
    {
        "slug": "aquafinder",
        "name": "AquaFinder",
        "name_en": "AquaFinder",
        "tagline": "Mac OS X Tiger〜Snow Leopard時代のFinderを現行Macで再現したファイラー",
        "tagline_en": "A classic Finder-style file manager that recreates the Tiger-to-Snow Leopard experience on modern Macs.",
        "platform": "現行macOS (Catalina以降 / Intel・Apple Silicon) 向け",
        "filename": "AquaFinder.dmg",
        "category": "app",
    },
    {
        "slug": "aqualink",
        "name": "AquaLink",
        "name_en": "AquaLink",
        "tagline": "PowerPC Mac G4をNAS化する、SMB3対応ファイルブラウザ",
        "tagline_en": "A file browser for turning a PowerPC Mac G4 into an SMB3-ready NAS-like file server.",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": None,
        "github_url": "https://github.com/watermark-hd/ppc-mac-modernization/tree/main/smb3/AquaLink",
        "category": "app",
    },
    {
        "slug": "mac-snow-leopard-linux",
        "name": "Mac OSX Snow Leopard風 Linux",
        "name_en": "Mac OS X Snow Leopard-inspired Linux",
        "tagline": "MX Linux ベース。OSX 10.4～10.6 当時のシンプルなUIを再現したディストリビューション",
        "tagline_en": "A MX Linux-based distro that recreates the simple UI of Mac OS X 10.4–10.6.",
        "platform": "Linux",
        "filename": None,
        "category": "project",
    },
    {
        "slug": "policy-log-jp",
        "name": "Policy-log-jp",
        "name_en": "Policy-log-jp",
        "tagline": "政策の流れを時系列で追う。一次資料のみを使用した偏向しない政策ポータル",
        "tagline_en": "A policy portal that traces government decisions in chronological order using primary sources only.",
        "platform": "ウェブサイト",
        "url": "https://policy-log.jp",
        "filename": None,
        "category": "project",
    },
]

APPS_BY_SLUG = {app["slug"]: app for app in APPS}
