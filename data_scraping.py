from google_play_scraper import reviews_all, Sort
import pandas as pd

def scrape_facebook_reviews():
    # Scrape Facebook reviews dari Google Play Store
    reviews = reviews_all(
        'com.facebook.katana',  # ID aplikasi Facebook
        lang='id',              
        country='id',           
        sort=Sort.MOST_RELEVANT,
        count=3000,
        filter_score_with=None
    )

    # Simpan hasil ke CSV
    df = pd.DataFrame(reviews)
    df.to_csv('facebook_reviews.csv', index=False)
    print(f"Scraped {len(df)} Facebook reviews and saved to facebook_reviews.csv")

if __name__ == "__main__":
    scrape_facebook_reviews()
