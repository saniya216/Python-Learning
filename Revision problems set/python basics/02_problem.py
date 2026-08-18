#02 install an external module and perform operation using your intrest .

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Heyy Sania , Good morning. Welcome to the python programming with me voice assistant ai tool ")
engine.runAndWait()