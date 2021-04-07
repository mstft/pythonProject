import numpy as np
from math import sqrt, pi, sin, cos, exp


def gabor_wavelet_design():
    depth = 5  # depth of pyramid, i.e. number of scales
    orientation_count = 8  # the number of distinct orientations
    base_scale = 64  # size in pixels of image to be filtered
    phase_count = 2  # number of distinct phases

    # theta changes from pi* (0 - 7) / 8
    # gamma changes as 1, 2, 4, 8, 16, 32
    # Create u * v gabor filters each being an m by n matrix

    # phase gabor_arrayZero & gabor_arrayPi
    gabor_array = np.zeros((phase_count, depth, orientation_count, base_scale, base_scale))

    # In  this  work,  Gabor  wavelets  are  generated  at  six  spatial frequencies, include 1, 2, 4, 8, 16, and 32
    # (unit: cycles per field of view). At each spatial frequency f ycles per field-of-view(FOV), wavelets are
    # positioned on anf×fgrid. At each grid position,  wavelets  occur  at  eight  equally  spaced  orientations
    # ranged from0◦to 157.5◦, and two orthogonal phases:0◦and 90◦. Preferred spatial frequency (1/λ) and size (σ)
    # are not completely independent:σ=aλ with between 0.3 and0.6 for most cells [29]. In the following, we used a
    # typical a value of 0.56 [4].

    gamma = 1
    lambdax = 41 / 3 * 2
    lambdas = [lambdax / sqrt(2 ** (i - 1)) for i in range(1, 6)]
    # % psi =..; = > 0 & 90
    sigmax = 20 / 3 * 2
    sigmas = [sigmax / sqrt(2 ** (i - 1)) for i in range(1, 6)]

    for i in range(1, depth + 1):
        lambda_each = lambdas[i - 1]
        sigma = sigmas[i - 1]
        for j in range(1, orientation_count + 1):
            teta = ((j - 1) / orientation_count) * pi
            gfilter_zero = np.zeros((base_scale, base_scale))
            gfilter_pi = np.zeros((base_scale, base_scale))
            for x in range(1, base_scale + 1):
                for y in range(1, base_scale + 1):
                    xprime = (x - (base_scale + 1) / 2) * cos(teta) + (y - (base_scale + 1) / 2) * sin(teta)
                    yprime = -(x - (base_scale + 1) / 2) * sin(teta) + (y - (base_scale + 1) / 2) * cos(teta)
                    gfilter_zero[x - 1, y - 1] = exp(
                        -(xprime ** 2 + gamma ** 2 * yprime ** 2) / (2 * (sigma ** 2))) * cos(
                        2 * pi * xprime / lambda_each)
                    gfilter_pi[x - 1, y - 1] = exp(
                        -(xprime ** 2 + gamma ** 2 * yprime ** 2) / (2 * (sigma ** 2))) * cos(
                        (2 * pi * xprime / lambda_each + pi / 2))
                gabor_array[0, i - 1, j - 1, :, :] = gfilter_zero
                gabor_array[1, i - 1, j - 1, :, :] = gfilter_pi


def about_gabor_wavelet_design():
    print("""
    
    # Code creating a (base_scale X base_scale) array, whose elements are m by n matrices;
    # each matrix being a 2 - D Gabor filter.
    # sigma = bandwidth, overall size, if increased we get more stripes;
    # theta = orientation, change the orientation of the filter;
    # lambda = wavelength, reducing it produce thinner stripes;
    # gamma = aspect ratio, the height of the function, very small = function all across the image, = 1
    # psi = phase psi can be define as the changing phase of the cos part of the filter. 

    # theta changes from pi* (0 - 7) / 8
    # gamma changes as 1, 2, 4, 8, 16, 32
    # Create u * v gabor filters each being an m by n matrix

    """)
