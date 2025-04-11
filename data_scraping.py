from google_play_scraper import reviews_all, Sort
import pandas as pd

def scrape_quora_reviews():
    # Scrape ulasan dari aplikasi Quora di Google Play Store
    reviews = reviews_all(
        'com.quora.android',  # ID aplikasi Quora
        lang='id',            # Bahasa ulasan
        country='id',         # Negara
        sort=Sort.MOST_RELEVANT,  # Urutan ulasan
        count=3000,          # Jumlah maksimum ulasan yang ingin diambil
        filter_score_with=None  # Tidak memfilter berdasarkan skor
    )

    # Simpan hasil ke CSV
    df = pd.DataFrame(reviews)
    df.to_csv('Quora_reviews.csv', index=False, encoding='utf-8')
    
    # Menampilkan jumlah ulasan yang diambil
    print(f"Scraped {len(df)} Quora reviews and saved to Quora_reviews.csv")

if __name__ == "__main__":
    scrape_quora_reviews()