#################################################
# Mike Solie                                    #                                   #
# 01/29/2023                                    #                                        #                                   #
# Master Boot Map                               #
#                                               #
# Description:                                  #
# This takes 3 locations within a dd file,      #
# uses int to convert the hex locations into    #
# standard integers, then indexes and slices    #
# locations within the Master Boot Record       #
# (that uses LBA format) to output 3 specific   #
# locations. The Status Byte, Partition Type    #
# and the First Absolute Sector.                #
#################################################

# import struct library to unpack the sliced bytes in the get_info function
import struct

#####
# function: read_file
# purpose: To read a file, specifically in binary
# inputs: File name, block.dd
# returns: block which is the read file
#####
def read_file(file_name):
    # opens and reads the file in binary
    with open(file_name, 'rb') as f:

        # stores the read contents in the variable "block"
        block = f.read(512)
    return block

#####
# function: get_info
# purpose: to interpret and analyze MBR hexadecimal locations
# inputs: hexadecimal disk addresses
# returns: the integer values of the status byte, partition type and sector address
#####
def get_info(block):
    # stores the location in the variable offset and uses int to convert
    offset = int('1BE', 16)

    # uses offset as an index to find and store the status byte
    status_byte = block[offset]

    # same as above but is located 4 bytes higher
    partition_type = block[offset + 4]

    # using struct.unpack (because there are 4 bytes) the location is sliced and output from 8 to 11 (this is what I think is happening, I'm not entirely sure)
    sector_address = struct.unpack('<i', block[offset + 8:offset + 12])[0]
    return status_byte, partition_type, sector_address

#####
# function: main
# purpose: to run the program
# inputs: file name
# returns: nothing, just runs and prints
#####
def main():
    info = read_file('block.dd')
    status_byte, partition_type, sector_address = get_info(info)
    print(f'Status Byte: {status_byte}')
    print(f'Partition Type: {partition_type}')
    print(f'Primary Sector: {sector_address}')

# call to start the program
##---->
main()
##<----
# program end
