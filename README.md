# phonikud-chatterbox

Hebrew TTS with [ChatterBox](https://github.com/resemble-ai/chatterbox) and [Phonikud](https://phonikud.github.io)

## Setup

1. Install [Astral uv](https://docs.astral.sh/uv/getting-started/installation) and [wget](http://chat.com/?q=how+to+install+wget+on+each+platform+in+short+mention+winget)

2. Prepare the project and run

```console
wget https://huggingface.co/thewh1teagle/phonikud-onnx/resolve/main/phonikud-1.0.int8.onnx
wget https://github.com/thewh1teagle/phonikud-chatterbox/releases/download/asset-files-v1/ref1.wav
uv run examples/example_tts.py
```