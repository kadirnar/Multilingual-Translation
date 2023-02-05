from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


def m2m100_translate(model_id: str, input_text: str, base_lang: str, target_lang: str):
    model = M2M100ForConditionalGeneration.from_pretrained(model_id)
    tokenizer = M2M100Tokenizer.from_pretrained(model_id)

    base_lang = tokenizer.src_lang = base_lang
    target_lang = tokenizer.get_lang_id(target_lang)
    encoder = tokenizer(input_text, return_tensors="pt")
    generated_tokens = model.generate(**encoder, forced_bos_token_id=target_lang)
    output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return output





