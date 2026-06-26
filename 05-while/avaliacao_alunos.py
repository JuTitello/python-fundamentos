
totalAvaliado = 0
quantAlunos = int(input("Digite a quantidade de alunos a serem avaliados: "))


while totalAvaliado < quantAlunos:

    print(f"\nTotal avaliado {totalAvaliado + 1} de {quantAlunos}")

    nomeAluno = input("Informe o nome do aluno: ")

    nota_1 = float(input("Informa a nota da 1ª avaliação: "))
    nota_2 = float(input("Informa a nota da 2ª avaliação: "))

    media_aluno = ((nota_1 + nota_2) / 2)

    if media_aluno >= 6.0:
        print(f"O(a) aluno(a) {nomeAluno}, foi APROVADO(A) com a nota média final {media_aluno:.1f}.")

    else: 
        print(f"O(a) aluno(a) {nomeAluno}, foi REPROVADO(A) com a nota média final {media_aluno:.1f}")

    totalAvaliado += 1

print("\nTodos os alunos foram avaliados com sucesso!")    


    
