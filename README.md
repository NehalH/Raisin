# Raisin🍇

Raisin is a command-line tool designed to compress text files using layered Huffman encoding techniques. It employs a layered approach, where the data is successively compressed at each layer, resulting in further reduction in size. Python is used as the programming language for the backend implementation.

## Features

- Compresses text files using layered Huffman encoding.
- Reduces the size of data while retaining the original content.
- Utilizes a binary string representation for efficient compression.
- Easy to use as a command-line tool.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/NehalH/Raisin.git
   ```
2. Navigate to the project directory:

   ```shell
   cd raisin
   ```
3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```
<!--
## Usage

To compress a text file using Raisin, run the following command:

shell
Copy code
python raisin.py compress <input_file_path> <output_file_path>
Replace <input_file_path> with the path to the text file you want to compress and <output_file_path> with the desired path for the compressed output file.

To decompress a compressed file and retrieve the original text, use the following command:

```shell
   python raisin.py decompress <compressed_file_path> <output_file_path>
```
Replace `<compressed_file_path>` with the path to the compressed file and `<output_file_path>` with the desired path for the decompressed output file.

Examples
Compress a text file named "example.txt" and save the compressed output as "example.bin":

shell
Copy code
python raisin.py compress example.txt example.bin
Decompress a file named "example.bin" and save the decompressed output as "example_decompressed.txt":

shell
Copy code
python raisin.py decompress example.bin example_decompressed.txt
-->

## Contributing

Contributions to Raisin are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on this repository. Pull requests are also encouraged.


## Why "Raisin"?

Wondering why this compression tool is named "Raisin" ?

Just like plump grapes transform into tiny raisins without loosing their nutrition, Raisin shrinks your data while preserving the real information. It's compression without compromise!

So, Raisin takes your files, gives them a little squeeze, and voilà! They become compact, travel-friendly, and ready to be stored or transmitted with ease.

Next time you use Raisin, remember the grape-to-raisin transformation. It's a small change that makes a big difference!

Happy compressing, and raisin up your data game! 🍇✨
