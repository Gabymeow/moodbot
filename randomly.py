import random
class random_moods:
	def random_happy():
		happy_list1 = ['Отлчно,','Классно,','Очень хорошо,','Супер,']
		happy_list2 = ['хорошего дня','так держать','ты молодец']
		happy_emoji = ['😀','😉','☺️']
		happy_words = random.choice(happy_list1) + ' ' + random.choice(happy_list2)+ ' ' + random.choice(happy_emoji)
		return happy_words
	def random_unhappy():
		unhappy_list1 = ['Очень жаль,','Ты чего,','Бывает и хуже,']
		unhappy_list2 = ['не грусти','это не конец света','улыбнись']
		unhappy_emoji = ['🙂','😉','💋']
		unhappy_words = random.choice(unhappy_list1) + ' ' + random.choice(unhappy_list2)+ ' ' + random.choice(unhappy_emoji)
		return unhappy_words
