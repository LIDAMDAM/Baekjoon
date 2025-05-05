import sys
input = sys.stdin.readline

test_date, good_len, bad_len = map(int, input().rstrip().split())
good_onion, bad_onion = 1, 1

for _ in range(test_date):
    good_onion += good_len
    bad_onion += bad_len
    if good_onion < bad_onion: good_onion, bad_onion = bad_onion, good_onion
    elif good_onion == bad_onion: bad_onion -= 1

print(good_onion, bad_onion)