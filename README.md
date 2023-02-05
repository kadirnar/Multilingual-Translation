<h2>
  Beyond English-Centric Multilingual Machine Translation
</h2>

<a href="https://badge.fury.io/py/multilingual_translation"><img src="https://badge.fury.io/py/multilingual_translation.svg" alt="pypi version"></a>
<a href="https://huggingface.co/spaces/kadirnar/multilingual_translation"><img src="https://img.shields.io/badge/%20HuggingFace%20-Demo-blue.svg" alt="HuggingFace Spaces"></a>

This repo is a PyTorch implementation of the paper [Beyond English-Centric Multilingual Machine Translation](https://arxiv.org/abs/2010.11125).

### Installation
```bash
pip install multilingual-translation
```
### Usage
```python
from multilingual_translation import translate

translate("facebook/m2m100_418M", "Hello World", "en", "tr") # Merhaba Dünya
```
### Citation
```bibtex
@misc{fan2020englishcentric,
      title={Beyond English-Centric Multilingual Machine Translation}, 
      author={Angela Fan and Shruti Bhosale and Holger Schwenk and Zhiyi Ma and Ahmed El-Kishky and Siddharth Goyal and Mandeep Baines and Onur Celebi and Guillaume Wenzek and Vishrav Chaudhary and Naman Goyal and Tom Birch and Vitaliy Liptchinsky and Sergey Edunov and Edouard Grave and Michael Auli and Armand Joulin},
      year={2020},
      eprint={2010.11125},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
