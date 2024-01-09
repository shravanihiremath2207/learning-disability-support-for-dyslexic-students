import speech_recognition as sr
import tkinter as tk
from nltk.corpus import cmudict
from Levenshtein import distance

# Load the CMU Pronouncing Dictionary
pron_dict = cmudict.dict()

# Create a Tkinter window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry("400x100")

# Create a label to display the recognized text and the pronunciation assessment
label = tk.Label(root, text="")
label.pack()

# Create a SpeechRecognizer instance
r = sr.Recognizer()

# Define the word to recognize
word_to_recognize = "hell"

def assess_pronunciation(word, user_audio_file):
    """
    Assess the user's pronunciation of a word using speech recognition and the Levenshtein distance.

    Args:
        word (str): The word to be pronounced.
        user_audio_file (str): The file path of the user's audio recording.

    Returns:
        float: The percentage of the correct pronunciation that the user got correct.
    """
    # Convert the correct pronunciation to a list of phonemes
    correct_pronunciation = pron_dict[word][0]
    print(correct_pronunciation)

    # Perform speech recognition on the user's audio input
    r = sr.Recognizer()
    with sr.AudioFile(user_audio_file) as source:
        audio = r.record(source)
    user_pronunciation = r.recognize_google(audio)

    # Calculate the Levenshtein distance between the user's pronunciation and the correct pronunciation
    
    user=user_pronunciation.split()[0]
    user_pro=pron_dict[user][0]
    print(user_pro)
    distance_score = distance(user_pro, correct_pronunciation)

    # Calculate the percentage of the correct pronunciation that the user got correct
    num_phonemes = len(correct_pronunciation)
    percent_correct = (num_phonemes - distance_score) / num_phonemes * 100

    return percent_correct


# Define a function to recognize speech, check for the specified word, and assess the pronunciation
def recognize_word():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Listen for the user's speech
        audio = r.listen(source)
        try:
            # Use Google's Speech Recognition API to transcribe the speech
            text = r.recognize_google(audio)
            # Display the recognized text in the label
            label.config(text=text)
            # Check if the recognized text contains the specified word
            if word_to_recognize in text.lower():
                label.config(text="Word recognized!")
                # Assess the user's pronunciation
                percent_correct = assess_pronunciation(word_to_recognize, "recorded.wav")
                label.config(text=f"You got {percent_correct:.2f}% of the pronunciation correct.")
            else:
                label.config(text="Word not recognized")
                percent_correct = assess_pronunciation(word_to_recognize, "recorded.wav")
                label.config(text=f"You got {percent_correct:.2f}% of the pronunciation correct.")
        except sr.UnknownValueError:
            # If the speech cannot be recognized, display an error message
            label.config(text="Speech not recognized")

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

# Create a button to initiate speech recognition and pronunciation assessment
button = tk.Button(root, text="Say \"Hello\"", command=recognize_word)
button.pack()

# Start the Tkinter event loop
root.mainloop()
