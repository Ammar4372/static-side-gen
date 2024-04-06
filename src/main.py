from htmlnode import LeafNode
from block_markdown import markdown_to_blocks

def main():
    node1 = LeafNode('p','this is a paragraph',{"hidden": "true",'color':'black'})
    print(node1.to_html())
    markdown_to_blocks('''# This is a heading
    This is a paragraph of text. It has some **bold** and *italic* words inside of it.
                       
    * This is a list item
    * This is another list item''')
main()