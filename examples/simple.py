# """
# wget https://huggingface.co/thewh1teagle/phonikud-onnx/resolve/main/phonikud-1.0.int8.onnx
# uv sync
# uv run python examples/simple.py
# """

# from phonikud_onnx import Phonikud
# from phonikud import lexicon


# def main():
#     phonikud = Phonikud("./phonikud-1.0.int8.onnx")
#     sentence = "כמה אתה חושב שזה יעלה לי? אני מגיע לשם רק בערב.."
#     with_diacritics = phonikud.add_diacritics(
#         sentence, mark_matres_lectionis=lexicon.NIKUD_HASER_DIACRITIC
#     )
#     print(with_diacritics)


# if __name__ == "__main__":
#     main()




"""
uv run examples/example_tts.py
"""
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from chatterbox.models.utils import get_device

# Automatically detect the best available device
device = get_device()

print(f"Using device: {device}")

model = ChatterboxTTS.from_pretrained(device=device)

text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
wav = model.generate(text)
ta.save("test-1.wav", wav, model.sr)

multilingual_model = ChatterboxMultilingualTTS.from_pretrained(device=device)
text = "Bonjour, comment ça va? Ceci est le modèle de synthèse vocale multilingue Chatterbox, il prend en charge 23 langues."
wav = multilingual_model.generate(text, language_id="fr")
ta.save("test-2.wav", wav, multilingual_model.sr)


# If you want to synthesize with a different voice, specify the audio prompt
AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
ta.save("test-3.wav", wav, model.sr)
