"""SobelGradientInterp

Advantages: very precise
Disadvantages: slow, poor performance on images with lots of objects

Method: Compute the edges of the image with laplacian, then blur the computed mask.
        Then, detect the larges area (empty space) in the mask and use that as the
        background. Finally, use the background to interpolate the gradient of the
        image."""


import cv2

from step_abc import ProcessStep

class SobelGradientInterp(ProcessStep):
    