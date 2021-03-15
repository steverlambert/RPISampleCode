print("Testing all package imports....")

import cv2
import pytesseract
import numpy as np
import tensorflow as tf
import tflite_runtime.interpreter as tflite
from PIL import Image
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import RPi.GPIO as GPIO
import time
import scipy as sp
import scipy.ndimage
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

print("Success!")
