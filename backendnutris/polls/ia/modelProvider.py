from ultralytics import YOLO

class ModelProvider:
  model = YOLO('polls/ia/best.pt')

def getModel(self):
    return self.model