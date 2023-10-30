from ultralytics import YOLO

class ModelProvider:
  model = YOLO('polls/assets/best.pt')

def getModel(self):
    return self.model