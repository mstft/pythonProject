import numpy as np
import tables
import scipy.io as sio

# TODO: remove voxels with low SNR


def remove_unrelated_data():
    print("-------------inside removeUnrelated-------------")
    # THIS PIECE of CODE ELIMINATE UNRELATED VOXELS & DATA

    # NOTE: This file is not loaded to github
    f = tables.open_file('/home/mt/Desktop/vim-1/EstimatedResponses.mat')

    # / Inside EstimatedResponses.mat file we have: dataTrnS*, dataValS*, roiS*, voxIdxS*

    # roiS* contains voxels' visual area info [0 ... 3] => changes between 0-7
    # no of voxels in each area (others= 17127,V1=1331,V2=2208,V3=1973,V3A=484,V3B=314,V4=1550,LatOcc=928)
    # / roi_s1(CArray(1, 25915), zlib(3))
    # / roiS2(CArray(1, 26329), zlib(3))
    roi_s1 = f.get_node('/roi_s1')[:][0]

    # roi_s1 [[  0   0   0 ... 3 3 3]]  => (CArray(1, 25915), zlib(3)) Values between 0 - 7 => shows region of the voxel
    # vox_idx_s1 [  657.   715.   716. ... 71591. 71592. 71593.] => (1, 25915) - 1D position of voxel in the brain
    # / vox_idx_s1(CArray(1, 25915), zlib(3))
    # / voxIdxS2(CArray(1, 26329), zlib(3))
    vox_idx_s1 = f.get_node('/vox_idx_s1')[:].flatten()
    # print("length of vox_idx_s1 {}".format(len(vox_idx_s1)))
    print("vox_idx_s1 {}".format(vox_idx_s1))

    # numpy nonzero returns the indices of the elements that are non-zero.
    # print("roi_s1 starts\n {}\n roi_s1 ends".format(roi_s1))
    v1_idx = np.nonzero(roi_s1 == 1)[0]  # number of V1 VOXELS in S1
    v2_idx = np.nonzero(roi_s1 == 2)[0]  # number of V2 VOXELS in S1
    v3_idx = np.nonzero(roi_s1 == 3)[0]  # number of V3 VOXELS in S1
    # all V1, V2 and V3 voxel positions are combined by converting to normal array and adding and sorting

    # vr_all is the position of the voxels in visual area V1, V2 or V3
    vr_all = np.array(sorted(list(v1_idx)+list(v2_idx)+list(v3_idx)))
    # dataTrn value of region given above roi_s1 == X for X is 1 or 2 or 3
    # print("vr_all {}".format(vr_all.shape))
    # print(vr_all)

    # / BOLD responses for each image used in training session
    # / data_trn_s1(CArray(1750, 25915), zlib(3))
    # / dataTrnS2(CArray(1750, 26329), zlib(3)) => not used
    data_trn_s1 = f.get_node('/data_trn_s1')[:]
    # print("dimeonsions of data_trn_s1 {}".format(data_trn_s1))
    # get the training values of the voxels which are in V1, V2, V3 areas
    # Sizes of training array decrease from 1750*25915 => 1750*5512
    data_trn_s1 = data_trn_s1[:, vr_all]  # training data of voxels in V1, V2, V3 areas

    # / BOLD responses for each image used in validating session
    # / data_val_s1(CArray(120, 25915), zlib(3))
    # / dataValS2(CArray(120, 26329), zlib(3))
    data_val_s1 = f.get_node('/data_val_s1')[:]
    print("dimeonsions of data_val_s1 {}".format(data_val_s1.shape))
    # get the validation values of the voxels which are in V1, V2, V3 areas
    # Sizes of training array decrease from 120*25915 => 120*5512
    data_val_s1 = data_val_s1[:, vr_all]

    mt = np.copy(roi_s1)
    new_column = np.arange(mt.shape[0])
    mt = np.vstack((mt, new_column)).T
    mt = mt[vr_all, :]

    # values in the V1, V2 and V3 (only 5512 voxel)

    print("-------------exits removeUnrelated-------------")

    sio.savemat('removeUnrelatedDataOuput', {"data_trn_s1": data_trn_s1, "data_val_s1": data_val_s1, "mt": mt},
                appendmat=True)

    return data_trn_s1, data_val_s1, mt

    # This Program returns
    #       data_trn_s1: Containing V1, V2, V3 area voxels respond to 1750 training images  => (1750, 5512)
    #       data_val_s1: Containing V1, V2, V3 area voxels respond to 120 validating images => ( 120, 5512)
    #          mt    : Containing [region type, voxel number]                             => (5512,    2)


def about_remove_unrelated_data():
    print("""
    Input almayan fonksiyon içerisinde DATALAD'a yüklenilen EstimatedResponse.mat dosyası 
    okunmaktadır. 
    This code is extracting subject S1's related data which will be used in study.
    V1, V2 and V3 areas and related voxels of the Subject S1's visual cortex's are determined
    by using roi_s1 and vox_idx_s1 parameters.    
    
    Outputs:
            data_trn_s1(1750, 5512): List of V1, V2, V3 areas' voxels' reaction to 1.750 different natural 
                                   images in training sessions. 
            data_val_s1( 120, 5512): List of V1, V2, V3 areas' voxels' reaction to 120 different natural 
                                   images in validation sessions. 
            mt           (5512,2): Shows voxels in V1, V2, V3 areas, and their numbers [region type, voxel number]
    Finally the data is saved as "removeUnrelatedDataOuput" in same folder. 
    """)
