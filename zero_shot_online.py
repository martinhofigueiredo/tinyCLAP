from gradio_client import Client, handle_file

def zeroshot(file, prompt):
    # zero shot through gradio api in huggingface space
    client = Client("fpaissan/tinyCLAP")
    result = client.predict(
            wav_path=handle_file(file),
            prompt=prompt,
            api_name="/predict"
    )

    return result




if __name__ == "__main__":
    output = zeroshot("/home/martinhof/Github/tinyCLAP/datasets/ESC50/ESC-50-master/audio/1-7973-A-7.wav","this is the sound of a rodent")
    # Output the result
    print("Inference Output:", output)



