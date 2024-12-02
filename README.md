# HinglishEval
Artifact for **HinglishEval: Evaluating the Effectiveness of Code-generation Models on Hinglish Prompts**.

### Background
Hindi is one of the most widely spoken languages in the world, and the most widely spoen in India. A majority of the population in India does not speak English as their first language, and therefore language models that can understand prompts in native languages are important for wider accessibility. Hinglish is a blend of Hindi and English, with frequent usage of English words in sentences with standard Hindi grammar. This is not representative of everyday spoken Hindi for most people, but is rather common in coversations involving technical language, especially in the context of programming.

Therefore it is most natural for Hindi speaking users to prompt LLMs in Hinglish when they want to generate code, or ask for help with programming in general (like explanations or debugging). We therefore present **HinglishEval**, a benchmark for evaluating the effectiveness of code-generation models on Hinglish prompts.

## Contributions

### The HinglishEval Benchmark
Our benchmark is based on OpenAI's [HumanEval Benchmark](https://github.com/openai/human-eval). HinglishEval contains all the problems in the HumanEval with their prompts translated to Hinglish. We used GPT-4 to translate the prompts and manually verified and corrected those translations. HinglishEval is available in JSON format in this repository as `HinglishEval.json`.

For each prompt in HumanEval, we translated the purpose statements (supplied as _docstrings_ in Python) to Hinglish ensuring that the translations are idiomatic and preserve the original meaning. We do not modify function signatures or any doctests present in the docstrings.

### Code Samples

We have released code samples for 18 different models from prompts in both English (HumanEval) and Hinglish (HinglishEval). These include both open- and closed-source models. Further, we provide both unsanitized (raw) and sanitized (processed) code samples. The sanitization process removes erroneous or irrelevant code and text from the outputs, and retains only the required function definitions. Note that all the code samples are generated using a temperature setting of 0 (greedy decoding).

The code samples from English prompts are available in the [English Data Release](https://github.com/mrigankpawagi/HinglishEval/releases/tag/English) and the code samples from Hinglish prompts are available in the [Hinglish Data Release](https://github.com/mrigankpawagi/HinglishEval/releases/tag/Hinglish). These code samples will allow reliable reproduction of the results presented in our paper. We understand that running LLMs can be complicated and expensive, and hope that these code samples will help motivate further research in this area.

### Evaluation of Models on HinglishEval

We evaluated 18 models on the HinglishEval dataset using following two metrics.

- **Pass@1**, which measures the percentage of times the model generates correct code on the first attempt. Note that the models were run with a temperature setting of 0 (greedy decoding).

- **Item Response Theory** or IRT, a statistical framework for evaluating the relative capabilities of models based on the hardness of the problems presented to them. We use a 2-parameter IRT model to compute the latent abilities (competencies) of the models from the difficulty ($\beta$) and discrimination ($\alpha$) parameters of each problem.
<br>
Difficulty roughly measures how models perform at a problem on average, while discrimination roughly measures how well a problem differentiates between high- and low-performing models.

## Usage

Here is a brief overview on duplicating the results, running the codes and evaluating the models on the HinglishEval benchmark.

### 1. Cloning the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/mrigankpawagi/HinglishEval.git
cd HinglishEval
```

### 2. Setting up the Environment

Some of the models will be downloaded locally via [HuggingFace](https://huggingface.co/models) like codegen, polycoder, gemma, etc. while others like gpt, mistral, llama, etc. use API-KEYS to access these models. We use mainly two distributors which are [OpenAI](https://openai.com) and [DeepInfra](https://deepinfra.com) You have to setup your own API Keys and set them in the `.env` file as present in the cloned repository.
<br>

You can find the link to obtain the API Keys for [OPENAI](https://openai.com/index/openai-api/), [DEEPINFRA](https://deepinfra.com/docs/deep_infra_api) and [HUGGING FACE](https://huggingface.co/docs/api-inference/en/index) in the respective links.

<br>
Next thing to do is to install some requirements which are necessary to run the code. You can create a virtual environment and install the requirements using the following commands:

```bash
python3 -m venv hinglisheval
source hinglisheval/bin/activate
pip install -r requirements.txt
```

Lastly(optional), we need to install `[HumanEval.json](https://github.com/openai/human-eval/blob/master/data)` file if you are interested in generating `English` generations or reprodice `HinglishEval.json`. This can be done by running the following command:

```bash
curl -O https://github.com/openai/human-eval/raw/refs/heads/master/data/HumanEval.jsonl.gz
gunzip HumanEval.jsonl.gz
```

### 3. Running the Code

- You can run and obtain code samples of various models by running codes in the `[samples/codemodels](/samples/codemodels)` directory.
- You can generate the HinglishEval dataset by running the code in the `[samples/tools](/samples/tools)` directory.
