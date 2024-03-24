import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests

# Function to perform task automation (mock function for sending email)
def send_email(recipient, subject, body):
    output_text.insert(tk.END, f"Sending email to {recipient} with subject: '{subject}' and body: '{body}'\n")

# Function to perform task automation (mock function for fetching weather)
def get_weather(location):
    # Mock API call to get weather data
    response = requests.get(f"https://api.weather.com/weather/{location}")
    if response.status_code == 200:
        return response.json()['weather']
    else:
        return "Weather data unavailable"

# Function to handle user commands
def handle_command(command):
    tokens = word_tokenize(command)
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
    if 'email' in tokens:
        # Extract email details
        recipient = tokens[tokens.index('to') + 1]
        subject_start_index = tokens.index('subject') if 'subject' in tokens else -1
        if subject_start_index != -1:
            subject = ' '.join(tokens[subject_start_index + 1:])
            body_start_index = tokens.index('body') if 'body' in tokens else -1
            if body_start_index != -1:
                body = ' '.join(tokens[body_start_index + 1:])
                send_email(recipient, subject, body)
            else:
                output_text.insert(tk.END, "Please specify email body.\n")
        else:
            output_text.insert(tk.END, "Please specify email subject.\n")
    elif 'weather' in tokens:
        location_index = tokens.index('weather') + 1
        location = tokens[location_index]
        weather_info = get_weather(location)
        output_text.insert(tk.END, f"Weather in {location}: {weather_info}\n")
    else:
        output_text.insert(tk.END, "Command not recognized.\n")

# Function to listen to user's voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_text.insert(tk.END, "Listening...\n")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        output_text.insert(tk.END, "Processing...\n")
        command = recognizer.recognize_google(audio)
        output_text.insert(tk.END, f"User said: {command}\n")
        handle_command(command)
    except sr.UnknownValueError:
        output_text.insert(tk.END, "Could not understand audio.\n")
    except sr.RequestError as e:
        output_text.insert(tk.END, f"Error: {e}\n")

# GUI Setup
root = tk.Tk()
root.title("Voice Assistant")

# Create output text area
output_text = tk.Text(root, wrap=tk.WORD, height=20, width=50)
output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Configure style for buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, relief=tk.FLAT, background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])

# Create Listen button
listen_button = ttk.Button(root, text="Listen", command=listen)
listen_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Create Quit button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Run the application
root.mainloop()
