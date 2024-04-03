import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import pydicom
import SimpleITK as sitk

def convert_to_nifti(folder_dicom_dir, nifti_dir):
    """
    convert a folder containing dicom files into a single nifti
    :param folder_dicom_dir: folder containing the dicom slides
    :param nifti_dir: file dir of the output nifti
    """
    reader = sitk.ImageSeriesReader()  # Initializes an ImageSeriesReader object from SimpleITK.
    dicom_names = reader.GetGDCMSeriesFileNames(folder_dicom_dir)  # Retrieves the file names of the DICOM series to be read.
    reader.SetFileNames(dicom_names)  # Sets the file names for the reader to process.
    image = reader.Execute()  # Executes the reading process and stores the resulting image in the `image` variable.
    sitk.WriteImage(image, nifti_dir)  # Writes the image data to a NIfTI file at the specified location.


