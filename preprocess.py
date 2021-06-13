import os
from shutil import copyfile
from nipype.interfaces.ants import N4BiasFieldCorrection
import logging
logging.basicConfig(filename='preprocess.log', filemode='w', format='[%(levelname)s] %(lineno)d :%(message)s', level=logging.DEBUG)

#Bias correction of MRI data
def correct_bias_field(input_file, output_file):
    print("Start")
    correct = N4BiasFieldCorrection()
    correct.save_bias = False
    correct.inputs.num_threads = 8
    #correct.inputs.bspline_order = 5
    correct.inputs.dimension = 3
    correct.inputs.bspline_fitting_distance = 300
    correct.inputs.shrink_factor = 3
    correct.inputs.input_image = input_file
    correct.inputs.output_image = output_file
    res = correct.run()
    print("Done")

BASE_DIR = '/kaggle''
DATA_PATH = os.path.join(BASE_DIR, 'input', 'mri-brain-dataset', 'NFBS_Dataset')
OUTPUT_DIR = os.path.join(BASE_DIR, 'input', 'mri-brain-dataset', 'NFBS_MRI_SKULL') 

list_dirs = os.listdir(DATA_PATH)

for dir in list_dirs:
    d_path = os.path.join(DATA_PATH, dir)
    if not os.path.isdir(d_path):
        continue

    files = os.listdir(d_path)
    output_d_path = os.path.join(OUTPUT_DIR, dir)
    if not os.path.exists(output_d_path):
        os.mkdir(output_d_path)

    logging.debug('-----%s' %dir)
    print(dir)
    for file in files:
        file_path = os.path.join(d_path, file)
        input_file = file_path
        output_file = os.path.join(OUTPUT_DIR, dir, file)
        if file.find('brain') == -1:
            correct_bias_field(input_file, output_file)
            logging.debug('Bias Corrected. Output: %s' %(output_file))
        else:
            copyfile(input_file, output_file)
            logging.debug('File has been copied. Output: %s' %(output_file))

