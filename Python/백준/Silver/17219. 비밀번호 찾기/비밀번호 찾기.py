import sys
input = sys.stdin.readline

site_num, test_case = map(int, input().rstrip().split())
site_dict = {}
for _ in range(site_num):
    site, pswd = input().rstrip().split()
    site_dict[site] = pswd

result = [site_dict[input().rstrip()] for _ in range(test_case)]
print('\n'.join(result))