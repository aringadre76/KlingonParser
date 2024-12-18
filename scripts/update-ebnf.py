def update_ebnf_with_vocab(nouns_file, verbs_file, ebnf_file):
    # Read nouns from file
    with open(nouns_file, 'r') as f:
        nouns = [line.strip() for line in f if line.strip()]

    # Read verbs from file
    with open(verbs_file, 'r') as f:
        verbs = [line.strip() for line in f if line.strip()]

    # Read the existing EBNF grammar
    with open(ebnf_file, 'r') as f:
        ebnf_content = f.readlines()

    # Update <simple_noun> section
    noun_section_found = False
    updated_ebnf = []
    for line in ebnf_content:
        if "<simple_noun> ::=" in line:
            noun_section_found = True
            line = f'<simple_noun> ::= {" | ".join(f"{noun}" for noun in nouns)}\n'
        updated_ebnf.append(line)
    
    if not noun_section_found:
        raise ValueError("<simple_noun> section not found in the EBNF file.")

    # Update <verb> section
    verb_section_found = False
    for i, line in enumerate(updated_ebnf):
        if "<verb> ::=" in line:
            verb_section_found = True
            updated_ebnf[i] = f'<verb> ::= {" | ".join(f"{verb}" for verb in verbs)}\n'
            break

    if not verb_section_found:
        raise ValueError("<verb> section not found in the EBNF file.")

    # Write the updated EBNF to the file
    with open(ebnf_file, 'w') as f:
        f.writelines(updated_ebnf)

# Paths to the files (adjust paths as needed)
nouns_file_path = "../klingon-nouns.txt"
verbs_file_path = "../klingon-verbs.txt"
ebnf_file_path = "../klingon-grammar-ebnf.txt"

# Run the update
update_ebnf_with_vocab(nouns_file_path, verbs_file_path, ebnf_file_path)
