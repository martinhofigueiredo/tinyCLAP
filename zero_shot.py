from transformers import AutoModel, AutoProcessor
import torch
import torchaudio
import os

# Load the Hugging Face model and processor
def load_model_and_processor(model_path):
    model = AutoModel.from_pretrained(model_path)
    processor = AutoProcessor.from_pretrained(model_path)
    model.eval()
    return model, processor

# Preprocess the audio file
def preprocess_audio(audio_path, processor, target_sample_rate=16000):
    waveform, sample_rate = torchaudio.load(audio_path)

    # Resample if needed
    if sample_rate != target_sample_rate:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=target_sample_rate)
        waveform = resampler(waveform)

    # Use the processor to prepare the inputs
    inputs = processor(waveform.squeeze(0), sampling_rate=target_sample_rate, return_tensors="pt")
    return inputs

# Perform zero-shot inference
def zero_shot_inference(model, inputs):
    with torch.no_grad():
        output = model(**inputs)
    return output

if __name__ == "__main__":
    # Path to the Hugging Face model and the audio file
    model_path = os.path.join(os.path.dirname(__file__), "models")
    audio_path = "/home/martinhof/Github/tinyCLAP/datasets/ESC-50-master/audio/1-7973-A-7.wav"  # Replace with the path to your audio file

    # Load model and processor
    print("Loading model and processor...")
    model, processor = load_model_and_processor(model_path)

    # Preprocess audio
    print("Preprocessing audio...")
    inputs = preprocess_audio(audio_path, processor)

    # Perform inference
    print("Performing zero-shot inference...")
    output = zero_shot_inference(model, inputs)

    # Output the result
    print("Inference Output:", output)
