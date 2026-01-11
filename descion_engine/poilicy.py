from hate_speech.labels import SAFE, MILD, SEVERE

def decide(severity):
    if severity == SAFE:
        return {
            "allow": True,
            "message": None
        }

    if severity == MILD:
        return {
            "allow": False,
            "message": "Please use respectful language."
        }

    if severity == SEVERE:
        return {
            "allow": False,
            "message": "Your message violates community guidelines and has been blocked."
        }
