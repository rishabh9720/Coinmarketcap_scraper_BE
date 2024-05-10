from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "coinmarketcap_data_scrapper_task": {
        "task": "apps.scraper.tasks.scrape_coinmarket_data_and_post",
        "schedule": 20,
        "description": "Task to scrape data from coinmarket every 20 seconds",
    },
}
