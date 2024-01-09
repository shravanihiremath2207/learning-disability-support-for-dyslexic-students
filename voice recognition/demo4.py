import speech_recognition as sr
import tkinter as tk
from nltk.corpus import cmudict
from Levenshtein import distance

# Create a Tkinter window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry("400x100")

# Create a label to display the recognized text
label = tk.Label(root, text="")
label.pack()

# Create a SpeechRecognizer instance
r = sr.Recognizer()

# Define the word to recognize
word_to_recognize = "hello"

# Define a function to recognize speech and check for the specified word
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
            else:
                label.config(text="Word not recognized")
        except sr.UnknownValueError:
            # If the speech cannot be recognized, display an error message
            label.config(text="Speech not recognized")

    with open("recorded1.wav", "wb") as f:
        f.write(audio.get_wav_data())


 



# Create a button to initiate speech recognition
button = tk.Button(root, text="Say \"Hello\"", command=recognize_word)
button.pack()


# Start the Tkinter event loop
root.mainloop()
