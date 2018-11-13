from django.db import models
from django.utils import timezone

LITERATURA = 'LI'
TECNOLOGIA_INFORMACAO = 'TI'
FILOSOFIA = 'FI'
HISTORIA = 'HI'
ELETRONICA = 'EL'
PORTUGUES = 'PT'
DIREITO = 'DI'
ADMINISTRACAO = 'AD'
MATEMATICA = 'MT'
EDUCACAO = 'ED'
INFORMATICA_BASICA = 'IB'
NAO_CLASSIFICADO = 'NC'
COMUNICACAO = 'CO'
ARTE = 'AR'
POLITICA = 'PO'
MEDICINA = 'ME'
CONTABILIDADE = 'CN'
METODOLOGIA = 'MO'
MARKETING = 'MK'
PLANEJAMENTO = 'PN'
BIOLOGIA = 'BI'
FISICA = 'FI'
NEGOCIACAO = 'NE'
PSICOLOGIA = 'PS'
QUIMICA = 'QI'

Categorias = (
	(LITERATURA, 'Literatura'),
	(TECNOLOGIA_INFORMACAO, 'Tecnologia da Informação'),
	(FILOSOFIA, 'Filosofia'),
	(HISTORIA, 'História'),
	(ELETRONICA, 'Eletrônica'),
	(PORTUGUES, 'Português'),
	(DIREITO, 'Direito'),
	(ADMINISTRACAO, 'Administração'),
	(MATEMATICA, 'Matemática'),
	(EDUCACAO, 'Educação'),
	(INFORMATICA_BASICA, 'Informática Básica'),
	(NAO_CLASSIFICADO, 'Não Classificado'),
	(COMUNICACAO, 'Comunicação'),
	(ARTE, 'Arte'),
	(POLITICA, 'Política'),
	(MEDICINA, 'Medicina'),
	(CONTABILIDADE, 'Contabilidade'),
	(METODOLOGIA, 'Metodologia'),
	(MARKETING, 'Marketing'),
	(PLANEJAMENTO, 'Planejamento'),
	(BIOLOGIA, 'Biologia'),
	(FISICA, 'Física'),
	(NEGOCIACAO, 'Negociação'),
	(PSICOLOGIA, 'Psicologia'),
	(QUIMICA, 'Química'),
	)

class Livros(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	titulo = models.CharField(max_length = 200)
	autor = models.CharField(max_length = 100)
	codigo = models.IntegerField()
	editora = models.CharField(max_length = 200)
	quantidade = models.IntegerField()
	valor = models.DecimalField(max_digits = 5, decimal_places = 2)
	foto = models.ImageField()
	categoria = models.CharField(max_length = 2, choices = Categorias, default = NAO_CLASSIFICADO)
	data_criacao = models.DateTimeField(default = timezone.now)

	def adicionado(self):
		self.data_criacao = timezone.now()
		self.save()

	def __str__(self):
		return '%s - %s - %s' % (self.data_criacao, self.codigo, self.titulo)

	def __unicode__(self):
		return '%s - %s - %s' % (self.data_criacao, self.codigo, self.titulo)		