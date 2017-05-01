"""If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage."""

ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

teens = {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen',
         '4': 'fourteen', '5': 'fifteen', '6': 'sixteen', '7': 'seventeen',
         '8': 'eighteen', '9': 'nineteen'}

tens = {'0': '', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
        '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}


def get_number_letter_counts(min_num=1, max_num=1000):

    numbers = []

    for num in xrange(min_num, max_num + 1):
        numbers.append(str(num))

    letter_counts = []
    number_words = []

    for num in numbers:

        if len(num) == 3:
            hundreds_word = ones[num[0]] + 'hundred'

            if num[-2] == '1':
                tens_word = teens[num[-1]]
                num_word = hundreds_word + 'and' + tens_word
            else:
                ones_word = ones[num[-1]]
                tens_word = tens[num[-2]]
                if ones_word and tens_word:
                    num_word = hundreds_word + 'and' + tens_word + ones_word
                elif ones_word:
                    num_word = hundreds_word + 'and' + ones_word
                elif tens_word:
                    num_word = hundreds_word + 'and' + tens_word
                else:
                    num_word = hundreds_word

        elif len(num) == 2:
            if num[-2] == '1':
                num_word = teens[num[-1]]
            else:
                ones_word = ones[num[-1]]
                tens_word = tens[num[-2]]
                num_word = tens_word + ones_word

        elif len(num) == 1:
            num_word = ones[num[-1]]

        elif len(num) == 4:
            num_word = 'onethousand'

        number_words.append(num_word)
        letter_counts.append(len(num_word))
    print sum(letter_counts)
    return number_words
