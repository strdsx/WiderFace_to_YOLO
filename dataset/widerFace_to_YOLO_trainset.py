import os
import cv2

def main():
    image_base_path = "./WIDER_train/images/"
    with open("./wider_face_split/wider_face_train_bbx_gt.txt", "r") as f:
        lines = f.readlines()

    image_count = 0
    face_cout = 0
    for i in lines:
        # One image
        if ".jpg" in i:
            img_path = i.split("\n")[0]
            
            # Read Image...
            img = cv2.imread(image_base_path + img_path)
            
            num_obj = lines[lines.index(i) + 1].split("\n")[0]
            face_cout += int(num_obj)
            
            bbox_line_start = lines.index(i) + 2
            bbox_line_end = bbox_line_start + int(num_obj)

            # Init relative bbox
            rel_bbox_list = []
            for j in range(bbox_line_start, bbox_line_end):
                bbox_list = lines[j].split("\n")[0]
                bbox_split = bbox_list.split(" ")

                # Absolute bbox
                x1 = int(bbox_split[0])
                y1 = int(bbox_split[1])
                w = int(bbox_split[2])
                h = int(bbox_split[3])

                # Relative bbox (YOLO Train)
                img_height = img.shape[0]
                img_width = img.shape[1]

                rel_cx = str(float((x1 + int(w/2)) / img_width))
                rel_cy = str(float((y1 + int(h/2)) / img_height))
                rel_w = str(float(w / img_width))
                rel_h = str(float(h / img_height))
                
                string_bbox = "0 " + rel_cx + " " + rel_cy + " " + rel_w + " " + rel_h
                rel_bbox_list.append(string_bbox)

                ## Visualization
                # cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0,0,255), 2)
                # print("x1, y1, W, H ==> ", x1, y1, w, h)
            # print(" ")

            # Save yolo train image ("wider_0.jpg, wider_1.jpg ...")
            save_path = "yolo_wider/"
            save_image_name = "wider_" + str(image_count)
            
            cv2.imwrite( save_path + save_image_name + ".jpg", img)
            with open(save_path + save_image_name + ".txt", "w") as f:
                for i in rel_bbox_list:
                    f.write(i + "\n")

            image_count += 1

            ## Visualization
            # cv2.imshow("test", img)
            # cv2.waitKey()
            # cv2.destroyAllWindows()

    # Total image, faces        
    print("Total Image : ", image_count)
    print("Total face : ", face_cout)
            

                
            
if __name__ == "__main__":
    main()
