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
      git clone https://github.com/your-username/raisin.git
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

Well, imagine a bunch of grapes sitting on your kitchen counter. They're plump, colorful, and bursting with flavor. Now, what happens when those grapes get a little too comfortable and decide to stick around a bit longer? They transform into raisins!

Just like those grapes, our software has the magical power to shrink the size of your data. But fear not! We're not here to take away any of its nutritious goodness. Raisin works its compression magic while keeping every single bit intact and retrievable.

So, think of Raisin as your data's personal nutritionist. It takes your files, gives them a little squeeze, and voilà! They become compact, travel-friendly, and ready to be stored or transmitted with ease.

Next time you use Raisin, remember the grape-to-raisin transformation. It's a small change that makes a big difference!

Happy compressing, and raisin up your data game! 🍇✨
