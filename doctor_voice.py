import os
from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Abhishek!"
# #text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY="sk_70c2e75067e9aa9de63f363eea70a22c7c206b668933f9e4"

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice

import subprocess
import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Abhishek, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    try:
        # Generate speech
        audioobj = gTTS(text=input_text, lang=language, slow=False)
        audioobj.save(output_filepath)
        print(f"Audio saved to {output_filepath}")
    except Exception as e:
        print(f"Error generating speech: {e}")
        return

    try:
        # Easiest and most reliable on Windows
        os.startfile(output_filepath)
    except Exception as e:
        print(f"Error playing audio: {e}")

# Example usage
input_text = "This is AI with Abhishek, testing autoplay using gTTS on Windows!"
#text_to_speech_with_gtts(input_text, "gtts_testing_autoplay.mp3")



from elevenlabs import ElevenLabs, save
import os
import platform
import subprocess

ELEVENLABS_API_KEY = ""  # Replace with your actual API key

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Generate audio from ElevenLabs
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Save MP3 output
    save(audio, output_filepath)
    print(f"Audio saved to {output_filepath}")

    # Play using default audio player (works on Windows)
    try:
        if platform.system() == "Windows":
            os.startfile(output_filepath)
        elif platform.system() == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif platform.system() == "Linux":
            subprocess.run(['mpg123', output_filepath])  # or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Example usage
text_to_speech_with_elevenlabs("Hello, this is ElevenLabs speaking on Windows!", "elevenlabs_testing_autoplay.mp3")



# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")