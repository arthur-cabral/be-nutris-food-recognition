from ultralytics import YOLO

class ModelProvider:
  model = YOLO('C:/Users/TUCO/Desktop/BackendDjangoNutris/backendnutris/polls/ia/best.pt')

def getModel(self):
    return self.model