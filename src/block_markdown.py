def markdown_to_blocks(text: str) -> list:
    blocks = text.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block == '':
            continue
        stripped_blocks.append(stripped_block)
    return stripped_blocks