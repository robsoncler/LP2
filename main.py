from disciplina import Disciplina
from professor import Professor
from aluno import Aluno

prof1 = Professor(nome='Alberto', ra= '14014')
prof2 = Professor(nome='Esteves', ra= '15697')
prof3 = Professor(nome='Fabiola', ra= '23589')
prof4 = Professor(nome='Mariana', ra= '97853')
prof5 = Professor(nome='Carlos',  ra= '74689')


disc1 = Disciplina (nome='Redes de Computadores', cargaHoraria = 40, mensalidade = 100, professor = prof4)
disc1 = Disciplina (nome='Web Designer', cargaHoraria = 120, mensalidade = 350, professor = prof1)
disc1 = Disciplina (nome='Arquitetura de Computadores', cargaHoraria = 80, mensalidade = 195 , professor = prof5)
disc1 = Disciplina (nome='Lógica de Programação', cargaHoraria = 80, mensalidade = 250, professor = prof2)
disc1 = Disciplina (nome='Internet of Things - IoT', cargaHoraria = 40, mensalidade = 150, professor = prof3)


a_1 = Aluno ('Mateus', 'mateus.souza@gmail.com','54697', '993785624',0)
a_2 = Aluno ('Fabiana', 'fabiana12@gmail.com','68935', '924893674',0)
a_3 = Aluno ('Cleide', 'cleidinha@gmail.com','85329', '999872478',0)

a_1.aumentaDesconto(20)
print ('Aumento o desconto de Mateus para: ', a_1.getDesconto())

a_1.diminuiDesconto(10)
print ('Diminuiu o desconto de Mateus para: ', a_1.getDesconto())

a_2.aumentaDesconto(40)
print ('Aumento no desconto de Fabiana: ', a_2.getDesconto())

a_3.aumentaDesconto(15)
print ('Aumento no desconto de Cleide: ', a_3.getDesconto())