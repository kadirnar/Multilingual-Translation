from transformers import pipeline, set_seed


def text_to_text_generation(
    prompt: str,
    model_id: str,
    device: str,
    target_lang: str,
):

    pipe = pipeline(task="text2text-generation", model=model_id, device=device)
    set_seed(42)
    prediction = pipe(
        prompt, 
        max_length=200, 
        num_return_sequences=1, 
        forced_bos_token_id=pipe.tokenizer.get_lang_id(target_lang))[0]
    
    return prediction["generated_text"]


if __name__ == "__main__":
    text_output = text_to_text_generation(
        prompt="Merhaba", model_id="facebook/m2m100_418M", device="cuda:0", target_lang="en")

    print(text_output)
