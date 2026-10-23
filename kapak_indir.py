import urllib.request
import os

# Doğrudan çalışan kapak görseli bağlantıları
kapaklar = {
    "gta_v.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2ltt.jpg",
    "fifa_17.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1x76.jpg",
    "minecraft.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co4rkc.jpg",
    "the_last_of_us.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1r7f.jpg",
    "god_of_war_iii.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1tzz.jpg",
    "skyrim.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1tnw.jpg",
    "red_dead_redemption.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1qrg.jpg",
    "gta_san_andreas.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1wz4.jpg",
    "resident_evil_4.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co1s54.jpg",
    "pes_2013.jpg": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2gso.jpg"
}

klasor = "kapaklar"
os.makedirs(klasor, exist_ok=True)

print("Kapak görselleri indiriliyor...\n")

headers = {'User-Agent': 'Mozilla/5.0'}

for dosya_adi, url in kapaklar.items():
    dosya_yolu = os.path.join(klasor, dosya_adi)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dosya_yolu, 'wb') as f:
            f.write(response.read())
        print(f"[BAŞARILI] {dosya_adi} indirildi.")
    except Exception as e:
        print(f"[HATA] {dosya_adi} indirilemedi: {e}")

print("\nİşlem tamamlandı!")
