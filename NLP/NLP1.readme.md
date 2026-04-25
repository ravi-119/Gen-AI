# NLP Fundamentals - Text Preprocessing Guide

Welcome to the NLP session! This guide covers the essential concepts of Natural Language Processing and the fundamental text preprocessing techniques.

---

## What is NLP?

**Natural Language Processing (NLP)** is a branch of artificial intelligence that helps computers understand, interpret, and manipulate human language. It bridges the gap between human communication and computer understanding.

### Why NLP Matters?
- **Chatbots** - Understanding user queries
- **Sentiment Analysis** - Detecting emotions in reviews
- **Machine Translation** - Translating languages
- **Text Summarization** - Condensing long documents
- **Search Engines** - Understanding search intent

---

## Text Preprocessing

Before feeding text to AI models, we need to clean and prepare it. This is called **Text Preprocessing**.

### Why Preprocess?
- Raw text contains noise (special characters, capitalization, etc.)
- Computers understand numbers better than words
- Reduces vocabulary size for efficient processing
- Improves model accuracy

---

## 1. Tokenization

**Tokenization** is the process of breaking text into smaller units called **tokens** (words, sentences, or characters).

### Types of Tokenization

#### Word Tokenization
Splits text into individual words.

```python
# Example
text = "NLP is amazing!"

# Tokens: ["NLP", "is", "amazing", "!"]
```

#### Sentence Tokenization
Splits text into sentences.

```python
# Example
text = "Hello! How are you? I'm fine."

# Tokens: ["Hello!", "How are you?", "I'm fine."]
```

### Real-World Example
```
Input:  "I love learning NLP. It's fascinating!"
Output: ["I", "love", "learning", "NLP", ".", "It's", "fascinating", "!"]
```

---

## 2. Stopwords

**Stopwords** are common words that appear frequently but carry little meaning (e.g., "the", "is", "and", "a").

### Why Remove Stopwords?
- Reduces data size
- Focuses on meaningful words
- Improves processing speed

### Common Stopwords
```
the, is, at, which, on, a, an, and, or, but, in, with, to, for, of, as, by
```

### Example
```
Original: "The cat is sitting on the mat"
After removing stopwords: "cat sitting mat"
```

### Python Example
```python
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

text = "The quick brown fox jumps over the lazy dog"
words = text.split()
filtered = [w for w in words if w.lower() not in stopwords.words('english')]
# Result: ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']
```

---

## 3. Stemming

**Stemming** reduces words to their root form by chopping off prefixes/suffixes. It's a fast, rule-based process.

### Example
| Original Word | Stemmed Word |
|---------------|--------------|
| running | run |
| runs | run |
| runner | run |
| happily | happi |
| connection | connect |

### Types of Stemmers
1. **Porter Stemmer** - Most common, gentle
2. **Snowball Stemmer** - Improved Porter
3. **Lancaster Stemmer** - Aggressive

### Python Example
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "runs", "runner", "connection"]

for word in words:
    print(f"{word} -> {stemmer.stem(word)}")

# Output:
# running -> run
# runs -> run
# runner -> run
# connection -> connect
```

### ⚠️ Limitation
Stemming can produce non-words:
- "happily" → "happi" (not a real word)
- "university" → "univers" (loses meaning)

---

## 4. Lemmatization

**Lemmatization** reduces words to their dictionary base form (lemma). It considers the context and part of speech.

### Example
| Original Word | Lemma | Stem |
|---------------|-------|------|
| running | run | run |
| runs | run | run |
| better | good | better |
| children | child | children |
| went | go | went |

### Python Example
```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = ["running", "runs", "better", "children", "went", "dogs"]

for word in words:
    print(f"{word} -> {lemmatizer.lemmatize(word)}")

# Output:
# running -> running
# runs -> run
# better -> better
# children -> child
# went -> went
# dogs -> dog
```

### ⚠️ Note
By default, lemmatizer treats words as nouns. Use POS tags for better results:
```python
# Verb lemmatization
print(lemmatizer.lemmatize("running", pos='v'))  # run
print(lemmatizer.lemmatize("better", pos='a'))   # good
```

---

## Stemming vs Lemmatization

| Feature | Stemming | Lemmatization |
|---------|----------|---------------|
| Speed | Fast | Slow |
| Accuracy | Lower | Higher |
| Output | May be non-word | Real dictionary word |
| Context | Ignores context | Uses POS tagging |
| Use Case | Large datasets | When accuracy matters |

### Quick Comparison
```
Word: "running"

Stemming:  "run"    (chops "ning")
Lemmatization: "run" (dictionary form)

Word: "better"

Stemming:  "better" (no change)
Lemmatization: "good" (dictionary form)

Word: "children"

Stemming:  "children" (no change)
Lemmatization: "child"  (dictionary form)
```

---

## Complete Pipeline Example

Here's how all techniques work together:

```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

text = "The children were running happily in the beautiful garden"

# 1. Tokenization
tokens = text.split()
print("1. Tokenization:", tokens)

# 2. Remove Stopwords
filtered = [t for t in tokens if t.lower() not in stopwords.words('english')]
print("2. Remove Stopwords:", filtered)

# 3. Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(t) for t in filtered]
print("3. Stemming:", stemmed)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(t) for t in filtered]
print("4. Lemmatization:", lemmatized)

# Output:
# 1. Tokenization: ['The', 'children', 'were', 'running', 'happily', 'in', 'the', 'beautiful', 'garden']
# 2. Remove Stopwords: ['children', 'running', 'happily', 'beautiful', 'garden']
# 3. Stemming: ['children', 'run', 'happili', 'beauti', 'garden']
# 4. Lemmatization: ['child', 'running', 'happily', 'beautiful', 'garden']
```

---

## Summary

| Technique | Purpose | Example |
|-----------|---------|---------|
| **Tokenization** | Split text into tokens | "Hello world" → ["Hello", "world"] |
| **Stopwords** | Remove common words | "the cat" → "cat" |
| **Stemming** | Cut words to root form | "running" → "run" |
| **Lemmatization** | Dictionary form | "children" → "child" |

---