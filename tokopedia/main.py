from Crawling_tokopedia import Scraper

if __name__ == "__main__":
  scraper = Scraper()

  datas = scraper.get_data()
  index = 1

  for data in datas:
    print(
      index,
      data['name'],
      data['img'],
      data['price'],
      data['city']
    )

    index += 1