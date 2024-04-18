from ultralytics import YOLO 
model = YOLO('yolov8x')


# predict 1
# model.predict('input_videos/image.png',save=True)

# predict 2
# result=model.predict('input_videos/image.png',save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#   print(box)

# predict 3
# result=model.predict('input_videos/input_video.mp4',save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#   print(box)
  
# predict 4
# model = YOLO('models/yolo5_last.pt')
# result=model.predict('input_videos/input_video.mp4',conf=0.2,save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#   print(box)
  
  
# predict 5
# result = model.track('input_videos/input_video.mp4',conf=0.2, save=True)

