from win32com.client import Dispatch
speak = Dispatch("SAPI.Spvoice")
speak.Speak("hello Aditya")
speak.Speak("How are You")