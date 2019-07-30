# Wider Face Trainset --> YOLO Trainset

## Download
- Wider Face dataset : https://pytorch.org/

## Description
- Wider Face Trainset의 ground-truth는 <code>dataset/wider_face_split/wider_face_train_bbx_gt.txt</code> 에서 확인 가능.
- wider_face_train_bbx_gt.txt
    ```
    0--Parade/0_Parade_marchingband_1_117.jpg   => [image path]
    9   => [number of face]
    69 359 50 36 1 0 0 0 0 1    => [x1, y1, width, height, ...]
    227 382 56 43 1 0 1 0 0 1 
    296 305 44 26 1 0 0 0 0 1 
    353 280 40 36 2 0 0 0 2 1 
    885 377 63 41 1 0 0 0 0 1 
    819 391 34 43 2 0 0 0 1 0 
    727 342 37 31 2 0 0 0 0 1 
    598 246 33 29 2 0 0 0 0 1 
    740 308 45 33 1 0 0 0 2 1
    ```

- Wider Face Trainset은 **12,880 image(159,420 face box)** 로 구성됨
- YOLO Trainset으로 변경하기 위해 wider face의 절대 좌표를 상대 좌표로 변경 
- YOLO Trainset
    ```
    wider_0.jpg, wider_0.txt, wider_1.jpg, wider_1.jpg...
    ```
    - **.txt** 파일은 해당 이미지의 <code> [object_index, relative_center_x, relative_center_y, relative_width, relative_height]</code>로 구성됨
- 해당 코드 -> <code> dataset/widerFace_to_YOLO_trainset.py</code> 