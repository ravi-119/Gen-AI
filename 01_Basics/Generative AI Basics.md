# Large Language Models (LLMs) and Transformer Architecture – End-to-End Notes

## Table of Contents
1. [Introduction to Large Language Models (LLMs)](#introduction-to-large-language-models-llms)
2. [Deep Dive into GPT Architecture](#deep-dive-into-gpt-architecture)
3. [How LLMs Work Under the Hood](#how-llms-work-under-the-hood)
4. [Fundamentals of Tokenization in NLP](#fundamentals-of-tokenization-in-nlp)
5. [Implementing a Custom Tokenizer in Python](#implementing-a-custom-tokenizer-in-python)
6. [The Transformer Breakthrough: Google's Attention Paper](#the-transformer-breakthrough-googles-attention-paper)
7. [Deep Diving into Vector Embeddings](#deep-diving-into-vector-embeddings)
8. [Role of Positional Encoding in Transformer](#role-of-positional-encoding-in-transformer)
9. [Understanding Multi-Head Attention for Rich Context](#understanding-multi-head-attention-for-rich-context)

---

## Introduction to Large Language Models (LLMs)
Large Language Models (LLMs) are deep learning models trained on vast amounts of textual data to understand and generate human-like text. They leverage **transformers** to model complex dependencies in sequences and perform tasks like text completion, summarization, translation, and question-answering.

Key features:
- **Contextual Understanding**: Captures long-range dependencies in text.
- **Generative Capabilities**: Can generate coherent text given a prompt.
- **Pre-training + Fine-tuning**: Pre-trained on large corpora and fine-tuned for specific tasks.

---

## Deep Dive into GPT Architecture
GPT (Generative Pre-trained Transformer) is an autoregressive LLM that predicts the next token in a sequence. Key components:
- **Transformer Decoder Blocks**: Stacks of self-attention layers and feed-forward networks.
- **Layer Normalization**: Stabilizes training and improves convergence.
- **Causal Masking**: Ensures the model only attends to previous tokens.
- **Output Layer**: Linear + Softmax for token probability prediction.

GPT variants (GPT-2, GPT-3, GPT-4) differ mainly in **model size**, **number of layers**, and **training data scale**.

---

## How LLMs Work Under the Hood
1. **Input Text → Tokenization**: Converts text to tokens.
2. **Embedding Layer**: Maps tokens to dense vector representations.
3. **Transformer Layers**:
   - Multi-head self-attention
   - Feed-forward network
   - Residual connections & layer normalization
4. **Prediction**: Outputs probabilities for the next token.
5. **Decoding**: Techniques like greedy, beam search, or sampling generate text.

---

## Fundamentals of Tokenization in NLP
Tokenization splits text into meaningful units (tokens). Types:
- **Word-level Tokenization**: Splits by spaces.
- **Subword Tokenization**: Handles unknown words using pieces (e.g., BPE, WordPiece).
- **Character-level Tokenization**: Splits into characters, useful for morphologically rich languages.

Importance:
- Reduces vocabulary size.
- Enables handling of rare or unseen words.
- Provides inputs suitable for embedding layers.

---

## Implementing a Custom Tokenizer in Python
Example: simple whitespace + punctuation tokenizer

```python
import re

class SimpleTokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
    
    def tokenize(self, text):
        tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
        return tokens
    
    def build_vocab(self, corpus):
        token_set = set()
        for sentence in corpus:
            token_set.update(self.tokenize(sentence))
        self.vocab = {tok: idx for idx, tok in enumerate(sorted(token_set))}
        self.inverse_vocab = {idx: tok for tok, idx in self.vocab.items()}
    
    def encode(self, text):
        return [self.vocab[tok] for tok in self.tokenize(text)]
    
    def decode(self, token_ids):
        return " ".join([self.inverse_vocab[id] for id in token_ids])
