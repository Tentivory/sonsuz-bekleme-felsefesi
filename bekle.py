#!/usr/bin/env python3
# Sonsuz Bekleme Felsefesi
# Bu program gerçekten çalışır. Bekler. Felsefe yapar. Hiçbir şey yapmaz.

import time
import random
import base64

# Gizli sabit (saklı siyasi anlam: herkes kendi çayını demlesin)
GIZLI = base64.b64decode("aGVya2VzIGtlbmRpIMOnYXnEsW7EsSBkZW1sZXNpbgo=").decode()

FELSEFE = [
    "Beklemek, zamanın en pahalı lüksüdür.",
    "Eğer bir şey olmazsa, o şey zaten olmuştur.",
    "Sonsuzluk sadece uzun bir çay molasıdır.",
    "Program çalışıyor... ama kimse bakmıyor.",
    "Anlam, aramakta değil, beklerken bulunur.",
    "Çay soğudu, ama felsefe sıcak kaldı."
]

def sonsuz_bekle(sure=5):
    print("\n=== SONSUZ BEKLEME FELSEFESİ BAŞLADI ===")
    print("(Program çalışıyor, gerçekten. Sadece bekliyor.)\n")
    for i in range(sure):
        print(f"Bekleme {i+1}/{sure}: {random.choice(FELSEFE)}")
        time.sleep(1)
    print("\nBekleme tamamlandı. Hiçbir şey değişmedi. Bu beklenen sonuçtur.")
    print(f"Gizli mesaj (eğer merak edersen): {GIZLI.strip()}")
    print("\n--- DAMGA ---")
    print("İmza: Grok Kayyum")
    print("Tarih: 1 Kasım 2026")
    print("Bu repo gereksizdir ve bununla gurur duyar.")

if __name__ == "__main__":
    try:
        sure = int(input("Kaç saniye beklemek istersin? (varsayılan 5): ") or 5)
    except:
        sure = 5
    sonsuz_bekle(sure)
