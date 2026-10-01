#!/bin/bash
# Setup à la maison — à sourcer avec : source ~/setup_maison.sh
# (pas de VPN AMF, pas de proxy, DNS normal)

echo "Setup maison — AI Pivot Project"
echo "================================"

# 1. Vérifier qu'il n'y a pas de wsl-vpnkit résiduel
if ip route | grep -q "192.168.127.1"; then
    echo "[WARN] wsl-vpnkit ENCORE actif (reliquat du bureau)"
    echo "       Ferme la fenêtre PowerShell wsl-vpnkit si elle est ouverte"
    echo "       Ou redémarre WSL : wsl --shutdown dans PowerShell"
fi

# 2. Reset DNS vers un DNS public (si venv-pkit a laissé 192.168.127.1)
if grep -q "192.168.127.1" /etc/resolv.conf; then
    echo "[FIX] Reset /etc/resolv.conf vers DNS public"
    echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" | sudo tee /etc/resolv.conf > /dev/null
else
    echo "[OK] DNS /etc/resolv.conf correct"
fi

# 3. Désactiver les proxies (ils sont pour le bureau uniquement)
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
unset REQUESTS_CA_BUNDLE SSL_CERT_FILE
echo "[OK] Proxies et SSL vars nettoyés"

# 4. Activer le venv
if [ -d "$HOME/ai-rag-project/venv" ]; then
    cd "$HOME/ai-rag-project"
    source venv/bin/activate
    echo "[OK] venv activé (prompt doit afficher '(venv)')"
else
    echo "[WARN] venv non trouvé dans ~/ai-rag-project/"
fi

echo "================================"
echo "Prête à bosser."
