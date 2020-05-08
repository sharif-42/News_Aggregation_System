from django.db import models

from news_processor.managers import NewsManager


class News(models.Model):
    MOST_READ = 'Most Read'
    BREAKING_NEWS = 'Breaking News'
    NATIONAL = 'National'
    INTER_NATIONAL = 'Inter National'
    POLITICS = 'Politics'
    SPORTS = 'Sports'
    ENTERTAINMENT = 'Entertainment'
    TECHNOLOGY = 'Technology'
    ENGLISH = 'English'
    BANGLA = "Bangla"

    CATEGORY_CHOICES = [
        (MOST_READ, 'most_read'),
        (BREAKING_NEWS, 'breaking_news'),
        (NATIONAL, 'national'),
        (INTER_NATIONAL, 'international'),
        (POLITICS, 'politics'),
        (SPORTS, 'sports'),
        (ENTERTAINMENT, 'entertainment'),
        (TECHNOLOGY, 'technology'),
    ]
    TYPE_CHOICES = [
        (BANGLA, 'bangla'),
        (ENGLISH, 'english')
    ]
    id = models.BigAutoField(primary_key=True, db_index=True)
    news_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=BANGLA,
        help_text="Type of the News"
    )
    author = models.CharField(
        max_length=100,
        help_text="Newspaper Name"
    )
    url = models.URLField(help_text="URL of the collected News")
    headline = models.CharField(
        max_length=200,
        help_text="Headline of the News"
    )
    news_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=MOST_READ,
        help_text='Category of the News'
    )
    published_time = models.DateTimeField(
        auto_now_add=True,
        help_text='Published Time'
    )
    summary = models.TextField(
        max_length=500,
        help_text="Summary of the Collected News",
        null=True, blank=True,
    )
    objects = NewsManager()

    def __str__(self):
        return '{} - {} - {}'.format(self.TYPE_CHOICES, self.news_category, self.author)

    class Meta:
        indexes = [
            models.Index(fields=['id', 'news_category', 'news_type', 'published_time']),
            # models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        verbose_name = "Collected News"
        verbose_name_plural = "Collected News"
