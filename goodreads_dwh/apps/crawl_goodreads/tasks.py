from celery import shared_task
from crawler import crawler

@shared_task
def crawl_book():
    return