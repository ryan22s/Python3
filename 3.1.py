george_v = "His Majesty George V, by the Grace of God, " \
           "of the United Kingdom of Great Britain and " \
           "Ireland and of the British Dominions beyond " \
           "the Seas, King, Defender of the Faith, Emperor of India"
ghandi = 'Mohandas Karamchand Gandhi'
john_f_kennedy = 'JFK'

print(len(george_v), 'characters is much too long of a name!')
print(len(ghandi), 'characters is better...')
print(len(john_f_kennedy), 'characters is short enough.')
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_number = int(input('Enter number to use as index: \n'))
print('\nLetter', user_number, 'of the alphabet is', alphabet[user_number])

current_time = '2014-07-26 02:12:18:'
my_city = ''
my_state = ''
log_entry = ''
my_city = str(input())
my_state = str(input())
''' Your solution goes here '''
sp = " "
sqnc = (current_time, my_city, my_state)
log_entry = sp.join(sqnc)
print(log_entry)
