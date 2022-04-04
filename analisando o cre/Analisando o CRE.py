#Fernanda tem um projeto de extensão e precisa selecionar alunos.
#Escreva um programa para que ela possa informar matrícula e CRE dos vários
#inscritos, e ver, ao final, a matrícula do aluno com menor CRE e o CRE médio de todos os candidatos.
acumulador=0
contador=0
t=10
x=0
while True:
    matricula=input()
    if matricula == '999':
        break
    cre=float(input())
    if cre > -10:
        acumulador+=cre
        contador+=1
        if cre<t:
            x=matricula
        t=cre
media=acumulador/contador
print('{}\n{:.2f}'.format(x,media))