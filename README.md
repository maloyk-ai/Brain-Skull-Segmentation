# Brain-Skull-Segmentation(Skull Stripping using UNet)
One of the most common MRI (Magnetic Resonance Imaging) use is a brain visualisation. Brain anatomy is highly complicated therefore it might be difficult to extract only these structures which have diagnostic value. In a consequence it is so necessary to develop and apply most efficient brain’s segmentation algorithms. One of the first steps in case of neurological MRI analysis is skull stripping. It involves removing extra-meningeal tissue from the head image, therefore it is essential to find the best method to determine the brain and skull boundaries.

Proposed implementation of Skull Stripping is based on Deep Neural Network(UNet) and shjows decent accuracy. The accuracy and obcetive loss can be further improved by using different architectures of UNets. 

Dataset: NFBS Skull-Stripped Repository (http://preprocessed-connectomes-project.org/NFB_skullstripped/)
"The Neurofeedback Skull-stripped (NFBS) repository is a database of 125 T1-weighted anatomical MRI scans that are manually skull-stripped. In addition to aiding in the processing and analysis of the NFB dataset, NFBS provides researchers with gold standard training and testing data for developing machine learning algorithms. "

Prediction using 2D Convolution based UNet

<img width="872" alt="Brain-Segmentation Prediction" src="https://user-images.githubusercontent.com/84564226/119955285-8bcb1b00-bfbd-11eb-8c46-7818984a9707.png">

Prediction using 3D Convolution based UNet

<img width="1235" alt="Screenshot 2021-06-03 at 6 08 01 PM" src="https://user-images.githubusercontent.com/84564226/120658137-cb54a400-c4a2-11eb-9dac-1d69cbc19267.png">




