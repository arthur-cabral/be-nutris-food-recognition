import shutil
import os
from django.http import JsonResponse, HttpResponseBadRequest
from .ia.modelProvider import ModelProvider
from PIL import Image
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

names = {
    0: 'Arroz',
    1: 'Carne',
    2: 'Feijao',
    3: 'Frango',
    4: 'Ovo',
    5: 'Salada'
}

df_taco = pd.read_csv('polls/assets/TACO_mini.csv', sep=';')

@csrf_exempt
def index(request):
    if request.method == 'POST':
      try:
        img_raw = request.FILES['image'] if 'image' in request.FILES else None
        validar_imagem(img_raw)
        img = Image.open(img_raw)

        ModelProvider.model.predict(conf=0.5, source=img, save_txt=True, project='./runs/detect/')
        response = retorna_macro()
        shutil.rmtree('runs')
        return JsonResponse({'lista_de_alimentos': response})
      except Exception as e:
        return HttpResponseBadRequest(e)


def retorna_macro():
  if os.path.exists('runs/detect/predict/labels.txt') == False:
    raise Exception('Erro ao criar a pasta de runs')
  df_resultado_imagem = pd.read_csv('runs/detect/predict/labels.txt', sep=' ', header = None)
  df_resultado_imagem.rename(columns={0:'id_alimento'},inplace=True)
  df_resultado_imagem['contagem'] = 1
  df_resultado_imagem = df_resultado_imagem.groupby('id_alimento').agg({'contagem':'sum'}).reset_index()
  df_resultado_imagem_taco = df_resultado_imagem.merge(df_taco, how='left', on='id_alimento')

  resultados = []
  for index, row in df_resultado_imagem_taco.iterrows():
    resultados.append({'nome_alimento': row.nome_alimento, 'calorias': row.calorias, 'gordura': row.gordura, 'proteina': row.proteina, 'carboidrato': row.carboidrato, 'contagem': row.contagem})
  return resultados

def validar_imagem(img_raw):
  if img_raw == None:
    raise Exception('Imagem não inserida')
  if img_raw.name.split('.')[-1] not in ['jpg', 'jpeg', 'png']:
    raise Exception('Formato de imagem inválido')
