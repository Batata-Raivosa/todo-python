def adicionar_tarefa(tarefas,nome_tarefa):
	tarefa ={"tarefa":nome_tarefa,"completada":False}
	tarefas.append(tarefa)
	print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
	
def ver_tarefas(tarefas):
	print("\nLista de tarefas")
	for indice, item in enumerate(tarefas, start=1): #começa a enumerar 1
		status = "✓" if item["completada"] else " "
		print(f"{indice}. [{status}] {item['tarefa']}")
		

tarefas = []