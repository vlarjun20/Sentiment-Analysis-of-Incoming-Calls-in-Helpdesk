
# Sentiment Analysis of Incoming Calls in Helpdesk


This repository contains a sentiment analysis application for incoming helpdesk calls using the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face. It automatically classifies the sentiment of calls into positive, neutral, or negative, helping support teams respond more effectively.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

In helpdesk operations, understanding the sentiment of incoming calls can significantly enhance customer support by prioritizing and addressing issues effectively. This project leverages the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face to analyze the sentiment of call transcripts.

## Features

- **Pre-trained BERT Model**: Utilizes `nlptown/bert-base-multilingual-uncased-sentiment` from Hugging Face.
- **Multilingual Support**: Supports multiple languages, making it versatile for international helpdesks.
- **Sentiment Classification**: Classifies text into five sentiment classes ranging from very negative to very positive.
- **Scalable**: Easily integrates with existing helpdesk systems.
- **Real-time Analysis**: Supports real-time sentiment analysis of incoming calls.

## Installation

To get started, clone the repository and install the required packages.

```bash
git clone https://github.com/vlarjun20/sentiment analysis of incoming on helpdesk.git
cd sentiment analysis of incoming calls on helpdesk
pip install -r requirements.txt
```

### Prerequisites

- Python 3.8 or higher
- PyTorch
- Transformers by Hugging Face
- Pandas
- Scikit-learn

## Usage

1. **Prepare your data**: Ensure your call transcripts are in a CSV format with a `text` column containing the call text.
2. **Run sentiment analysis**: Use the provided script to classify sentiments.

```bash
python analyze_sentiment.py --input data/calls.csv --output results/sentiments.csv
```

3. **Results**: The output will be a CSV file with an additional `sentiment` column indicating the sentiment for each call.

## Dataset

The application requires a dataset of call transcripts. The dataset should be in a CSV format with at least one column named `text` containing the call text. Sample dataset can be found in the `data` folder.

## Model

The project uses the `nlptown/bert-base-multilingual-uncased-sentiment` model from the [Transformers library](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment). You can load the model and tokenizer using:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
```

## Results

The model achieves high accuracy in classifying the sentiments of the calls. Detailed performance metrics are available in the `results` folder.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Hugging Face for their Transformers library.
- PyTorch for the deep learning framework.
- All contributors for their valuable inputs.

---
