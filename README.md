# Genomic Data Processing Project

This project is structured to facilitate the processing and analysis of genomic data, specifically focusing on the GRCh38 genome. It employs Python for data processing and analysis, and utilizes Poetry for dependency management.

## Project Structure

### Root Directory
- `README.md`: This file, providing an overview and setup instructions for the project.
- `data`: Directory containing data and scripts related to genomic, protein, and transcript sequences.
- `gemb`: A Python package/module for implementing project-specific functionalities.
- `poetry.lock` & `pyproject.toml`: Configuration and lock files for Poetry, ensuring consistent dependency resolution.

### Data Directory
- `download_grch38.sh`: A shell script for downloading GRCh38 genomic data.
- Subdirectories containing specific biological data:
  - `genomes`: Contains genome sequences and their index.
  - `proteins`: Contains protein sequences and their index.
  - `transcripts`: Contains transcript sequences and their index.

### Gemb Directory
- `__init__.py`: Initializes the `gemb` directory as a Python package/module.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Poetry (for dependency management)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/ptmorris03/g-emb.git 
   ```
2. Navigate to the project directory and install dependencies using Poetry:
   ```sh
   cd g-emb 
   poetry install
   ```
3. Execute the `download_grch38.sh` script to download the GRCh38 data:
   ```sh
   bash ./data/download_grch38.sh
   ```

## Usage
(Provide usage instructions, examples, and/or code snippets here)

## Contributing
(Provide guidelines on how to contribute to this project)

## License
(Provide license information)

## Acknowledgements
(Provide acknowledgements, if any)

