# Average 3

student_scores = input().split(' ')

n1, n2, n3, n4 = student_scores

n1 = round(float(n1),1)
n2 = round(float(n2),1)
n3 = round(float(n3),1)
n4 = round(float(n4),1)

try:
    exam_score = float(input())
except EOFError:
    pass

avg = float(((n1*2.0)+(n2*3.0)+(n3*4.0)+(n4*1.0))/10)

print("Media: %.1f"%(avg))
if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    print("Nota do exame: %.1f"%(exam_score))
    avg_final = (avg + exam_score)/2
    if avg_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % (avg_final))