from relatedData import *
from gaborDesign import *

# IMPORTANT NOTES:
# Conversion voxel info from 1D to 3D transform(voxelNumber) to (x+64*y+64^2*z)

# TODO: 1. Design Gabor Wavelet Pyramid
# TODO: 2. Genetic Algorithm Design

while True:
    startStep = int(input("""
                        You are @ the Main Menu of the Program
                            Enter 
                            1 to Run removeUnrelatedPart Function
                            2 to Run gabor_wavelet_design Function
                            9 to Get InformationAbout Function
                            0 to EXIT
                            : 
                            """))

    # COMPILE PART
    if startStep == 1:
        data_trn_s1, data_val_s1, mt = remove_unrelated_data()  # Eliminate Unrelated Voxels' Data
        print(data_trn_s1.shape, data_val_s1.shape, mt.shape)
    elif startStep == 2:
        gabor_wavelet_design()
    # GET INFORMATION ABOUT FUNCTIONS
    elif startStep == 9:
        secondStep = int(input("""You are @ the Information About Functions Part
                                    Enter 
                                    1 to Get Information About removeUnrelated Function 
                                    2 to Get Information About gabor_wavelet_design Function
                                    0 to EXIT
                                    :s
                                    """))
        if secondStep == 1:
            about_remove_unrelated_data()
        elif secondStep == 2:
            about_gabor_wavelet_design()
        elif secondStep == 0:
            break
        else:
            EOFError("wrong input")
    # HALT THE PROGRAM PART
    elif startStep == 0:
        break
    else:
        EOFError("wrong input")


#  UPLOAD GABOR WAVELET PYRAMID PART OF THE CODE IS:
#  APPLY GABOR WAVELET PYRAMID TO 1750 TRAINING IMAGE AND 120 VALIDATING IMAGE
#  AND SAVES TO .MAT FILES TO BE USED IN SECOND PART
#  TRAINING.MAT => 1750*2728  && VALIDATING.MAT => 120*2728
