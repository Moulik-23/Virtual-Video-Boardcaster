import cv2
from ultralytics import YOLO
import numpy as np
import torch

class CustomerSegmentationWithYolo():
    def __init__(self,erode_size=5,erode_intensity=2):
        self.model = YOLO("yolov8s-seg.pt")
        self.erode_size = erode_size
        self.erode_intensity = erode_intensity
        self.background_image = cv2.imread("./static/wallpaperflare.com_wallpaper.jpg")

    def generate_mask_from_result(self,results):
        for result in results:
            if result.masks:
                # get array results
                masks = result.masks.data
                boxes = result.boxes.data

                # extract classes
                clss = boxes[:, 5]

                # get indices of results where class is 0 (people in COCO)
                people_indices = torch.where(clss == 0)

                # use these indices to extract the relevant masks
                people_masks = masks[people_indices]

                if len(people_masks) == 0:
                    return None
                
                # scale for visualizing results
                people_masks = torch.any(people_masks, dim=0).to(torch.uint8) * 255

                kernel = np.ones((self.erode_size, self.erode_size), np.uint8)
                eroded_mask = cv2.erode(people_masks.cpu().numpy(), kernel, iterations=self.erode_intensity)

                return people_masks
            else:
                return None
            
    def apply_blur_with_mask(self,frame, mask, blur_strength=21):
        blur_strength=(blur_strength, blur_strength)
        blurred_frame = cv2.GaussianBlur(frame, blur_strength, 0)

        mask = (mask.cpu().numpy() > 0).astype(np.uint8)


        mask_3d = cv2.merge([mask, mask, mask])

        result_frame = np.where(mask_3d == 1, frame, blurred_frame)

        return result_frame
    
    def apply_black_bakground(self, frame, mask):
        black_bakground = np.zeros_like(frame)
        result_frame = np.where(mask[:, :, np.newaxis] == 255, frame, black_bakground)
        return result_frame
    
    def apply_custom_bakground(self, frame, mask):
        background_image = cv2.resize(self.background_image, (frame.shape[1], frame.shape[0]))

        result_frame = np.where(mask[:, :, np.newaxis] == 255, frame, background_image)
        return result_frame