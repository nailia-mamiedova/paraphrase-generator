import itertools
from flask import Flask, request, jsonify
from nltk.tree import Tree

app = Flask(__name__)


def generate_phrases(tree, phrases):
    if tree.label() == 'NP':
        phrase = ' '.join(tree.leaves())
        phrases.append(phrase)
    for child in tree:
        if isinstance(child, Tree):
            generate_phrases(child, phrases)


def replace_noun_phrases(tree, phrase_permutation):
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            for i, phrase in enumerate(phrase_permutation):
                if ' '.join(subtree.leaves()) == phrase:
                    subtree.clear()
                    subtree.insert(0, Tree.fromstring('(' + phrase + ')'))


@app.route('/paraphrase', methods=['GET'])
def paraphrase():
    tree_string = request.args.get('tree')
    limit = int(request.args.get('limit', 20))
    tree = Tree.fromstring(tree_string)
    phrases = []
    generate_phrases(tree, phrases)
    noun_phrases = [phrase for phrase in phrases if ' ' in phrase]
    paraphrases = []
    for i in range(2, len(noun_phrases)+1):
        for combination in itertools.combinations(noun_phrases, i):
            for permutation in itertools.permutations(combination):
                new_tree = tree.copy(deep=True)
                replace_noun_phrases(new_tree, permutation)
                paraphrase = str(new_tree).replace('\n', '')
                if paraphrase not in paraphrases:
                    paraphrases.append(paraphrase)
                    if len(paraphrases) == limit:
                        break
            else:
                continue
            break
        else:
            continue
        break
    return jsonify({'paraphrases': [{'tree': tree} for tree in paraphrases]})


if __name__ == '__main__':
    app.run(debug=True)
