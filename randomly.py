import random


class RandomMoods:
	@staticmethod
	def random_positive():
		positive_list1 = ['Отлчно,', 'Классно,', 'Очень хорошо,', 'Супер,', 'Это же отличная новость,']
		positive_list2 = ['хорошего дня', 'так держать', 'ты большой молодец,', 'как раз то, что нужно', 'как тебе это удается?']
		positive_emoji = ['😀', '😉', '😋', '🥳']
		positive_words = random.choice(positive_list1) + ' ' + random.choice(positive_list2) + ' ' + random.choice(positive_emoji)
		return positive_words

	@staticmethod
	def random_negative():
		negative_list1 = ['Очень жаль,', 'Ты чего,', 'Бывает и хуже,', 'Взбодрись,', 'Не унывай,', 'Расслабься,']
		negative_list2 = ['не грусти', 'это не конец света', 'улыбнись']
		negative_emoji = ['🙂', '😌', '💋', '😇']
		negative_words = random.choice(negative_list1) + ' ' + random.choice(negative_list2) + ' ' + random.choice(negative_emoji)
		return negative_words
#mod write by me
#mod write by me on mac