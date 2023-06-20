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

def print_stats(original_data, l1_data, l2_data, packed_data):
    original_data_size = calculate_original_size(original_data)
    l1_data_size = calculate_original_size(l1_data)
    l2_data_size = calculate_original_size(l2_data)
    packed_data_size = calculate_original_size(packed_data)

    print('\nCOMPRESSION STATISTICS:')
    table = Table(show_lines=False)
    table.add_column("Data Type", style="cyan", width=20)
    table.add_column("Size", justify="right", style="green")

    table.add_row("Original Data", str(original_data_size) + " B")
    table.add_row("L1 Compressed Data", str(l1_data_size) + " B")
    table.add_row("L2 Compressed Data", str(l2_data_size) + " B")
    table.add_row("Packed Data", str(packed_data_size) + " B")

    console = Console()
    console.print(table)
