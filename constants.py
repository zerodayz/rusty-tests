import os
import platform

# Core directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project directories
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
DRIVER_DIR = os.path.join(BASE_DIR, 'drivers')

# System
PLATFORM = platform.system()
PROCESSOR = platform.processor()