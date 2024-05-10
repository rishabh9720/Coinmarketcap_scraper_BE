from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "scrap_data_from_coin_market": {
        "task": "apps.scraper.tasks.scrape_data_from_coin_market",
        "schedule": 15,  # Execute every 15 seconds
        "description": "Scrape data from coin market every 15 seconds",
    },
}
