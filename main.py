from bs4 import BeautifulSoup
import requests

urls_dark_knight = [
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/the_dark_knight/reviews?type=&sort=&page=7'
]

urls_love_and_monsters = [
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/love_and_monsters/reviews?type=&sort=&page=7'
]

urls_the_woman_in_the_window = [
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/the_woman_in_the_window_2020/reviews?type=&sort=&page=7'
]

urls_the_hitmans_body_guard = [
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/the_hitmans_bodyguard/reviews?type=&sort=&page=7'
]

urls_spiderman = [
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews',
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=2',
    'https://www.rotentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/spider_man_homecoming/reviews?type=&sort=&page=7'
]

urls_john_wick = [
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=2',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=3',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=4',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=5',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=6',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=7',
    'https://www.rottentomatoes.com/m/john_wick/reviews?type=&sort=fresh&page=8'
]

urls_army_of_dead = [
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=7',
    'https://www.rottentomatoes.com/m/army_of_the_dead_2021/reviews?type=&sort=&page=8'
]

urls_mortal_kombat = [
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=7',
    'https://www.rottentomatoes.com/m/mortal_kombat_2021/reviews?type=&sort=&page=8'
]

urls_interstellar = [
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=7',
    'https://www.rottentomatoes.com/m/interstellar_2014/reviews?type=&sort=&page=8'
]

urls_watchmen = [
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=2',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=3',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=4',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=5',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=6',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=7',
    'https://www.rottentomatoes.com/m/watchmen/reviews?type=&sort=&page=8'
]


def get_reviews(urls):
    reviews = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        review = soup.find_all('div', class_='the_review')
        reviews.append(review)
    return reviews


def write_to_file(reviews, file):
    for review in reviews:
        for i in range(len(review)):
            file.write(review[i].text)
    file.close()


def create_text_file(str):
    file = str + '.txt'
    file1 = open(file, 'w')
    return file1


reviews1 = get_reviews(urls_dark_knight)
reviews2 = get_reviews(urls_love_and_monsters)
reviews3 = get_reviews(urls_the_hitmans_body_guard)
reviews4 = get_reviews(urls_the_woman_in_the_window)
reviews5 = get_reviews(urls_army_of_dead)
reviews6 = get_reviews(urls_interstellar)
reviews7 = get_reviews(urls_john_wick)
reviews8 = get_reviews(urls_mortal_kombat)
reviews9 = get_reviews(urls_spiderman)
reviews10 = get_reviews(urls_watchmen)

output1 = create_text_file("the_dark_knight_review")
output2 = create_text_file("love_and_monsters")
output3 = create_text_file("the_hitmans_bodyguard")
output4 = create_text_file("the_woman_in_the_window")
output5 = create_text_file("the_army_of_dead")
output6 = create_text_file("interstellar_2014")
output7 = create_text_file("john_wick")
output8 = create_text_file("mortal_kombat_2021")
output9 = create_text_file("spider_man_homecoming")
output10 = create_text_file("watchmen")

write_to_file(reviews1, output1)
write_to_file(reviews2, output2)
write_to_file(reviews3, output3)
write_to_file(reviews4, output4)
write_to_file(reviews5, output5)
write_to_file(reviews6, output6)
write_to_file(reviews7, output7)
write_to_file(reviews8, output8)
write_to_file(reviews9, output9)
write_to_file(reviews10, output10)
