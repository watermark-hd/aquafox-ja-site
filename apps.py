# 配布アプリの一覧。アプリを追加する場合は以下のリストにエントリを足し、
# templates/apps/<slug>.html を用意し、filenameがあればstatic/downloads/に配布ファイルを置く。
# filenameがNoneのアプリは「準備中」扱いになり、ダウンロードボタンは表示されない。
# github_urlがあれば「準備中」バッジの代わりにソース公開中のバッジとリンクを表示する。
# 最終更新日は配布ファイルのmtimeから自動算出するため、ここには書かない。
# changelogは手書きの更新履歴（新しい順）。無くても動くので、更新時に書ければ追記する。
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
        "filename": "AquaLink.zip",
        "github_url": "https://github.com/watermark-hd/ppc-mac-modernization/tree/main/smb3/AquaLink",
        "category": "app",
        "changelog": [
            {
                "date": "2026-08-20",
                "note": "UIを英語対応(日本語/英語切り替え)",
                "note_en": "Added English UI support (switchable between Japanese and English)",
            },
            {
                "date": "2026-08-20",
                "note": "メニューバーが開かなくなる不具合を修正",
                "note_en": "Fixed an issue where the menu bar would fail to open",
            },
        ],
    },
    {
        "slug": "ppc-claude-agent",
        "name": "PPC Claude Agent",
        "name_en": "PPC Claude Agent",
        "tagline": "PowerPC Mac (Tiger)のターミナルからClaudeと会話できる、Perl製の自己完結型AIエージェント",
        "tagline_en": "A self-contained Perl agent that lets you talk to Claude from the Terminal on a PowerPC Mac (Tiger).",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": "ppc-claude-agent.zip",
        "category": "app",
        "changelog": [
            {
                "date": "2026-08-22",
                "note": "IME経由の日本語入力に0x16のゴミバイトが混入し文字化けする不具合を修正",
                "note_en": "Fixed Japanese IME input getting corrupted by a stray 0x16 byte",
            },
            {
                "date": "2026-08-22",
                "note": "Install.commandの「Enterキーで閉じます」という実態と異なる表示を修正",
                "note_en": "Fixed Install.command's misleading \"Press Enter to close this window\" message",
            },
            {
                "date": "2026-08-22",
                "note": "特定の入力の直後にEnterキーが認識されないことがある不具合を修正",
                "note_en": "Fixed Enter sometimes being silently swallowed right after certain input",
            },
            {
                "date": "2026-08-22",
                "note": "日本語などの入力時、1文字ごとに改行され行編集ができない不具合を修正",
                "note_en": "Fixed every keystroke pushing the terminal down a new line instead of editing in place",
            },
            {
                "date": "2026-08-22",
                "note": "日本語入力時に画面が「◆」で埋まる文字化けを修正",
                "note_en": "Fixed Japanese input filling the screen with garbled \"◆\" characters",
            },
            {
                "date": "2026-08-22",
                "note": "インストーラー再実行時にAnthropic APIキーの再入力を求められる不具合を修正",
                "note_en": "Fixed the installer prompting to re-enter the Anthropic API key when re-run for an upgrade",
            },
            {
                "date": "2026-08-22",
                "note": "矢印キー入力でカーソル移動の代わりに文字が挿入されてしまう不具合を修正",
                "note_en": "Fixed arrow keys inserting garbage characters instead of moving the cursor",
            },
        ],
    },
    {
        "slug": "exfat-tiger-ppc",
        "name": "exFAT for Tiger (PowerPC)",
        "name_en": "exFAT for Tiger (PowerPC)",
        "tagline": "PowerPC Mac OS X 10.4 (Tiger)でexFATドライブの読み書き・マウントができるようにするメニューバーアプリ",
        "tagline_en": "A menu bar app that lets PowerPC Mac OS X 10.4 (Tiger) read, write, and mount exFAT drives.",
        "platform": "PowerPC Mac (Tiger) 向け",
        "filename": "exfat-tiger-ppc.zip",
        "github_url": "https://github.com/watermark-hd/exfat-tiger-ppc",
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
