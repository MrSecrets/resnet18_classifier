import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import csv


class ResnetClassifier(object):
    def __init__(self,device=None):
    
        if device is None:
            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

        self.classes = []
        self.transform = transforms.Compose(
                    [
                        transforms.Resize(224),
                        transforms.CenterCrop(224),
                        transforms.ToTensor(),
                        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
                    ])
        
        with open('resnet/model/imagenet1000_clsidx_to_labels.csv') as f:
            csv_reader = csv.reader(f,delimiter=':')
            for row in csv_reader:
                self.classes.append(row[1])

        self.resnet18 = models.resnet18(pretrained=False, progress=True)
        self.resnet18.load_state_dict(torch.load('resnet/model/weights.pth'))
        self.resnet18.eval()



    def predict(self,im):
        img = self.transform(im).float()
        img = img.unsqueeze_(0)
        output = self.resnet18(img)
        prob = torch.nn.functional.softmax(output, dim=1)[0] * 100
        _, indices = torch.sort(output, descending=True)
        
        result = [self.classes[idx] for idx in indices[0][:5]]


        return f"The image appears to be {str(result[0])}"

