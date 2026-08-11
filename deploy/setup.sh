#!/bin/bash
# Aquafox 日本語化パック配布サイト — VPS初期セットアップスクリプト
# policy-log-jp とは完全に別ユーザー・別ディレクトリ・別プロセス（gunicorn/systemdサービス）で
# 動きます。nginxはoldmac.policy-log.jpというserver_nameで振り分ける別ファイル
# （/etc/nginx/sites-available/aquafox-ja）を追加するだけで、既存の policy-log の
# nginx設定ファイルやsystemdサービスには一切触れません。
# 使い方: VPSにファイルをアップロード後、rootで実行
#   sudo bash /var/www/aquafox-ja/deploy/setup.sh

set -e  # エラーで即停止

APP_DIR="/var/www/aquafox-ja"
APP_USER="aquafoxja"
LOG_DIR="/var/log/aquafox-ja"

echo "======================================"
echo "  Aquafox 日本語化パック配布サイト セットアップ開始"
echo "======================================"
echo ""

# ── Step 1: アプリ用ユーザー作成 ─────────
echo "[1/5] アプリ用ユーザー ($APP_USER) を作成..."
if id "$APP_USER" &>/dev/null; then
    echo "      $APP_USER は既に存在します（スキップ）"
else
    useradd -r -s /bin/bash -d $APP_DIR $APP_USER
    echo "      完了"
fi
echo ""

# ── Step 2: ディレクトリ権限設定 ─────────
echo "[2/5] ディレクトリ権限を設定..."
mkdir -p $LOG_DIR
chown -R $APP_USER:$APP_USER $APP_DIR
chown -R $APP_USER:$APP_USER $LOG_DIR
chmod 755 $APP_DIR
echo "      完了"
echo ""

# ── Step 3: Python仮想環境＋パッケージ ───
echo "[3/5] Pythonパッケージをインストール..."
su - $APP_USER -s /bin/bash -c "
    cd $APP_DIR
    python3 -m venv venv
    venv/bin/pip install -q --upgrade pip
    venv/bin/pip install -q -r requirements.txt
"
echo "      完了"
echo ""

# ── Step 4: systemdサービス登録 ──────────
echo "[4/5] アプリをサービスとして登録..."
cp $APP_DIR/deploy/aquafox-ja.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable aquafox-ja
systemctl start aquafox-ja
echo "      完了 (systemctl status aquafox-ja で確認できます)"
echo ""

# ── Step 5: nginx設定（oldmac.policy-log.jp サブドメイン用） ──
# name-based virtual hostなので、policy-log.jp本体が同じ80番ポートで
# 動いていてもserver_nameで振り分けられ、本体側の設定ファイルには触れない。
echo "[5/5] nginxを設定..."
cp $APP_DIR/deploy/nginx-aquafox-ja.conf /etc/nginx/sites-available/aquafox-ja
ln -sf /etc/nginx/sites-available/aquafox-ja /etc/nginx/sites-enabled/aquafox-ja
nginx -t
systemctl restart nginx
echo "      完了"
echo ""

echo "======================================"
echo "  セットアップ完了！"
echo "======================================"
echo ""
echo "【動作確認】 http://oldmac.policy-log.jp/ にアクセス"
echo "  ※事前にさくらのDNSで oldmac.policy-log.jp のAレコード(このVPSのIP)を"
echo "    追加し、反映されている必要があります。"
echo ""
echo "  systemctl status aquafox-ja   # アプリの状態"
echo "  systemctl status nginx        # nginxの状態"
echo "  tail -f $LOG_DIR/error.log   # エラーログ"
echo ""
echo "【SSL化】"
echo "  DNS反映を確認できたら以下を実行してHTTPS化する:"
echo "    certbot --nginx -d oldmac.policy-log.jp"
echo ""
