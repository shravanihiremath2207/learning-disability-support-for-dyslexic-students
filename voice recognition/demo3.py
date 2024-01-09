import speech_recognition as sr
import tkinter as tk

# Create a GUI window for the speech recognition app
window = tk.Tk()
window.title("Speech Recognition App")
window.geometry("400x200")

# Create a label to display the recognized text
label = tk.Label(window, text="")
label.pack()

# Create a function to recognize speech
def recognize_speech():
    # Create a recognizer object
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust the recognizer for ambient noise
        r.adjust_for_ambient_noise(source)

        # Listen for the user's speech input
        audio = r.listen(source)

    try:
        # Use Google Speech Recognition to transcribe the speech
        text = r.recognize_google(audio)

        # Display the recognized text in the GUI
        label.config(text=text)
    except sr.UnknownValueError:
        # Handle speech recognition errors
        label.config(text="Sorry, I could not understand your speech")
    except sr.RequestError as e:
        # Handle network errors
        label.config(text="Sorry, an error occurred while accessing Google Speech Recognition: {}".format(e))

# Create a button to start speech recognition
button = tk.Button(window, text="Start Speech Recognition", command=recognize_speech)
button.pack()

# Run the GUI window
window.mainloop()
