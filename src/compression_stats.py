import sys
from rich import print
from rich.console import Console
from rich.table import Table

def calculate_original_size(data):
    
    return sys.getsizeof(data)


def calculate_compressed_size(compressed_data):
    
    return sys.getsizeof(compressed_data)


def calculate_compression_ratio(original_size, compressed_size):

    return compressed_size / original_size


def calculate_compression_percentage(original_size, compressed_size):

    return ((original_size - compressed_size) / original_size) * 100


def calculate_efficiency(original_size, compressed_size):

    return (compressed_size / original_size) * 100

def print_stats(original_data_size, l1_packed_data_size, l2_packed_data_size, final_packed_data_size):

    print('\nCOMPRESSION STATISTICS:')
    table = Table(show_lines=False)
    table.add_column("Data", style="cyan", width=20)
    table.add_column("Size", justify="right", style="green")

    table.add_row("Original File", str(original_data_size) + " B")
    table.add_row("Compressed File", str(final_packed_data_size) + " B")
    table.add_row("Size Difference", str(round(original_data_size - final_packed_data_size, 3)) + " B")
    table.add_row("Compression Ratio", str(round(calculate_compression_ratio(original_data_size, final_packed_data_size), 3)) + " ")
    table.add_row("Compression %", str(round(calculate_compression_percentage(original_data_size, final_packed_data_size), 3)) + " %")
    table.add_row("Efficiency", str(round(calculate_efficiency(original_data_size, final_packed_data_size),3)) + " ")

    console = Console()
    console.print(table)
