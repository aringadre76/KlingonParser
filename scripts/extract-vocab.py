import re

def extract_vocab(input_file, nouns_file, verbs_file):
    # Patterns to identify nouns and verbs
    noun_pattern = r"'''([\w`']+)''' - ''n''"
    verb_pattern = r"'''([\w`']+)''' - ''v''"
    
    nouns = []
    verbs = []

    with open(input_file, 'r') as f:
        for line in f:
            # Find nouns
            noun_match = re.search(noun_pattern, line)
            if noun_match:
                nouns.append(noun_match.group(1))
            
            # Find verbs
            verb_match = re.search(verb_pattern, line)
            if verb_match:
                verbs.append(verb_match.group(1))

    # Write nouns to file
    with open(nouns_file, 'w') as f:
        for noun in nouns:
            f.write(f"{noun}\n")

    # Write verbs to file
    with open(verbs_file, 'w') as f:
        for verb in verbs:
            f.write(f"{verb}\n")

# Define file paths
input_vocab_file = "../klingon-dictionary.txt"
nouns_output_file = "../klingon-nouns.txt"
verbs_output_file = "../klingon-verbs.txt"

# Run the extraction
extract_vocab(input_vocab_file, nouns_output_file, verbs_output_file)
