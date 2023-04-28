# Paraphrase Generator

This is a Flask web application that generates paraphrases of a given English sentence.

## Installation
1. Clone the repository to your local machine.
2. Create a virtual environment using `python3 -m venv venv`.
3. Activate the virtual environment using `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows).
4. Install the dependencies using `pip install -r requirements.txt`.

## Usage
To start the server, run `python main.py` in your terminal. The server will be hosted at `http://localhost:5000/`.

To generate paraphrases, send a GET request to `http://localhost:5000/paraphrase` with the following query parameters:

- `tree`: A string representation of the sentence's parse tree.
- `limit` (optional): The maximum number of paraphrases to generate (default is 20).

Example usage:

`http://localhost:5000/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter)%20)%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)%20)%20)%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets)%20)%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars)%20)%20(,%20,)%20(NP%20(NNS%20clubs)%20)%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants)%20)%20)%20)%20)%20)%20)%20)`
