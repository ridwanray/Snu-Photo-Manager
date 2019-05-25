import kivy
from kivy.utils import platform
from collections import OrderedDict
try:
    import numpy
    import cv2
    opencv = True
except:
    opencv = False

if platform in ['win', 'linux', 'macosx', 'unknown']:
    desktop = True
else:
    desktop = False

kivy_version = kivy.__version__.split('.')
kivy_version_primary = int(kivy_version[0])
kivy_version_secondary = int(kivy_version[1])

scale_size_to_options = OrderedDict([('long', 'Long Side'), ('short', 'Short Side'), ('height', 'Height'), ('width', 'Width')])
naming_method_default = '%Y-%M-%D< - %T>'
avoidfolders = ['.picasaoriginals', '.thumbnails', '.originals']
imagetypes = ['.jpg', '.png', '.jpeg', '.bmp', '.gif', '.pcx']
movietypes = ['.avi', '.mov', '.mp4', '.mpeg4', '.mts', '.mpg', '.mpeg', '.vob']
negative_kelvin = [(255, 115, 0), (255, 124, 0), (255, 121, 0), (255, 130, 0), (255, 126, 0), (255, 135, 0), (255, 131, 0), (255, 141, 11), (255, 137, 18), (255, 146, 29), (255, 142, 33), (255, 152, 41), (255, 147, 44), (255, 157, 51), (255, 152, 54), (255, 162, 60), (255, 157, 63), (255, 166, 69), (255, 161, 72), (255, 170, 77), (255, 165, 79), (255, 174, 84), (255, 169, 87), (255, 178, 91), (255, 173, 94), (255, 182, 98), (255, 177, 101), (255, 185, 105), (255, 180, 107), (255, 189, 111), (255, 184, 114), (255, 192, 118), (255, 187, 120), (255, 195, 124), (255, 190, 126), (255, 198, 130), (255, 193, 132), (255, 201, 135), (255, 196, 137), (255, 203, 141), (255, 199, 143), (255, 206, 146), (255, 201, 148), (255, 208, 151), (255, 204, 153), (255, 211, 156), (255, 206, 159), (255, 213, 161), (255, 209, 163), (255, 215, 166), (255, 211, 168), (255, 217, 171), (255, 213, 173), (255, 219, 175), (255, 215, 177), (255, 221, 180), (255, 217, 182), (255, 223, 184), (255, 219, 186), (255, 225, 188), (255, 221, 190), (255, 226, 192), (255, 223, 194), (255, 228, 196), (255, 225, 198), (255, 229, 200), (255, 227, 202), (255, 231, 204), (255, 228, 206), (255, 232, 208), (255, 230, 210), (255, 234, 211), (255, 232, 213), (255, 235, 215), (255, 233, 217), (255, 237, 218), (255, 235, 220), (255, 238, 222), (255, 236, 224), (255, 239, 225), (255, 238, 227), (255, 240, 228), (255, 239, 230), (255, 241, 231), (255, 240, 233), (255, 243, 234), (255, 242, 236), (255, 244, 237), (255, 243, 239), (255, 245, 240), (255, 244, 242), (255, 246, 243), (255, 245, 245), (255, 247, 245), (255, 246, 248), (255, 248, 248), (255, 248, 251), (255, 249, 251), (255, 249, 253), (255, 249, 253)]
positive_kelvin = [(254, 249, 255), (254, 250, 255), (252, 247, 255), (252, 248, 255), (249, 246, 255), (250, 247, 255), (247, 245, 255), (247, 245, 255), (245, 243, 255), (245, 244, 255), (243, 242, 255), (243, 243, 255), (240, 241, 255), (241, 241, 255), (239, 240, 255), (239, 240, 255), (237, 239, 255), (238, 239, 255), (235, 238, 255), (236, 238, 255), (233, 237, 255), (234, 237, 255), (231, 236, 255), (233, 236, 255), (230, 235, 255), (231, 234, 255), (228, 234, 255), (229, 233, 255), (227, 233, 255), (228, 233, 255), (225, 232, 255), (227, 232, 255), (224, 231, 255), (225, 231, 255), (222, 230, 255), (224, 230, 255), (221, 230, 255), (223, 229, 255), (220, 229, 255), (221, 228, 255), (218, 228, 255), (220, 227, 255), (217, 227, 255), (219, 226, 255), (216, 227, 255), (218, 226, 255), (215, 226, 255), (217, 225, 255), (214, 225, 255), (216, 224, 255), (212, 225, 255), (215, 223, 255), (211, 224, 255), (214, 223, 255), (210, 223, 255), (213, 222, 255), (209, 223, 255), (212, 221, 255), (208, 222, 255), (211, 221, 255), (207, 221, 255), (210, 220, 255), (207, 221, 255), (209, 220, 255), (206, 220, 255), (208, 219, 255), (205, 220, 255), (207, 218, 255), (204, 219, 255), (207, 218, 255), (203, 219, 255), (206, 217, 255), (202, 218, 255), (205, 217, 255), (201, 218, 255), (204, 216, 255), (201, 217, 255), (204, 216, 255), (200, 217, 255), (203, 215, 255), (199, 216, 255), (202, 215, 255), (199, 216, 255), (202, 214, 255), (198, 216, 255), (201, 214, 255), (197, 215, 255), (200, 213, 255), (196, 215, 255), (200, 213, 255), (196, 214, 255), (199, 212, 255), (195, 214, 255), (198, 212, 255), (195, 214, 255), (198, 212, 255), (194, 213, 255), (197, 211, 255), (193, 213, 255), (197, 211, 255)]

containers = ['mp4', 'matroska', 'mov', 'ogg', 'avi']
containers_friendly = ['MP4', 'Matroska', 'Quicktime', 'Ogg', 'AVI']
containers_extensions = ['mp4', 'mkv', 'mov', 'ogv', 'avi']
video_codecs = ['libx264', 'mpeg4', 'mpeg2video', 'libtheora']
video_codecs_friendly = ['H.264', 'MPEG 4', 'MPEG 2', 'Ogg Theora']
audio_codecs = ['aac', 'ac3', 'libmp3lame', 'flac', 'libvorbis']
audio_codecs_friendly = ['AAC', 'AC-3', 'MP3', 'FLAC', 'Ogg Vorbis']
interface_multiplier = 22
drag_delay = .5
