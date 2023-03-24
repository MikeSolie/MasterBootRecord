# MBR Hexadecimal Interpreter 

This Python script reads a binary file and interprets and analyzes the Master Boot Record (MBR) hexadecimal locations. It returns the integer values of the status byte, partition type, and sector address. 

## Installation

1. Clone the repository
2. Make sure Python 3 is installed

## Usage

1. Make sure the binary file is on your local machine
2. Update the `file_name` variable in `main()` so that it matches your files name and location
3. Run the script using `python3 mbr_locate.py`
4. It will output the Status Byte, Partition Type, and Sector Address for the MBR

## Example Output

```
Status Byte: 80
Partition Type: 5 
Primary Sector: 63
```

## Contributing

Contributions are welcome. Feel free to fork this repository and submit a pull request with your changes. Be sure to include a description of your changes and any necessary documentation updates. 

## Credits

This script was created by Mike Solie under the MIT License.

## License

This project is licensed under the terms of the MIT License. Se the LICENSE file for details.
