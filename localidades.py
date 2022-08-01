from estados import Estados
from cidades import Cidade

serra = Cidade("Serra", 527240)
vitoria = Cidade("Vitória", 365855)
cariacica = Cidade("Cariacica", 386495)

espirito_santo = Estados("ES", "Espírito Santo")
espirito_santo.adiciona_cidade(serra)
espirito_santo.adiciona_cidade(vitoria)
espirito_santo.adiciona_cidade(cariacica)

petropolis = Cidade("Petropolis", 306678)
copacabana = Cidade("Copacabana", 298843)

rio_de_janeiro = Estados("RJ", "Rio de Janeiro")
rio_de_janeiro.adiciona_cidade(petropolis)
rio_de_janeiro.adiciona_cidade(copacabana)

espirito_santo.exibe_cidades()