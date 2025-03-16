import sys

cr_gr = float(0)
cr_total = float(0)
grade_change = ['A+',"A0",'B+','B0','C+','C0','D+','D0','F']
num_change = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    name, credit, grade  = line.split()
    if grade == 'P':
        continue
    for i in range(9):
        if grade == grade_change[i]:
            gr_num = float(num_change[i])
            break
    cr_gr += float(credit)*float(gr_num)
    cr_total += float(credit)

print(round(cr_gr/cr_total,6))