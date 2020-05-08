# Simple_Scrappy_Project

## Installation Guidelines
- Create Virtualenvironment
    ~~~~
    virtualenv venv --python=python3.6 #for python3.6
    ~~~~
- Install Scrapy
    ~~~~
    pip install Scrapy
    ~~~~
- Start a Project
    ~~~~
    scrapy startproject demo_scrapy_project
    ~~~~
- Install MySQL Client
    ~~~~
    pip install mysqlclient
    ~~~~
  
## Necessary Commands
- Run a spider
    ~~~~
    scrapy crawl quotes #here qoute is the unique name of the spider
    ~~~~
- Save the scrapped data to a json file
    ~~~~
    scrapy crawl quotes -o quotes.json
    ~~~~
    For historic reasons, Scrapy appends to a given file instead 
    of overwriting its contents. If you run this command twice without 
    removing the file before the second time, you’ll end up with a broken JSON file.
- Use other format ex. JSON Lines:
    ~~~~
    scrapy crawl quotes -o quotes.jl
    ~~~~
    The JSON Lines format is useful because it’s stream-like, 
    you can easily append new records to it. It doesn’t have 
    the same problem of JSON when you run twice. Also, as each record is a separate line.
- Use Scrappy Shell
    ~~~~
    scrapy shell 'http://quotes.toscrape.com/page/1/'
    ~~~~
   
## Basic Terminology
### Spiders:
Spiders are classes which define how a certain site (or a group of sites)
 will be scraped, including how to perform the crawl (i.e. follow links) 
 and how to extract structured data from their pages (i.e. scraping items). 
 In other words, Spiders are the place where you define the custom behaviour 
 for crawling and parsing pages for a particular site (or, in some cases, 
 a group of sites).
 
 
## Some Findings For A Scalable Scrapper:

### Concurrency
The default global concurrency limit in Scrapy is not suitable for crawling 
many different domains in parallel, so you will want to increase it. 
How much to increase it will depend on how much CPU and memory you 
crawler will have available.
A good starting point is <b>100:</b>
~~~~
CONCURRENT_REQUESTS = 100
~~~~
But the best way to find out is by doing some trials and identifying at what concurrency your Scrapy process gets CPU 
bounded. For optimum performance, you should pick a concurrency where CPU usage is at 80-90%.

Increasing concurrency also increases memory usage. If memory usage is a concern, you might need to lower your global 
concurrency limit accordingly.

### Increase Twisted IO thread pool maximum size
Currently Scrapy does DNS resolution in a blocking way with usage of thread pool. 
With higher concurrency levels the crawling could be slow or even fail hitting DNS 
resolver timeouts. Possible solution to increase the number of threads handling DNS 
queries. The DNS queue will be processed faster speeding up establishing of connection 
and crawling overall.

To increase maximum thread pool size use:
~~~~
REACTOR_THREADPOOL_MAXSIZE = 20
~~~~
### Setup your own DNS
If you have multiple crawling processes and single central DNS, it can act like DoS 
attack on the DNS server resulting to slow down of entire network or even blocking your 
machines. To avoid this setup your own DNS server with local cache and upstream to some 
large DNS like OpenDNS or Verizon.

### Reduce log level
When doing broad crawls you are often only interested in the crawl rates you get and any 
errors found. These stats are reported by Scrapy when using the INFO log level. 
In order to save CPU (and log storage requirements) you should not use DEBUG log level 
when preforming large broad crawls in production. Using DEBUG level when developing your 
(broad) crawler may be fine though.

To set the log level use:
~~~~
LOG_LEVEL = 'INFO'
~~~~
### Disable cookies
Disable cookies unless you really need. Cookies are often not needed when doing broad 
crawls (search engine crawlers ignore them), and they improve performance by saving 
some CPU cycles and reducing the memory footprint of your Scrapy crawler.

To disable cookies use:
~~~~
COOKIES_ENABLED = False
~~~~

### Disable retries
Retrying failed HTTP requests can slow down the crawls substantially, specially when 
sites causes are very slow (or fail) to respond, thus causing a timeout error which gets
retried many times, unnecessarily, preventing crawler capacity to be reused for other 
domains.

To disable retries use:
~~~~
RETRY_ENABLED = False
~~~~
### Reduce download timeout
Unless you are crawling from a very slow connection (which shouldn’t be the case for 
broad crawls) reduce the download timeout so that stuck requests are discarded quickly 
and free up capacity to process the next ones.

To reduce the download timeout use:
~~~~
DOWNLOAD_TIMEOUT = 15
~~~~
### Disable redirects
Consider disabling redirects, unless you are interested in following them. When doing 
broad crawls it’s common to save redirects and resolve them when revisiting the site 
at a later crawl. This also help to keep the number of request constant per crawl batch, 
otherwise redirect loops may cause the crawler to dedicate too many resources on any 
specific domain.

To disable redirects use:
~~~~
REDIRECT_ENABLED = False
~~~~
### Enable crawling of “Ajax Crawlable Pages”
Some pages (up to 1%, based on empirical data from year 2013) declare themselves as ajax
crawlable. This means they provide plain HTML version of content that is usually 
available only via AJAX. Pages can indicate it in two ways:
- by using #! in URL - this is the default way;
- by using a special meta tag - this way is used on “main”, “index” website pages.

Scrapy handles (1) automatically; to handle (2) enable AjaxCrawlMiddleware:
~~~~
AJAXCRAWL_ENABLED = True
~~~~
When doing broad crawls it’s common to crawl a lot of “index” web pages; 
AjaxCrawlMiddleware helps to crawl them correctly. It is turned OFF by default because 
it has some performance overhead, and enabling it for focused crawls doesn’t make much 
sense.

### Crawl in BFO order
Scrapy crawls in [DFO order](https://docs.scrapy.org/en/latest/faq.html#faq-bfo-dfo) by default.

In broad crawls, however, page crawling tends to be faster than page processing. 
As a result, unprocessed early requests stay in memory until the final depth is reached,
which can significantly increase memory usage.
[Crawl in BFO](https://docs.scrapy.org/en/latest/faq.html#faq-bfo-dfo) order instead to save memory.








