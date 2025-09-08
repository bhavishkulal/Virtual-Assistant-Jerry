import speech_recognition as sr
import webbrowser 
import pyttsx3
import time
import musiclibrary as ml
import requests
from client import GeminiClient
recogniser = sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...........")
    print("Initializing Jarvis...........")
    # Initialize Gemini client once
    gemini = GeminiClient(api_key="AIzaSyAsuv8ESZ2Rb1ItApmJl9kwFm0HMh2m-9k")
    # Debug: list microphones
    try:
        mic_names = sr.Microphone.list_microphone_names()
        print("Available microphones:")
        for idx, name in enumerate(mic_names):
            print(f"  [{idx}] {name}")
    except Exception as e:
        print(f"Could not list microphones: {e}")

    loop_num = 0
    while True:
        # listen for word jarvis
        #obtain audio from microphone
        try:
            # Recreate recognizer each loop to avoid drift across iterations
            recogniser = sr.Recognizer()
            recogniser.energy_threshold = 250
            recogniser.dynamic_energy_threshold = True
            recogniser.pause_threshold = 0.8

            with sr.Microphone() as source:
                loop_num += 1
                print(f"\n[Loop {loop_num}] Listening...........")
                print(f"Energy threshold (pre-calibration): {recogniser.energy_threshold}")
                recogniser.adjust_for_ambient_noise(source, duration=0.8)
                # Lock in a slightly padded fixed threshold to prevent runaway growth
                recogniser.energy_threshold = max(200, int(recogniser.energy_threshold * 1.2))
                recogniser.dynamic_energy_threshold = False
                print(f"Energy threshold (fixed): {recogniser.energy_threshold}")
                audio = recogniser.listen(source, timeout=6, phrase_time_limit=7)
                try:
                    raw = audio.get_raw_data()
                    print(f"Captured audio bytes: {len(raw)}")
                except Exception:
                    pass
            text = recogniser.recognize_google(audio)
            print(f"You said: {text}")
            # Small pause to avoid overlapping iterations on slower systems
            lower_text = text.lower()
            
            # Check for website opening commands first
            if lower_text=="open google":    
                speak("Opening Google............")
                webbrowser.open("https://www.google.com")
            elif lower_text=="open youtube":
                speak("Opening Youtube............")
                webbrowser.open("https://www.youtube.com")
            elif lower_text=="open facebook":
                speak("Opening Facebook............")
                webbrowser.open("https://www.facebook.com")
            elif lower_text=="open instagram":
                speak("Opening Instagram............")
                webbrowser.open("https://www.instagram.com")
            elif lower_text=="open twitter":
                speak("Opening Twitter............")
                webbrowser.open("https://www.twitter.com")
            elif lower_text=="open linkedin":
                speak("Opening LinkedIn............")
                webbrowser.open("https://www.linkedin.com")
            elif lower_text=="open github":
                speak("Opening GitHub............")
                webbrowser.open("https://www.github.com")
            elif lower_text=="open stackoverflow":
                speak("Opening StackOverflow............")
                webbrowser.open("https://www.stackoverflow.com")
            elif lower_text=="open reddit":
                speak("Opening Reddit............")
                webbrowser.open("https://www.reddit.com")
            elif lower_text=="open wikipedia":
                speak("Opening Wikipedia............")
                webbrowser.open("https://www.wikipedia.org")
            elif lower_text=="open amazon":
                speak("Opening Amazon............")
                webbrowser.open("https://www.amazon.com")
            elif lower_text=="open flipkart":
                speak("Opening Flipkart............")
                webbrowser.open("https://www.flipkart.com")
            elif lower_text=="open netflix":
                speak("Opening Netflix............")
                webbrowser.open("https://www.netflix.com")
            elif lower_text=="open hotstar":
                speak("Opening Hotstar............")
                webbrowser.open("https://www.hotstar.com")
            elif lower_text=="open prime video":
                speak("Opening Prime Video............")
                webbrowser.open("https://www.primevideo.com")
            elif lower_text=="open disney+":
                speak("Opening Disney+............")
                webbrowser.open("https://www.disneyplus.com")
            elif lower_text=="open chatgpt":
                speak("Opening ChatGPT............")
                webbrowser.open("https://www.chatgpt.com")
            elif lower_text.startswith("play"):
                song=lower_text.split("play", 1)[1].strip()
                speak(f"Playing {song}............")
                link=ml.music[song]
                webbrowser.open(link)
            elif lower_text.startswith("ask"):
                question = text[text.lower().find("ask") + 3:].strip()
                if not question:
                    speak("What would you like to ask?")
                else:
                    answer = gemini.ask(question)
                    print(f"Answer: {answer}")
                    speak(answer)
            elif lower_text=="open news":
                speak("Fetching latest news headlines............")
                try:
                    # Using a free news API (NewsAPI) for Indian tech, AI, and startup news
                    api_key = "9c22a1e49d41462b8e26978bc5513e1e"  # You can get a free key from newsapi.org
                    url = f"https://newsapi.org/v2/everything?q=India tech AI startup&language=en&sortBy=publishedAt&apiKey={api_key}"
                    response = requests.get(url)
                    data = response.json()
                    
                    if data['status'] == 'ok':
                        articles = data['articles'][:5]  # Get first 5 headlines
                        speak("Here are the latest Indian tech, AI, and startup news:")
                        for i, article in enumerate(articles, 1):
                            headline = article['title']
                            print(f"{i}. {headline}")
                            speak(f"News {i}: {headline}")
                    else:
                        speak("Sorry, couldn't fetch news at the moment.")
                except Exception as e:
                    print(f"Error fetching news: {e}")
                    speak("Sorry, couldn't fetch news at the moment.")

            elif lower_text=="exit":
                speak("Exiting............")
                print("Exiting............")
                break
            elif lower_text == "jerry":
                speak("yes sir")
            elif lower_text.endswith("?") or lower_text.startswith(("what","who","why","how","when","where","tell me","explain")):
                # Treat as a general question to the LLM
                answer = gemini.ask(text)
                print(f"Answer: {answer}")
                speak(answer)
            else:
                # Fallback: treat as a natural-language question for Gemini
                answer = gemini.ask(text)
                print(f"Answer: {answer}")
                speak(answer)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            time.sleep(0.3)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            time.sleep(0.3)
        except sr.RequestError as e:
            print(f"API error: {e}")
            time.sleep(0.5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(0.5)