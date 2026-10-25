import unittest
import aluno as a
import turma as t


class turmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')

        self.alunos = []

        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', -1))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 7))

        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(
            10,
            self.turmaObject.maiorNota.nota,
            'Erro ao encontrar maior nota'
        )

    def testMenor(self):
        self.assertEqual(
            7,
            self.turmaObject.menorNota.nota,
            'Erro ao encontrar menor nota'
        )

    def testIntervalo(self):
        print('Testar se o intervalo de notas está correto.')

        for aluno in self.turmaObject.turma:
            self.assertGreaterEqual(
                aluno.nota, 0,
                'Existe aluno com nota menor que 0'
            )
            self.assertLessEqual(
                aluno.nota, 10,
                'Existe aluno com nota maior que 10'
            )

    def testAlunoNotaNegativa(self):
        nomes = [aluno.nome for aluno in self.turmaObject.turma]

        self.assertNotIn(
            'Melissa',
            nomes,
            'Aluno com nota negativa não deveria ser cadastrado'
        )

    def testQuantidadeAlunos(self):
        self.assertEqual(
            3,
            len(self.turmaObject.turma),
            'A quantidade de alunos cadastrados está incorreta'
        )


if __name__ == "__main__":
    unittest.main()
