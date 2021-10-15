#!/bin/bash

# ============================================================
#
# RESIZE IMAGES
#
# ============================================================

# DELETE TXT FILE
name_img=./name_img.txt
if [ -f "$name_img" ]; then
    rm ./name_img.txt
fi

# RESIZE IMAGES
python3 resize_down.py
echo 

# ============================================================
#
# TO GET ATTENTION MAPS
#
# ============================================================

for image in `ls ./testing_real/input_img/`
do
	python3 model1/test_model.py --weights_path model1/derain_gan/derain_gan.ckpt-100000 --image_path ./testing_real/input_img/$image
done


# ============================================================
#
# CHANGE PATH AND DELETE FILES
#
# ============================================================

# FIND ALL IMAGES
cd ~/Desktop/model2/

echo

# DELETE TXT FILE
out_name_img=./out_name_img.txt
if [ -f "$out_name_img" ]; then
    rm ./out_name_img.txt
fi

# DETELE RESULTS FOLDER
rest_folder=./testing_result/
if [ -d "$rest_folder" ]; then
    rm -r testing_result
fi

# ============================================================
#
# PREDICTIONS
#
# ============================================================

# NETWORK
python3 run_model.py --phase test --restore_step 258000  --inputdata_path ./testing_real/input_img --output_path ./testing_result/output_test/
		
echo

# ============================================================
#
# RESIZE IMAGES
#
# ============================================================

# RESIZE IMAGES
python3 resize_up.py
echo




