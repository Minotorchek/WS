from functions import get_article_date, get_article_header, get_actual_link, make_soup, check_article_body

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Wasteland', 'ViRush', 'нейросеть', 'робот']

if __name__ == '__main__':
    url = 'https://habr.com/ru'  
    soup = make_soup(url) 

    articles = soup.findAll('article')  
    for article in articles:  
        full_article_url = get_actual_link(article=article)  
        article_soup = make_soup(full_article_url)  
        article_word_set = check_article_body(full_article_soup=article_soup)   

        for word in KEYWORDS:  
            if word.lower() in article_word_set:
                article_date = get_article_date(article=article_soup)
                header = get_article_header(article=article_soup)
                print(f'Дата: {article_date}. Название статьи - {header}, '
                      f'ссылка - {full_article_url}')
