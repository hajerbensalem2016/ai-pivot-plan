#!/bin/bash
# Setup au bureau — à sourcer avec : source ~/setup_bureau.sh
# (ne pas exécuter directement, les exports ne persisteraient pas)

echo "Setup bureau AMF — AI Pivot Project"
echo "===================================="

# 1. Vérifier que wsl-vpnkit tourne
if ip route | grep -q "192.168.127.1"; then
    echo "[OK] wsl-vpnkit actif (route via 192.168.127.1)"
else
    echo "[WARN] wsl-vpnkit NON actif"
    echo "       Lance-le depuis PowerShell Windows :"
    echo "       wsl -d wsl-vpnkit --cd /app ./wsl-vpnkit"
fi

# 2. Fixer le DNS si besoin
if ! grep -q "192.168.127.1" /etc/resolv.conf; then
    echo "[FIX] Mise à jour /etc/resolv.conf"
    echo "nameserver 192.168.127.1" | sudo tee /etc/resolv.conf > /dev/null
else
    echo "[OK] DNS /etc/resolv.conf correct (192.168.127.1)"
fi

# 3. Exports proxy + SSL
export HTTP_PROXY=http://185.46.212.41:10299
export HTTPS_PROXY=http://185.46.212.41:10299
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
echo "[OK] Proxy + SSL exportés"

# 4. Activer le venv
if [ -d "$HOME/ai-rag-project/venv" ]; then
    cd "$HOME/ai-rag-project"
    source venv/bin/activate
    echo "[OK] venv activé (prompt doit afficher '(venv)')"
else
    echo "[WARN] venv non trouvé dans ~/ai-rag-project/"
fi

echo "===================================="
echo "Prête à bosser."
