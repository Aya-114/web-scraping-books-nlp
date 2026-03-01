import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        f"https://books.toscrape.com/catalogue/page-{i}.html"
        for i in range(1, 51)
    ]

    def parse(self, response):
        books = response.css("article.product_pod")
        
        for book in books:
            relative = book.css("h3 a::attr(href)").get()
            book_url = response.urljoin(relative)

            yield scrapy.Request(
                url=book_url,
                callback=self.parse_book,
                meta={"page_number": response.url.split("-")[-1].replace(".html", "")}
            )

    def parse_book(self, response):
        yield {
            "Page": response.meta["page_number"],
            "Title": response.css("h1::text").get(),
            "Price": response.css(".price_color::text").get(),
            "Availability": response.css(".instock.availability::text").get().strip(),
            "Description": response.css("meta[name='description']::attr(content)").get(),
        }